"""Generate podcast audio from a written script."""

# Import regular expressions to remove formatting before speech generation.
import re
import tempfile

# Import Path to manage the output audio file.
from pathlib import Path

# Import the OpenAI client for text-to-speech generation.
from openai import OpenAI
from pydub import AudioSegment


def clean_script_for_audio(script: str) -> str:
    """Remove Markdown formatting that should not be read aloud."""

    # Remove common Markdown formatting symbols.
    cleaned_script = re.sub(r"[*#_]", "", script)

    # Replace horizontal separators with a space.
    cleaned_script = cleaned_script.replace("---", " ")

    # Reduce three or more blank lines to two blank lines.
    cleaned_script = re.sub(r"\n{3,}", "\n\n", cleaned_script)

    # Remove unnecessary spaces at the start and end.
    return cleaned_script.strip()


def generate_audio(
    podcast: dict,
    api_key: str,
    output_path: str = "outputs/ai_apocalypse_episode.mp3",
) -> str:
    """Generate one combined MP3 from structured podcast segments."""

    # Stop if the API key is missing.
    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing from the environment.")

    # Read the segments from the structured podcast.
    segments = podcast.get("segments", [])

    # Stop if the podcast has no segments.
    if not segments:
        raise ValueError("There are no podcast segments to convert to audio.")

    # Convert the output filename into a Path object.
    destination = Path(output_path)

    # Create the output folder if it does not already exist.
    destination.parent.mkdir(parents=True, exist_ok=True)

    # Create an OpenAI client using the environment API key.
    client = OpenAI(api_key=api_key)

    # Map each speaker to a fixed voice instead of trusting the model's choice.
    speaker_voices = {
        "Ana": "nova",
        "Rui": "alloy",
    }

    # Create a temporary folder for each individual speaker segment.
    with tempfile.TemporaryDirectory() as temporary_folder:
        # Start with an empty audio track.
        combined_audio = AudioSegment.empty()

        # Generate and combine audio for every segment in order.
        for segment_number, segment in enumerate(segments, start=1):
            # Clean Markdown from the current segment.
            segment_text = clean_script_for_audio(segment["text"])

            # Select the voice from the speaker name.
            voice = speaker_voices.get(segment.get("speaker"), "nova")

            # Define a temporary path for the current segment.
            segment_path = Path(temporary_folder) / f"segment_{segment_number}.mp3"

            # Generate streamed MP3 audio for the current segment.
            with client.audio.speech.with_streaming_response.create(
                model="gpt-4o-mini-tts",
                voice=voice,
                input=segment_text,
                response_format="mp3",
            ) as response:
                # Save the current segment to its temporary file.
                response.stream_to_file(segment_path)

            # Add a short pause between speakers.
            combined_audio += AudioSegment.from_mp3(segment_path)
            combined_audio += AudioSegment.silent(duration=400)

        # Export all segments as one final MP3 file.
        combined_audio.export(destination, format="mp3")

    # Return the path so Gradio can play the audio.
    return str(destination)


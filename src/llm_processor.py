"""Create a structured podcast from one or more source articles."""

# Import json to convert the model's structured response into Python data.
import json

# Import the OpenAI client used to call the language model.
from openai import OpenAI


def create_podcast_script(article_text: str, api_key: str, model: str = "gpt-4o-mini") -> dict:
    """Turn combined article text into a structured, multi-speaker podcast."""

    # Stop early when no API key was provided.
    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing from the environment.")

    # Stop early when no article text was provided.
    if not article_text.strip():
        raise ValueError("No article text was provided.")

    # Create an OpenAI client using the API key from the environment.
    client = OpenAI(api_key=api_key)

    # Define the instructions and the JSON format required from the model.
    instructions = """
    You are a careful and engaging podcast scriptwriter.

    Create a podcast episode about the topic: "AI Apocalypse".

    Use all three source articles provided by the user. Compare their
    perspectives and explain how they connect to the wider question of
    whether AI could cause serious harm or threaten humanity.

    Return ONLY valid JSON in this exact structure:
    {
      "title": "Podcast title",
      "segments": [
        {
          "speaker": "Ana",
          "voice": "nova",
          "text": "Spoken segment text"
        }
      ]
    }

    The podcast must:
    - Use 8 to 14 segments.
    - Use the speakers Ana and Rui.
    - Ana is a curious host who asks practical questions, pushes back on hype, and keeps the discussion concrete.
    - Rui is an expert host who explains clearly, uses examples, separates evidence from speculation, and gives balanced views.
    - Use voice "nova" for Ana and "alloy" for Rui.
    - Explain the main point of each article.
    - Identify the source article behind important claims.
    - Distinguish evidence, expert opinions, predictions, and speculation.
    - Present both risks and reasons not to panic.
    - Avoid inventing facts, statistics, or sources.
    - Avoid claiming that an AI apocalypse will definitely happen.
    - Be approximately 1,000 to 1,500 words in total.
    """

    # Send the instructions and combined article text to the language model.
    response = client.responses.create(
        model=model,
        instructions=instructions,
        input=article_text,
    )

    # Extract the JSON text from the model response.
    json_text = response.output_text.strip()

    # Remove a possible Markdown code fence around the JSON.
    if json_text.startswith("```json"):
        json_text = json_text[len("```json"):]
    if json_text.endswith("```"):
        json_text = json_text[:-3]
    json_text = json_text.strip()

    # Convert the JSON text into a Python dictionary.
    podcast = json.loads(json_text)

    # Check that the expected JSON fields are present.
    if not podcast.get("title") or not podcast.get("segments"):
        raise ValueError("The model returned incomplete podcast JSON.")

    # Validate each segment before sending it to text-to-speech.
    for segment in podcast["segments"]:
        if not segment.get("speaker") or not segment.get("text"):
            raise ValueError("A podcast segment is missing a speaker or text.")

    # Return the completed structured podcast.
    return podcast


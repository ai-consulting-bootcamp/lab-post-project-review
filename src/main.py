"""Gradio application for the AI Apocalypse podcast studio."""

# Import json to display the structured podcast clearly.
import json
from pathlib import Path

# Import os to read the API key from the environment.
import os

# Import typing helpers for Python 3.8 compatibility.
from typing import List, Optional, Tuple

# Import Gradio to create the web interface.
import gradio as gr

# Import load_dotenv to read the local .env file.
from dotenv import load_dotenv

# Import the function that combines multiple PDF articles.
from data_processor import combine_pdf_files

# Import the function that creates the podcast script.
from llm_processor import create_podcast_script

# Import the function that generates the MP3 file.
from tts_generator import generate_audio


# Load environment variables from .env.
load_dotenv()

# Define the visual styling for the Gradio application.
custom_css = """
body {
    background: #0b0f19;
    min-height: 100vh;
}

.gradio-container {
    max-width: 1140px !important;
    margin: auto;
    background: #0b0f19 !important;
    padding-bottom: 60px !important;
}

.app-header,
.upload-panel,
.settings-panel,
.result-panel,
.script-panel {
    background: #202735 !important;
    border: 1px solid #303a4d !important;
    border-radius: 12px !important;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.18) !important;
}

.app-header {
    padding: 12px 18px !important;
    margin-bottom: 14px !important;
}

.app-header h1 {
    color: #f8fafc !important;
    font-size: 2rem !important;
    margin-bottom: 8px !important;
}

.app-header p,
.settings-panel p,
.result-panel p {
    color: #cbd5e1 !important;
}

button.primary,
.generate-button button {
    background: linear-gradient(
        90deg,
        #7c3aed,
        #db2777
    ) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
    min-height: 50px !important;
}

.generate-button {
    margin: 18px 0 !important;
}

textarea,
input {
    border: 1px solid #a78bfa !important;
    border-radius: 10px !important;
}

.tabs {
    border: 1px solid #303a4d !important;
    border-radius: 12px !important;
    overflow: hidden !important;
}

.tab-nav button.selected {
    color: #f472b6 !important;
    border-bottom: 2px solid #ec4899 !important;
}

.status-message {
    color: #cbd5e1 !important;
    text-align: center !important;
}
"""


def build_episode(pdf_files: List[str]) -> Tuple[str, str, Optional[str], str]:
    """Run the complete PDF-to-podcast pipeline."""

    try:
        # Stop early when no files were uploaded.
        if not pdf_files:
            raise ValueError("Please upload exactly three PDF articles.")

        # Convert Gradio's uploaded file objects into local file paths.
        pdf_paths = [
            uploaded_file.name if hasattr(uploaded_file, "name") else uploaded_file
            for uploaded_file in pdf_files
        ]

        # Require exactly three source articles for this project.
        if len(pdf_paths) != 3:
            raise ValueError("Please upload exactly three PDF articles.")

        # Read the API key without placing it in the source code.
        api_key = os.getenv("OPENAI_API_KEY", "")

        # Check that the API key is available.
        if not api_key:
            raise ValueError("OPENAI_API_KEY is missing from the .env file.")

        # Extract and combine all uploaded PDF articles.
        combined_text = combine_pdf_files(pdf_paths)

        # Ask the LLM to create structured podcast segments from the articles.
        podcast = create_podcast_script(combined_text, api_key)

        # Convert all structured segments into one combined MP3 file.
        audio_path = generate_audio(podcast, api_key)

        # Format the JSON for display in the Gradio text box.
        podcast_json = json.dumps(podcast, indent=2, ensure_ascii=False)

        # Calculate simple episode information for the result summary.
        word_count = sum(
            len(segment["text"].split())
            for segment in podcast["segments"]
        )
        duration_minutes = max(1, round(word_count / 150))

        # Build a polished summary card with the uploaded source filenames.
        source_list = "".join(
            f"<li><strong>{Path(pdf_path).name}</strong></li>"
            for pdf_path in pdf_paths
        )
        summary = (
            f"<h2>✅ {podcast['title']}</h2>"
            f"<p><strong>{word_count} words</strong> · about "
            f"<strong>{duration_minutes} minutes</strong></p>"
            f"<h3>Sources used</h3><ul>{source_list}</ul>"
        )

        # Return the results to the Gradio components.
        return summary, podcast_json, audio_path, "Episode generated successfully."

    except Exception as error:
        # Show a readable error message instead of crashing the app.
        return "", "", None, f"Error: {error}"


# Create the main Gradio application container.
with gr.Blocks(title="AI Apocalypse Podcast Studio", css=custom_css) as app:

    # Add the application title and instructions.
    gr.Markdown(
        "# AI Apocalypse Podcast Studio\n"
        "Upload the three articles to create one podcast episode.",
        elem_classes=["app-header"],
    )

    # Create tabs that match the team's upload-focused interface design.
    with gr.Tabs(elem_classes=["tabs"]):
        with gr.Tab("Upload PDFs"):
            # Create a file uploader that accepts exactly three PDF files.
            pdf_input = gr.File(
                label="Upload your three PDF articles",
                file_types=[".pdf"],
                file_count="multiple",
                type="file",
            )

        with gr.Tab("Paste text"):
            # Explain that PDF upload is the active MVP input method.
            gr.Markdown(
                "Paste-text input is reserved for a future version. "
                "For this MVP, please use the **Upload PDFs** tab."
            )

    # Show the actor design in a compact settings panel.
    with gr.Accordion("Episode settings", open=False, elem_classes=["settings-panel"]):
        gr.Markdown(
            "**Ana** — curious host using `nova`\n\n"
            "**Rui** — expert host using `alloy`\n\n"
            "The episode is generated from exactly three PDF articles."
        )

    # Create the button that starts the processing pipeline.
    create_button = gr.Button(
        "Create podcast episode",
        variant="primary",
        elem_classes=["generate-button"],
    )

    # Create an area for status and error messages.
    status_output = gr.Markdown(elem_classes=["status-message"])

    # Create a polished result summary card.
    summary_output = gr.HTML(elem_classes=["result-panel"])

    # Create an area for the generated podcast script.
    with gr.Accordion("Generated podcast script", open=True, elem_classes=["script-panel"]):
        script_output = gr.Textbox(lines=20)

    # Create an audio player for the generated MP3.
    audio_output = gr.Audio(
        label="Generated podcast audio",
        type="filepath",
    )

    # Connect the button to the build_episode function.
    create_button.click(
        fn=build_episode,
        inputs=pdf_input,
        outputs=[summary_output, script_output, audio_output, status_output],
    )


# Start the interface when this file is run directly.
if __name__ == "__main__":
    # Disable automatic API-schema generation to avoid a Gradio 4 compatibility issue.
    app.launch(show_api=False)


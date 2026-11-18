# AI Apocalypse Podcast Studio

This project creates a short podcast episode from three articles about the risks and realities of an AI apocalypse.

The application pipeline is:

```text
Three PDF articles -> text extraction -> LLM script -> MP3 audio -> Gradio interface
```

The generated podcast uses two actors:

- **Ana**: curious host who asks practical questions and pushes back on hype; voice `nova`.
- **Rui**: expert host who explains evidence and speculation clearly; voice `alloy`.

## Setup

Create and activate the project environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

The application uses `ffmpeg` through `pydub` to combine the speaker segments into one MP3. On macOS, install it with:

```bash
brew install ffmpeg
```

Create a `.env` file in the project root and add your API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Never commit `.env` or share your API key. The file is excluded through `.gitignore`.

## Run the application

```bash
python src/main.py
```

Open the local address shown in the terminal, usually:

```text
http://127.0.0.1:7860
```

Upload the three PDF articles and click **Create podcast episode**. The generated script appears in the interface and the MP3 is saved in the `outputs/` folder.

## Project structure

```text
src/
├── data_processor.py  # Extract and combine PDF text
├── llm_processor.py   # Generate the podcast script
├── tts_generator.py   # Generate the MP3 file
└── main.py            # Gradio application
```

`sources.json` contains citation metadata and links only. The original PDF files are local input files and do not need to be redistributed publicly.

## Sources

The podcast script is based on these three articles. They are used as source material and are not presented as the work of this project’s author.

1. Olsen, S. G., Reinecke-Tellefsen, C. J., & Østergaard, S. D. (2026). “Potentially Harmful Consequences of Artificial Intelligence (AI) Chatbot Use Among Patients With Mental Illness: Early Data From a Large Psychiatric Service System.” *Acta Psychiatrica Scandinavica*, 153, 301–303. https://doi.org/10.1111/acps.70068

2. Bareis, J., Ackerl, C., & Heil, R. (2026). “AI going rogue? An integrative narrative review of the tacit assumptions underlying existential AI-risks.” *AI and Ethics*, 6, 152. https://doi.org/10.1007/s43681-025-00928-w

3. Rogul, A. (2026). “AI & the End of the World: What the Data Say.” Working paper.

## Lab Repository Information

**Track:** Module 4 — Project / PM · **When:** Week 2, Day 4 · **Status:** Optional / Extra

This repository contains everything you need for this lab.

## Files

- [`instructions.md`](./instructions.md) — the lab instructions
- [`rubric.md`](./rubric.md) — how your submission is graded; this is what the AI reviewer checks your PR against

## How to complete this lab

1. **Fork** this repository.
2. Do the work described in `instructions.md`, committing to your fork.
3. Open a **pull request** back into this repository.
4. You'll receive **AI feedback** on your PR based on `rubric.md`. Address any blocking feedback and push updates to the same PR.

## Submission hygiene

- Keep this repository scoped to this lab only — no unrelated projects or personal files.
- Use clear, descriptive filenames.
- Remove secrets, API keys, and tokens before committing.

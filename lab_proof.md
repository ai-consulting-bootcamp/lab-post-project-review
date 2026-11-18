

# Project 1 Stakeholder and Production Readiness Lab

## 1. Project Summary

The AI Apocalypse Podcast Studio was created to make complex discussions about artificial intelligence risks easier to understand through audio. It is intended for students, educators, and listeners who prefer learning through podcasts instead of reading several long articles. The MVP accepts three PDF articles, extracts their text, uses an LLM to create structured podcast segments, and generates a multi-speaker MP3 through a Gradio interface. The current version demonstrates the complete workflow but is still a classroom prototype rather than a production-ready service.

## 2. Stakeholder Analysis

| Stakeholder | Direct / indirect | Role / relationship | Need from the project | Risk if ignored | Influence | Interest |
|---|---|---|---|---|---|---|
| Students and podcast listeners | Direct | Main users of the generated podcast | Clear, accessible, engaging audio | They may stop using the tool if the content is confusing or difficult to access | Low | High |
| Educators and instructors | Direct | Use the project for teaching and evaluation | A reliable demo with understandable outputs | The project may not demonstrate the required learning objectives | High | High |
| Project team members | Direct | Build, test, and present the application | Clear ownership, shared code, and consistent design | Duplicate work, merge confusion, or incompatible versions | High | High |
| API/course account owner | Indirect | Provides or manages the OpenAI API access | Controlled usage and awareness of API consumption | Unexpected costs, quota exhaustion, or disabled access | High | Low |
| Article authors and publishers | Indirect | Created the source material | Proper attribution and responsible reuse | Copyright concerns or inappropriate redistribution of articles | High | Low |
| Application maintainer | Direct | Runs, updates, and fixes the Python project | Clear setup instructions, dependencies, and error messages | The app becomes difficult to run or maintain after handoff | High | High |
| Accessibility-focused users | Direct | May rely on audio rather than long written articles | Understandable audio and readable interface design | Some users may be excluded by poor contrast or unclear controls | Low | High |
| GitHub repository reviewers | Indirect | Inspect and assess the submitted project | Organized files, documentation, and reproducible setup | They may be unable to understand or run the project | High | Medium |


## 3. Demo → Real

### Operations

The current MVP can generate an episode when a user uploads three PDFs, but it does not include production monitoring, automated alerts, backups, or an on-call owner. For a real deployment, we would define who maintains the service, monitor failed requests and API usage, and create a process for responding to incidents.

### Security and Compliance

The API key is stored in an environment variable and excluded from GitHub through `.gitignore`. However, the MVP does not yet include user accounts, access control, audit logs, or a formal review of data residency. A production version would use managed secrets, authentication, access permissions, and documented rules for handling uploaded documents.

### Data Lifecycle

The application temporarily processes uploaded PDF files and sends extracted article text to the LLM. The MVP does not have a formal retention or deletion policy. A production version would define how long uploaded files, extracted text, generated scripts, and audio files are stored and would provide a way to delete them.

### Handoff and Maintenance

The README explains the setup process and the purpose of the main Python files, but the project was mainly designed for its creators. A production handoff would include user documentation, maintenance instructions, dependency updates, troubleshooting steps, and a clear definition of who owns future support.

### Scope and Edge Cases

The MVP assumes that users upload exactly three readable PDFs. It does not yet fully support scanned PDFs, OCR, very large documents, multilingual content, or API outages. A production rollout would add file-size limits, OCR support, language handling, retry behavior, and a clear degraded mode when an external API is unavailable.

## 4. Before / After Scope Revision

### Before

At the beginning, we defined success as creating a working podcast generator that accepts three PDF articles, uses an LLM to create a script, generates audio, and displays the result in Gradio. Our main focus was proving that the end-to-end workflow worked.

### After

We would now define success more broadly: the application should still generate a podcast, but it should also provide clear ownership, secure secret handling, documented API usage, source attribution, predictable error messages, and defined rules for uploaded data. We would keep the first release limited to three readable PDFs, while explicitly treating OCR, multilingual support, monitoring, authentication, and production-scale storage as later phases.

## 5. Workflow Proof

### Input

The application was tested with three PDF articles about AI risks:

- `ACPS-153-301.pdf`
- `AI going rogue.pdf`
- `ssrn-7553718.pdf`

The original PDFs are kept as local test inputs and are not included in the public repository.

### Run

The application was started with:

```bash
source .venv/bin/activate
python src/main.py
```


The Gradio interface was opened at:

http://127.0.0.1:7860

The three PDFs were uploaded through the interface and the **Create podcast episode** button was selected.

### Evidence Produced

The application:

1. Extracted text from the three PDFs.
2. Created structured JSON podcast segments.
3. Assigned the voices `nova` to Ana and `alloy` to Rui.
4. Generated separate audio segments.
5. Combined the segments into one MP3 file.
6. Displayed the result in the Gradio interface.

The final audio output is:

`outputs/ai_apocalypse_episode.mp3`

The repository also contains `sources.json`, which stores citation metadata and DOI links for the source articles.

### Failure or Limitation

The MVP requires exactly three readable PDF files. It does not yet support scanned PDFs without selectable text, OCR, very large documents, or API outages. If the API key is missing, a PDF is invalid, or the LLM returns invalid podcast data, the application displays an error message instead of completing the episode.

## 6. Submission Checklist

- [x] Recognize: The project and intended beneficiaries are clearly described.
- [x] Apply: The stakeholder table contains more than six stakeholders with needs, risks, influence, and interest.
- [x] Integrate: The Demo → Real section covers five production dimensions.
- [x] Verify: The Before / After section shows a clear change in scope and success criteria.
- [x] Evidence: The workflow includes input, run instructions, output, and a limitation.
- [x] Documentation: The project is specific to the AI Apocalypse Podcast Studio.
- [x] Sources: Article metadata and links are documented in `sources.json`.


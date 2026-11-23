## Part 1: Project snapshot
In 3–5 sentences, write:
What problem it was meant to solve
Who the intended user or beneficiary is
What you actually built or delivered (MVP level is fine)

The Podcast Generator was intended for AI-curious professionals and non-experts who encounter conflicting claims about AI risks and need a clear, balanced way to understand the evidence rather than hype or speculation.

We delivered a functioning MVP with a Gradio interface that lets users upload one or more PDF sources, preview their source references locally, and generate a two-host podcast with Ana asking questions and Rui explaining the evidence.

The Python pipeline uses PyPDF to extract source text, GPT-4o to generate a structured podcast script, and GPT-4o-mini-TTS to convert the script segments to speech; long text segments are split at sentence boundaries before being combined into a final MP3.

The MVP also saves the generated transcript, source metadata, and MP3 for reuse, and it replaces the existing saved episode only after script and audio generation have both completed successfully, so a failed new generation leaves the previous saved episode available without making additional API calls.

## Part 2: Stakeholder impact
List at least six stakeholders (mix of direct — daily touch — and indirect — oversight, policy, or downstream).

For each stakeholder, note in a table:

Role / relationship to the project
What they need from the outcome (one line)
Risk if ignored (what goes wrong if you never talk to them or design for them)

| Stakeholder | Type / relationship | What they need | Risk if ignored |
|---|---|---|---|
| Users / audience | Direct | A podcast that meets a real need and explains research clearly | Poor problem-solution fit, low adoption, loss of trust |
| Advertisers | Indirect / future monetization | Access to a relevant audience and brand-safe content | Missed monetization opportunities |
| Marketers | Indirect / future distribution | A clear target audience and compelling product positioning | Ineffective campaigns and high acquisition costs |
| Product manager | Direct | Customer insights, clear objectives, and success criteria | Wrong product priorities, lack of direction or ownership |
| Research paper authors / contributors | Indirect | Accurate representation and proper attribution | Misrepresentation, reputational damage, or copyright concerns |
| Data protection officer | Indirect / oversight | Appropriate data handling, privacy safeguards, and compliance | Privacy breaches, penalties, or reputational damage |

### Stakeholder prioritization

| Stakeholder | Influence (Y-axis) | Interest (X-axis) | Management strategy |
|---|---|---|---|
| Audience / Users | High | High | Manage closely |
| Advertisers | High | Low | Keep satisfied |
| Marketers | Low* | High | Keep informed |
| Product Manager | High | High | Manage closely |
| Researchers / Authors | Low | Low* | Monitor |
| Data Protection Officer | High* | Low* | Keep satisfied |

**Low Interest:** is defined as limited concern about the product’s technical specifications, development decisions, and overall direction. The stakeholder impact also considers implication for production ready product rather than just MVP.

### Part 3: From demo to “real project”
Course demos often assume happy paths, static data, generous API budgets, and you as the maintainer. 
For each dimension, write 2–3 sentences: how your current project handled it (even if “not at all”) and what would change for a production rollout.

Operations
Current MVP: The app shows specific file/PDF errors and a generic message for unexpected failures. Errors are only printed in the terminal; there is no automated monitoring, alerting, incident process, on-call owner, or backup system.
Production rollout: Add structured logging, monitoring, alerts, retries, backups, and a defined support owner.

Security and compliance
Current MVP: The OpenAI key is loaded from an environment variable or local .env file, and .env is listed in .gitignore. The app has no malware scanning, upload security checks, authentication, authorization, or copyright-permission workflow.
Production rollout: Use managed secret storage, scan and validate uploads, restrict access, maintain audit records, and disclose third-party AI processing.

Data lifecycle
Current MVP: The app stores one shared transcript, source-metadata file, and MP3, replacing the previous episode after successful generation. It has no user accounts, per-user access controls, retention policy, or deletion controls.
Production rollout: Store outputs per user or project, define retention periods, provide deletion controls, and remove uploaded PDFs after processing when appropriate.

Scope beyond the demo (edge cases)
Current MVP: The app accepts multiple PDFs and rejects missing, invalid, unreadable, or text-free files, but one unreadable PDF stops the whole batch. It has no OCR, PDF-size limits, topic checks, or confirmation workflow, and it intentionally removes detected bibliography sections.
Production rollout: Process files individually, report failures by filename, add OCR and size/page/token checks, and let users confirm exclusions. Generation should stop only when there is not enough readable and relevant source material.

### Part 4: Revision brief
Time: 10–15 minutes

Write a before / after of one short paragraph each:

### Part 4 — Revision Brief

**Before:** Our goal was to build a working AI-powered Podcast Studio that transformed PDFs into conversational podcasts using an LLM and text-to-speech. Success meant demonstrating the complete workflow through a Gradio interface.

**After:** We would spend more time agreeing on the scope upfront to avoid minor scope creep. We would also assign clear responsibilities to each team member and integrate our work through a shared GitHub repository. Initially, we explored the entire workflow individually to learn how it worked, but this resulted in different approaches that were difficult to combine. Going forward, we would define responsibilities, component interfaces, and integration processes earlier, while expanding success criteria to include security, data handling, and reliable error management.

For production, we would retain the core podcast generation workflow but introduce clearer requirements for security, data handling, and content reliability. Users would specify a podcast topic, receive warnings about unreadable, oversized, or irrelevant PDFs, and confirm before proceeding with incomplete sources. We would also introduce secure API key management, PDF validation, individual access to saved episodes, and automatic deletion of uploaded PDFs after processing. To control storage costs, only the latest episode would be retained per user, with an option to download it

### Checkpoints

Use this order and tick each box in your submission.

- [x] Recognize: You named the project and stated one clear intended beneficiary.
- [x] Apply: Your stakeholder table has at least six rows, each with a need, risk, influence, and interest.
- [x] Integrate: Your “demo → real” section covers at least four dimensions with concrete changes.
- [x] Verify: Your revision brief shows a visible shift in scope or success criteria between “before” and “after.”
- [ ] Stretch (optional): Add one row for a stakeholder who is easy to forget and explain why they matter.

### Definition of done
All requirements filled in this .md file
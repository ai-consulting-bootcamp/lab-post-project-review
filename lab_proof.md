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


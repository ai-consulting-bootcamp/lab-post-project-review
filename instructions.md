# Post-project review — stakeholders & real-world scope

> **How you'll submit this lab**
>
> This repo is your lab. Fork it, do the work described below in your fork, then open a pull
> request back into this repository. An AI reviewer will check your PR against `rubric.md` and
> leave feedback directly on the PR. See `README.md` for the full workflow.

## Overview

You recently shipped or wrapped substantial work on a bootcamp project—for **Week 2**, use your **Project 1** or **mini-project** work from Day 1 of this week, or another assignment you completed meaningfully. In this lab you **step back**: who does that work actually affect, and what would have to change to treat it as a **client-ready, production-style** engagement instead of a classroom demo?


**Estimated time:** 60–90 minutes

## Learning objectives

By the end of this lab, you will be able to:

- **Identify** direct and indirect stakeholders for a project you worked on and explain how the work affects them.
- **Map** simple interest and influence for each stakeholder and prioritize who needs attention first.
- **Describe** concrete gaps between a demo or coursework scope and a “real” deployment (operations, security, data, cost, handoff).
- **Draft** a short revision to scope or framing that would make the project more generalizable or client-ready.

We will consider as **out of scope for this lab:** vendor selection, detailed cost models, legal contracts, or full risk registers (those belong in the classical PM lesson and the scoping lab).

## Instructions

### Part 1: Project snapshot

**Time:** 10 minutes

1. In **3–5 sentences**, write:
   - What problem it was meant to solve
   - Who the intended user or beneficiary is
   - What you actually built or delivered (MVP level is fine)

---

### Part 2: Stakeholder impact

**Time:** 25–35 minutes

A **stakeholder** is anyone who can affect, or be affected by, the project (users, sponsors, IT, legal, support, finance, future you, etc.).

1. List **at least six** stakeholders (mix of **direct** — daily touch — and **indirect** — oversight, policy, or downstream).
2. For **each** stakeholder, note in a table:
   - **Role / relationship** to the project
   - **What they need** from the outcome (one line)
   - **Risk if ignored** (what goes wrong if you never talk to them or design for them)

3. Add a **simple influence / interest** label per row (High or Low for each). You do not need the full quadrant engagement playbook from the scoping lab—just enough to see who is “loud and powerful” vs “quiet but critical.”

**Deliverable:** Stakeholder table (minimum six rows) with needs and risks.

---

### Part 3: From demo to “real project”

**Time:** 20–30 minutes

Course demos often assume happy paths, static data, generous API budgets, and you as the maintainer. A **real** client project usually must account for more of the following:

- **Operations:** monitoring, incident response, backups, who owns on-call
- **Security & compliance:** access control, secrets handling, data residency, audit expectations
- **Data lifecycle:** retention, deletion, PII, training data vs production data
- **Handoff:** documentation, training for client staff, definition of “done” for support
- **Scope beyond the demo:** edge cases, accessibility, multilingual, degraded modes when an API fails

1. Pick **at least four** dimensions from the list above (you may add one of your own).
2. For each dimension, write **2–3 sentences**: how your **current** project handled it (even if “not at all”) and what would **change** for a production rollout.

**Deliverable:** “Demo → real” section with four (or more) dimensions addressed.

---

### Part 4: Revision brief

**Time:** 10–15 minutes

Write a **before / after** of **one short paragraph each**:

- **Before:** How you would have described scope or success at the start of the project.
- **After:** How you would reframe objectives, boundaries, or success criteria now that you have thought about stakeholders and production reality.

Keep it honest (e.g. “we would narrow MVP” or “we would add a security review gate”) rather than generic.

**Deliverable:** Before/after revision brief.

---

##  Checkpoints

Use this order and tick each box in your submission (or paste the checklist with `[x]`).

- [ ] **Recognize:** You named the project and stated one clear intended beneficiary.
- [ ] **Apply:** Your stakeholder table has ≥6 rows, each with need + risk + influence/interest.
- [ ] **Integrate:** Your “demo → real” section covers ≥4 distinct dimensions with concrete “what would change” language (not only buzzwords).
- [ ] **Verify:** Your revision brief shows a visible shift in scope or success criteria between “before” and “after.”
- [ ] **Stretch (optional):** Add one row for a stakeholder who is easy to forget (e.g. finance, internal audit, end user in a stressed scenario) and explain why they matter.

## Definition of done

- One link submitted containing all the elements in the checklist.
- Writing is specific to **your** project (no generic filler that could apply to any team).

## Submission

### Submission hygiene

- **Filenames:** Use clear, descriptive names (avoid vague names such as `lab.ipynb`, `final_v2.py`, or `untitled.md`).
- **Scope:** Your **GitHub** repository must contain **only materials for this lab**—no unrelated projects, dumps, or personal files.
- **README:** Include a `README.md` that briefly explains what each main file or folder is for (a short map of your file structure).

**GitHub only:** Submit the URL to a **GitHub repository** that contains everything for this lab (Markdown, code, exports, images, decks). Do **not** submit a standalone Google Doc, Notion page, or cloud-only link as your primary deliverable—put sources or exports (for example `.md`, `.pdf`, `.pptx`, screenshots) **in the repository**.

Submit the URL to your **GitHub** repository in the deliverable field for this lab.

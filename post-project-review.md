# Post-project Review: Lesson Recapper

## Part 1: Project snapshot

Our project, Lesson Recapper, aimed to help bootcamp students review their notes through audio and better understand class topics. It was designed for students who want to study when reading is not convenient or who prefer listening to explanations. We built a prototype that turns notes into an AI-generated educational script and an audio podcast, which users can play and download through a Gradio interface. The tool could later be adapted for master’s and PhD students, but we have not yet evaluated whether it improves understanding or preserves enough detail for advanced academic content.

## Part 2: Stakeholder impact

Our development team built the prototype for students, and our teacher reviewed our work and gave positive feedback. This was encouraging, but further testing with students would be needed to evaluate its learning benefits.

The final three stakeholders represent roles we would involve in a real deployment. Influence and interest are estimated for a bootcamp pilot.

| Stakeholder | Role / relationship | What they need | Risk if ignored | Influence | Interest |
|---|---|---|---|---|---|
| Bootcamp students — direct | Intended users who review class notes through audio. | Clear, accurate explanations and audio that is easy to access. | Incorrect or incomplete explanations could confuse them. | Low | High |
| Teacher — direct | Reviewed the prototype and provided positive feedback. | A working tool that supports learning and explains topics correctly. | Podcasts could miss key concepts or include misleading explanations. | High | High |
| Development team — direct | Built and tested the application. | Clear responsibilities, understandable code, and reliable connections between modules. | Changes could break the application or make maintenance difficult. | High | High |
| Academic coordinator — indirect, proposed | Would approve the pilot and define its educational scope. | Evidence that the tool is useful and clear limits on its use. | The team could expand the tool without meeting the bootcamp’s priorities. | High | High |
| IT support team — direct, proposed | Would help users and maintain the deployed application. | Setup instructions, useful error logs, and clear support responsibilities. | Students could lose access, with nobody responsible for fixing problems. | High | High |
| Privacy lead — indirect, proposed | Would review how uploaded notes and generated files are handled. | Clear information about data access, external processing, storage, and deletion. | Personal or confidential information could be shared or kept without appropriate controls. | High | Low |

### Who needs attention first?

Before a pilot, we would agree on scope with the academic coordinator and teacher, and test the tool with students. Although students have low formal influence, their feedback is essential. We would also involve IT support and the privacy lead before using real student data.

The privacy lead’s low interest means limited day-to-day involvement, not that privacy is unimportant.

## Part 3: From demo to real project

The confirmed version ran locally through Gradio. We used GitHub to collaborate and merge the code; this did not mean that the application was publicly hosted. The following improvements are proposals, not completed features.

### 1. Operations

For the demo, we ran the application locally after merging our code on GitHub, so availability depended on the computer running it. For a real deployment, we would need hosted infrastructure, availability monitoring, and a named person responsible for incidents and maintenance.

### 2. Security and access

The confirmed version used a local URL; we have not verified user authentication or access controls. Before a student pilot, we would review API key handling, keep secrets outside the repository, and restrict access to approved users.

### 3. Data lifecycle

The application processes study materials and generates scripts and audio files, but we have not confirmed retention or deletion rules. For a real deployment, we would explain what information is sent to the AI provider, define how long files are kept, and provide a way to delete them. We would initially limit the pilot to notes without personal or confidential information and with permission for processing.

### 4. Handoff and support

Our team developed the prototype, and our teacher reviewed it positively, but we have not confirmed a formal handoff process. For a client pilot, we would document setup, configuration, common errors, and known limitations. We would also name a support owner and define which problems the team would handle after delivery.

### 5. Reliability and educational quality

The prototype generates educational scripts and audio, but positive teacher feedback does not establish reliability across different inputs or improved student understanding. Before a pilot, we would test empty inputs, long notes, and API failures, and show clear messages when generation fails. A teacher would review sample podcasts for accuracy, and students would evaluate whether they help with revision.

## Part 4: Revision brief

### Before

At the start, our goal was to build a working prototype that turned study notes into an educational podcast. Success meant connecting the modules, generating a script and audio, and allowing users to play and download the podcast through Gradio. Our main focus was completing the classroom demonstration.

### After

We would now limit the next stage to a small pilot with bootcamp students, using notes that contain no personal or confidential information and that we have permission to process. Before opening access, we would review security, define file deletion rules, name a support owner, and test long inputs and API failures. Success would include reliable podcast generation, teacher review of sample explanations, and student feedback on usefulness and clarity; we would evaluate learning benefits rather than assume them. Support for master’s and PhD students would remain outside this initial pilot.

## Submission checklist

- [x] Recognize: Named the project and identified bootcamp students as the main intended users.
- [x] Apply: Listed six stakeholders with needs, risks, influence, and interest.
- [x] Integrate: Addressed five dimensions with concrete changes for a real deployment.
- [x] Verify: Changed the scope from a classroom demo to a controlled student pilot.

These checks refer to the completed review. The proposed production improvements have not yet been implemented.
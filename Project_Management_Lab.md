# **Project Management Lab: (Post-project review — stakeholders & real-world scope)** 

# **Part 1: Project snapshot** 

# **Project Name: Lesson Recapper – AI-Powered Audio Summarization Application** 

Our team designed and developed Lesson Recapper, an AI-powered web application that addresses the difficulty of reviewing lengthy meeting and lecture transcripts, particularly for people who miss sessions or have limited time to read through the material. The application is intended for students, professionals, and other learners who want to catch up on important information or reinforce their understanding while on the go. Users upload a transcript, which is processed using an LLM to extract five key points and transform them into a concise, podcast-style summary. The application then generates approximately five minutes of audio, allowing users to review essential information while commuting, walking, or performing other daily activities. 

# **Part 2: Stakeholder Impact** 

Lesson Recapper application identified the stakeholders who would influence or be affected by Lesson Recapper if it were introduced into a real educational or professional environment. 

# **Stakeholder analysis table** 

Proposed stakeholders for a real-world deployment 

|**Stakeholder / Role &**<br>**Relationship**|**What they need**|**Risk if ignored**|**Influen**|**lce Interest**|
|---|---|---|---|---|
|1. Students and learners<br>(Direct) – Primary users of<br>the application|Accurate, concise, and<br>accessible audio<br>summaries for learning<br>and revision|Poor user experience, low<br>adoption, or<br>misunderstanding of<br>important concepts|Low|High|
|2. Professionals and<br>meeting participants<br>(Direct) – Users reviewing<br>missed meetings|Reliable summaries<br>capturing key<br>discussions and<br>decisions|Important information or<br>decisions may be missed<br>or misinterpreted|Low|High|
|3. Teachers and meeting<br>organizers (Direct) –<br>Providers and reviewers of<br>source content|Summaries that<br>accurately reflect the<br>original lessons or<br>discussions|Critical information may be<br>omitted or incorrectly<br>summarized|i i<br>High|High|
|4. Development team<br>(Direct) – Builds and<br>maintains the application|Clear requirements,<br>reliable APIs, and well-<br>defined technical<br>responsibilities|Integration failures,<br>technical errors, and<br>delayed delivery|High|High|



|5. Project sponsor /<br>training manager<br>(Indirect) – Approves and<br>funds implementation|Evidence of user value,<br>reliability, and cost-<br>effectiveness|Lack of funding,<br>management support, or<br>project continuation|High|High|
|---|---|---|---|---|
|6. IT and technical support<br>(Indirect) – Responsible<br>for system operations|<br>Stable infrastructure,<br>documentation, and<br>troubleshooting<br>procedures|System downtime,<br>unresolved errors, and<br>increased maintenance<br>effort|High|Low|



# **Part 3: From Demo to “Real Project”** 

# **1. Operations and Reliability** 

**Current Demo:** Our team developed a web application that converts uploaded transcripts into approximately five-minute audio summaries. During development, we experienced dependency issues, environment configuration errors, and challenges integrating different Python modules, which we resolved through troubleshooting and testing. 

**Production Rollout:** For real-world deployment, we would introduce automated monitoring, structured error handling, and standardized deployment procedures to ensure the application operates reliably. We would also assign responsibility for technical support, incident resolution, and service recovery when transcript processing or audio generation fails. 

# **2. Security and Compliance** 

**Current Demo:** Our main focus was developing the application's core functionality, including transcript processing, LLM summarization, and audio generation. 

**Production Rollout:** We would implement secure user authentication, access controls, and protected API credentials to prevent unauthorized access. We would also establish appropriate data protection measures, including GDPR requirements where applicable, particularly because uploaded lecture and meeting transcripts may contain personal or confidential information. 

# **3. Data Lifecycle Management** 

**Current Demo:** Our application processed uploaded transcripts to extract five important points and generate audio recaps. However, the presentation did not specify how long uploaded transcripts, generated summaries, or audio files were retained or how they were deleted. 

**Production Rollout:** We would establish clear policies for data storage, retention, and deletion, including appropriate handling of personal information. Users would be provided with suitable options to manage their uploaded transcripts and generated podcasts, while the organization would define who is authorized to access stored content. 

# **4. Documentation, Training, and Handoff** 

**Current Demo:** Our team collaborated using Git and GitHub. We encountered merge conflicts and workflow mistakes, which highlighted the importance of clear development responsibilities and proper version control. 

**Production Rollout:** We would prepare technical documentation, installation instructions, user guides, and training materials for client staff. A structured handover would also define maintenance responsibilities, troubleshooting procedures, and acceptance criteria so that the application could be supported without relying on the original development team. 

# **5. Scope Beyond the Demo** 

**Current Demo:** Lesson Recapper focused on its core functionality: uploading a transcript, identifying five key points, and generating an approximately five-minute audio recap. The presentation did not demonstrate how the application handled unusual inputs, unsupported languages, or external service failures. 

**Production Rollout:** We would extend testing to include lengthy or incomplete transcripts, different languages, and failures in LLM or audio-generation services. We would also introduce accessible text summaries, informative error messages, and alternative ways to access the content when audio generation is unavailable. 

# **Part 4: Revision Brief – Before vs. After** 

# **Before: Original Project Scope** 

Our initial goal was to develop Lesson Recapper, a web application that transforms lengthy meeting and lecture transcripts into approximately five-minute audio summaries highlighting five key points. We focused on building a functional application where users could upload transcripts, generate summaries using an LLM, and listen to the resulting podcast-style audio. At this stage, we considered the project successful if the application could complete the process and produce a playable audio recap. 

# **After: Revised Project Scope** 

After considering stakeholders' needs and real-world deployment requirements, we would shift our focus from simply generating audio recaps to delivering a reliable, secure, and accurate learning and information-recap tool. We would initially limit the rollout to one training program, introduce instructor reviews to verify the accuracy of the five key points, and require a security and data protection review before processing real user transcripts. Success would be measured by summary accuracy, audio quality, successful podcast generation, and user satisfaction, with clear acceptance criteria and support responsibilities established before expanding the application to more users. 

# **Checkpoints** 

Use this order and tick each box in your submission (or paste the checklist with [x]). 

X Recognize: You named the project and stated one clear intended beneficiary. 

X  Apply: Your stakeholder table has ≥6 rows, each with need + risk + influence/interest. 

X Integrate: Your “demo → real” section covers ≥4 distinct dimensions with concrete “what would change” language (not only buzzwords). 

X Verify: Your revision brief shows a visible shift in scope or success criteria between “before” and “after.” 

Stretch (optional): Add one row for a stakeholder who is easy to forget (e.g. finance, internal audit, end user in a stressed scenario) and explain why they matter. 

# **Definition of done** 

- One link submitted containing all the elements in the checklist. 

- Writing is specific to your project (no generic filler that could apply to any team). 


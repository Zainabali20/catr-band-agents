# CATR — Career Advisory Team with Band

CATR is a Pakistan-first, globally adaptable multi-agent career guidance system for students, parents, schools, and education organizations.

It uses Band as the core collaboration layer where specialized agents assess a student profile, map suitable career paths, create an academic roadmap, review the plan, and approve the final recommendation.

Live Demo: https://catr-band-agents.netlify.app/

---

## Copyright and Usage Notice

© 2026 Zainab Ali. All rights reserved.

This repository is shared as a hackathon demonstration of the CATR multi-agent workflow. The source code, written content, workflow design, product presentation, and project concept are not licensed for commercial reuse, redistribution, copying, or derivative product development without written permission from the author.

This public repository is intended for judging, demonstration, and portfolio review only.

---

## Problem

Students in many countries, especially in emerging markets, often make academic and career decisions without structured guidance.

They may choose subjects, degrees, universities, or career paths without clearly understanding:

* which subjects match their strengths and interests
* which academic tracks lead to which careers
* which degrees and entry exams are required
* which skills they should start building early
* what career outcomes and salary paths may look like
* how parents, teachers, and institutions can support better planning

CATR is Pakistan-first because the demo focuses on Pakistan-specific subject choices, university pathways, and career planning. However, the same workflow can be adapted for other countries by changing local education rules, admission data, university pathways, and labor market information.

---

## Solution

CATR turns career guidance into a structured multi-agent decision workflow.

Instead of one chatbot giving generic advice, CATR uses four specialized Band agents:

1. Assessment Agent
   Extracts the student profile from raw input.

2. Career Mapper Agent
   Maps interests, strengths, and goals to suitable career tracks.

3. Roadmap Planner Agent
   Creates a Pakistan-specific academic and career roadmap.

4. Review & Decision Agent
   Reviews the roadmap for quality, realism, risk, clarity, and responsible guidance before approving the final output.

---

## Band Multi-Agent Workflow

CATR uses Band as the actual collaboration layer.

The agents do not run as one hidden prompt. They communicate through visible Band handoffs and pass structured context from one stage to the next.

Workflow:

```text
Assessment Agent
→ Career Mapper Agent
→ Roadmap Planner Agent
→ Review & Decision Agent
→ Final Reviewed Roadmap
```

Handoff markers used in the Band workflow:

```text
[HANDOFF:ASSESSMENT_TO_MAPPER]
[HANDOFF:MAPPER_TO_PLANNER]
[HANDOFF:PLANNER_TO_REVIEWER]
[FINAL REVIEWED CATR ROADMAP]
```

This demonstrates planning, execution, review, decision-making, and task handoff through Band.

---

## Why This Fits the Hackathon

The challenge asks for a cross-framework multi-agent system where at least three agents collaborate through Band across planning, execution, review, decision-making, or task handoff.

CATR demonstrates:

* 4 collaborating Band remote agents
* structured context sharing
* visible agent-to-agent handoffs
* planning through the Roadmap Planner Agent
* review and quality control through the Review & Decision Agent
* final decision-making before the roadmap is delivered
* a real education and career planning use case

CATR is not a simple chatbot. It is a coordinated multi-agent decision workflow.

---

## React Frontend

The project includes a React frontend deployed on Netlify.

Live Demo:

```text
https://catr-band-agents.netlify.app/
```

The frontend presents the product experience:

* CATR overview
* sample student profile
* four-agent workflow
* Band handoff flow
* final reviewed roadmap
* quality review scorecard
* next 7 days action plan

The React frontend is for presentation and product experience.
The actual multi-agent collaboration happens live inside Band.

---

## Tech Stack

* Band Remote Agents
* Band SDK
* Python
* LangGraph Adapter
* Featherless API
* Qwen model
* React
* Vite
* Netlify
* GitHub

---

## Project Structure

```text
band_remote_agents/
│
├── agent_runner.py          # Runs the 4 Band remote agents
├── test_provider.py         # Tests Featherless provider connection
├── README.md                # Main project documentation
├── netlify.toml             # Netlify deployment settings
├── pyproject.toml
├── uv.lock
├── .gitignore
│
├── frontend/                # React demo frontend
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── index.css
│   ├── package.json
│   └── vite.config.js
│
├── .env                     # Local only, not pushed
└── agent_config.yaml         # Local only, not pushed
```

---

## Example Student Input

```text
Student profile:
Name: Hasan
Age: 14
Country: Pakistan
Interests: computers, maths, business
Strong subjects: mathematics, computer science
Weak subjects: chemistry
Dream job: software engineer and entrepreneur
Parent expectation: stable career with good income
```

---

## Example Final Output

The Review & Decision Agent produces:

* quality review scorecard
* final decision
* approved roadmap
* academic pathway
* skill roadmap
* next 7 days action plan
* disclaimer

Example scorecard:

```text
Quality Review Scorecard:
- Student-career fit: 9/10
- Pakistan relevance: 9/10
- Academic pathway clarity: 9/10
- Parent/student readability: 9/10
- Risk level: Low
- Final decision: APPROVED
```

---

## Running the Band Agents Locally

Create a local `.env` file:

```text
BAND_REST_URL=https://app.band.ai/
BAND_WS_URL=wss://app.band.ai/api/v1/socket/websocket
FEATHERLESS_API_KEY=your_featherless_key
FEATHERLESS_BASE_URL=https://api.featherless.ai/v1
FEATHERLESS_MODEL=your_model_name
```

Create a local `agent_config.yaml` file:

```yaml
assessment:
  agent_id: "your_assessment_agent_uuid"
  api_key: "your_assessment_band_key"

mapper:
  agent_id: "your_mapper_agent_uuid"
  api_key: "your_mapper_band_key"

planner:
  agent_id: "your_planner_agent_uuid"
  api_key: "your_planner_band_key"

reviewer:
  agent_id: "your_reviewer_agent_uuid"
  api_key: "your_reviewer_band_key"
```

Run:

```bash
uv run python agent_runner.py
```

---

## Running the React Frontend Locally

```bash
cd frontend
npm install
npm run dev
```

---

## Deployment

The React frontend is deployed on Netlify.

Netlify settings:

```text
Base directory: frontend
Build command: npm run build
Publish directory: dist
```

---

## Security

The following files are excluded from GitHub:

```text
.env
agent_config.yaml
.venv/
```

API keys, Band agent keys, and provider keys should never be pushed to GitHub.

---

## Future Work

Planned future improvements include:

* Schedule Planner Agent for weekly study plans
* calendar-based study reminders
* parent and teacher review dashboard
* student progress tracking
* school and government education-sector dashboard
* localized university admission data
* PDF export of final career roadmaps
* expansion beyond Pakistan into other emerging education markets

---

## Demo Summary

CATR shows how Band can coordinate a real multi-agent decision workflow:

```text
assessment → mapping → planning → review → final decision
```

The system is designed as a Pakistan-first, globally adaptable career guidance workflow for students, parents, schools, and education organizations.

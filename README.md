# CATR — Career Advisory Team for Pakistani Students

CATR is a Band-powered multi-agent career guidance system designed for Pakistani students and parents who need clearer academic and career planning before choosing subjects, degrees, and future pathways.

It demonstrates a real multi-agent workflow where specialized agents collaborate through Band by sharing structured context, handing off tasks, reviewing outputs, and making a final decision.

---

## Problem

Many students in Pakistan choose academic tracks without fully understanding:

* which subjects fit their interests and strengths
* which degrees lead to their dream careers
* which entry exams they need to prepare for
* which universities are relevant
* which technical and soft skills they should build early
* what the career and salary path may look like

This often leads to confusion, late career switching, weak planning, and pressure on both students and parents.

---

## Solution

CATR uses a collaborative agent workflow through Band.

Instead of one chatbot giving generic advice, CATR uses four specialized agents:

1. **Assessment Agent**

   * Reads the raw student profile.
   * Extracts structured student information.
   * Hands off the profile to the Career Mapper Agent.

2. **Career Mapper Agent**

   * Reviews student interests, strengths, weak areas, and goals.
   * Recommends a primary and alternative career track.
   * Hands off the mapping to the Roadmap Planner Agent.

3. **Roadmap Planner Agent**

   * Builds a Pakistan-specific academic and career roadmap.
   * Includes subject choices, intermediate pathway, degree options, entry exams, universities, skills, certifications, and next steps.
   * Hands off the draft roadmap to the Review & Decision Agent.

4. **Review & Decision Agent**

   * Reviews the roadmap for quality, realism, Pakistan relevance, age-appropriate advice, parent/student readability, and responsible salary guidance.
   * Produces a final reviewed roadmap with a quality scorecard and final decision.

---

## Band Multi-Agent Workflow

CATR uses Band as the actual collaboration layer.

The agents do not work as one hidden prompt. They communicate visibly through Band handoffs:

```text
Assessment Agent
→ Career Mapper Agent
→ Roadmap Planner Agent
→ Review & Decision Agent
→ Final Reviewed Roadmap
```

Example handoff markers:

```text
[HANDOFF:ASSESSMENT_TO_MAPPER]
[HANDOFF:MAPPER_TO_PLANNER]
[HANDOFF:PLANNER_TO_REVIEWER]
[FINAL REVIEWED CATR ROADMAP]
```

This makes the collaboration visible, structured, and central to the workflow.

---

## Why This Fits the Hackathon

The challenge asks for a cross-framework multi-agent system where at least three agents collaborate through Band across planning, execution, review, decision-making, or handoff.

CATR demonstrates:

* **Minimum 3 agents:** CATR uses 4 agents.
* **Meaningful Band usage:** Agents hand off structured context through Band.
* **Planning:** Roadmap Planner Agent creates the academic and career plan.
* **Execution:** Assessment and Career Mapper Agents process the student profile.
* **Review:** Review & Decision Agent checks roadmap quality.
* **Decision-making:** Final agent approves or flags the roadmap before delivery.
* **Real-world use case:** Career guidance for students and parents in Pakistan.

---

## React Frontend

The project also includes a React frontend that presents the product experience.

The frontend shows:

* CATR overview
* sample student profile
* four-agent workflow
* Band handoff flow
* final reviewed roadmap
* quality review scorecard
* next 7 days action plan

The React frontend is for presentation and product demo polish.

The live multi-agent collaboration happens inside Band.

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
* dotenv

---

## Project Structure

```text
band_remote_agents/
│
├── agent_runner.py          # Runs the 4 Band remote agents
├── test_provider.py         # Tests Featherless provider connection
├── README.md                # Main project documentation
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
├── .env                    # Local only, not pushed
└── agent_config.yaml        # Local only, not pushed
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

The final Review & Decision Agent produces:

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

## Running the Band Agents

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

Install dependencies and run:

```bash
uv run python agent_runner.py
```

---

## Running the React Frontend

```bash
cd frontend
npm install
npm run dev
```

Open the local Vite URL shown in the terminal.

---

## Security

The following files are excluded from GitHub:

```text
.env
agent_config.yaml
.venv/
```

API keys and Band agent keys should never be pushed to GitHub.

---

## Future Work

Possible future improvements:

* Schedule Planner Agent to convert the roadmap into weekly study plans.
* Calendar reminder integration.
* Parent/teacher review dashboard.
* University admission data integration.
* Student progress tracking.
* PDF export of the final roadmap.

---

## Demo Summary

CATR shows how Band can be used as the core collaboration layer for a real decision workflow.

The project combines:

```text
assessment → mapping → planning → review → final decision
```

This makes the system more than a chatbot. It is a structured multi-agent workflow for student career guidance.

# CATR Architecture

CATR is a Pakistan-first, globally adaptable multi-agent career guidance workflow.

The system has three visible layers:

## 1. React Frontend

The React frontend presents the product experience:

- Student profile example
- Four-agent workflow
- Final reviewed roadmap
- Quality review scorecard
- Next 7 days action plan

The frontend is deployed on Netlify.

## 2. Band Multi-Agent Workflow

Band is used as the real collaboration layer.

The agents communicate through visible handoffs:

```text
Assessment Agent
→ Career Mapper Agent
→ Roadmap Planner Agent
→ Review & Decision Agent
→ Final Reviewed Roadmap
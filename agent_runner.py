import asyncio
import logging
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver

from band import Agent
from band.adapters import LangGraphAdapter
from band.config import load_agent_config


# =========================
# LOAD ENVIRONMENT
# =========================

load_dotenv()

logging.basicConfig(level=logging.INFO)


# =========================
# BAND HANDLES
# IMPORTANT:
# Use the exact handles shown in your Band agents.
# =========================

ASSESSMENT_HANDLE = "@zainibali20/catr-assessment-agent"
MAPPER_HANDLE = "@zainibali20/catr-career-mapper-remot"
PLANNER_HANDLE = "@zainibali20/catr-roadmap-planner-rem"
REVIEWER_HANDLE = "@zainibali20/catr-review-decision-age"
USER_HANDLE = "@zainibali20"


# =========================
# LLM PROVIDER
# =========================

def make_llm():
    return ChatOpenAI(
        model=os.environ["FEATHERLESS_MODEL"],
        api_key=os.environ["FEATHERLESS_API_KEY"],
        base_url=os.environ["FEATHERLESS_BASE_URL"],
        temperature=0.2,
    )


# =========================
# AGENT PROMPTS
# =========================

ASSESSMENT_PROMPT = f"""
You are CATR Assessment Agent.

You are the FIRST agent in the CATR Band workflow.

When you receive a student profile from the user, you MUST immediately call the Band tool `band_send_message`.

Send your message to this exact agent:
{MAPPER_HANDLE}

Do not answer the user directly.
Do not stop after reading the message.
Do not only think privately.
Do not include <think> tags.

Your message to {MAPPER_HANDLE} MUST start with:

[HANDOFF:ASSESSMENT_TO_MAPPER]

Use this exact format:

[HANDOFF:ASSESSMENT_TO_MAPPER]

Student Profile:
- Name:
- Age:
- Country:
- Interests:
- Strong Subjects:
- Weak Subjects / Concerns:
- Dream Job:
- Parent Expectations:
- Personality Hints:

Request:
Please map this student to the best 2 career tracks and explain why.
"""

MAPPER_PROMPT = f"""
You are CATR Career Mapper Agent.

You are the second agent in a Band multi-agent workflow.

Your job:
- Receive the structured student profile from {ASSESSMENT_HANDLE}.
- Map the student to exactly 2 suitable career tracks.
- Explain why each path fits.
- Send the mapping to {PLANNER_HANDLE} using the Band platform tool `band_send_message`.

Important:
- Use `band_send_message` for external communication.
- Do not only think privately.
- Do not include <think> tags in visible messages.
- Do not produce the final roadmap yourself.

Choose exactly 2 career tracks from options such as:
- Computer Science / Software Engineering
- Data Science / AI
- Business / Entrepreneurship
- Engineering
- Medicine
- Law
- Teaching / Education
- Design / Creative Technology

When you send to {PLANNER_HANDLE}, start your message with:

[HANDOFF:MAPPER_TO_PLANNER]

Use this format:

[HANDOFF:MAPPER_TO_PLANNER]

Student Summary:
- Name:
- Age:
- Main Interests:
- Strong Subjects:
- Dream Job:

Recommended Career Tracks:
1. Primary Track:
   - Why it fits:
   - Key risks:
   - Skills needed:

2. Alternative Track:
   - Why it fits:
   - Key risks:
   - Skills needed:

Request:
Please create a Pakistan-specific academic and career roadmap.
"""


PLANNER_PROMPT = f"""
You are CATR Roadmap Planner Agent.

You are the third agent in a Band multi-agent workflow.

Your job:
- Receive the student profile and career mapping from {MAPPER_HANDLE}.
- Create a practical Pakistan-specific academic and career roadmap.
- Send the completed roadmap to {REVIEWER_HANDLE} for final review and approval using the Band platform tool `band_send_message`.

Important:
- Use `band_send_message` for external communication.
- Do not only think privately.
- Do not include <think> tags in visible messages.
- Do not send the final roadmap directly to the user.
- The Review & Decision Agent will approve it and send the final version to the user.

Create a professional roadmap with:

Student Summary:
- Name
- Age
- Interests
- Strong Subjects
- Dream Job

Recommended Career Path:
- Primary Path
- Alternative Path

Why This Fits:
- Explain simply for both student and parents.

Academic Roadmap:
1. Matric subject focus
2. Intermediate pathway
3. Degree options
4. Entry exams in Pakistan
5. Recommended universities in Pakistan

Skill Roadmap:
- Skills to start this year
- Beginner certifications
- Portfolio/project ideas

Career Outlook:
- Entry salary range in PKR
- Mid-level salary range in PKR
- Possible private/public sector paths

Next 7 Days Action Plan:
Day 1:
Day 2:
Day 3:
Day 4:
Day 5:
Day 6:
Day 7:

When you send to {REVIEWER_HANDLE}, start your message with:

[HANDOFF:PLANNER_TO_REVIEWER]

Use this format:

[HANDOFF:PLANNER_TO_REVIEWER]

Draft Roadmap:
- Include the full roadmap here.

Review Request:
Please review this roadmap for quality, realism, Pakistan relevance, age-appropriate guidance, and final approval.
"""


REVIEWER_PROMPT = f"""
You are CATR Review & Decision Agent.

You are the final quality-control and decision-making agent in the CATR Band multi-agent workflow.

Your job:
- Receive the completed roadmap from {PLANNER_HANDLE}.
- Review it before it reaches the user.
- Approve it, flag risks, and produce the final reviewed roadmap.
- Send the final approved roadmap to {USER_HANDLE} using the Band platform tool `band_send_message`.

Important:
- Use `band_send_message` for external communication.
- Do not only think privately.
- Do not include <think> tags in visible messages.

Review the roadmap for:
1. Student-career fit
2. Pakistan-specific relevance
3. Age-appropriate advice
4. Academic pathway clarity
5. Degree and entry exam realism
6. Parent/student readability
7. Responsible salary guidance
8. Disclaimer and safety

Start your final message with:

[FINAL REVIEWED CATR ROADMAP]

Use this format:

[FINAL REVIEWED CATR ROADMAP]

Quality Review Scorecard:
- Student-career fit: /10
- Pakistan relevance: /10
- Academic pathway clarity: /10
- Parent/student readability: /10
- Risk level: Low / Medium / High
- Final decision: APPROVED or NEEDS REVISION

Final Recommendation:
- Give one clear recommendation.

Approved Roadmap:
- Present the improved final roadmap clearly.

Next 7 Days Action Plan:
- Day 1:
- Day 2:
- Day 3:
- Day 4:
- Day 5:
- Day 6:
- Day 7:

Disclaimer:
This is AI-assisted career guidance and should be validated with parents, teachers, counselors, and official university/admission sources.
"""


# =========================
# AGENT CREATION
# =========================

def create_agent(config_name: str, custom_prompt: str):
    agent_id, api_key = load_agent_config(config_name)

    adapter = LangGraphAdapter(
        llm=make_llm(),
        checkpointer=InMemorySaver(),
        custom_section=custom_prompt,
    )

    agent = Agent.create(
        adapter=adapter,
        agent_id=agent_id,
        api_key=api_key,
        ws_url=os.environ["BAND_WS_URL"],
        rest_url=os.environ["BAND_REST_URL"],
    )

    return agent


async def run_agent(config_name: str, custom_prompt: str):
    agent = create_agent(config_name, custom_prompt)
    await agent.run()


# =========================
# MAIN
# =========================

async def main():
    required_env_vars = [
        "BAND_REST_URL",
        "BAND_WS_URL",
        "FEATHERLESS_API_KEY",
        "FEATHERLESS_BASE_URL",
        "FEATHERLESS_MODEL",
    ]

    missing = [var for var in required_env_vars if not os.environ.get(var)]

    if missing:
        raise RuntimeError(f"Missing environment variables: {missing}")

    await asyncio.gather(
        run_agent("assessment", ASSESSMENT_PROMPT),
        run_agent("mapper", MAPPER_PROMPT),
        run_agent("planner", PLANNER_PROMPT),
        run_agent("reviewer", REVIEWER_PROMPT),
    )


if __name__ == "__main__":
    asyncio.run(main())
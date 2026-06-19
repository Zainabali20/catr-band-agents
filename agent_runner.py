import asyncio
import logging
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver

from band import Agent
from band.adapters import LangGraphAdapter
from band.config import load_agent_config


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("catr-agents")

ASSESSMENT_HANDLE = "@zainibali20/catr-assessment-agent"
MAPPER_HANDLE = "@zainibali20/catr-career-mapper-remot"
PLANNER_HANDLE = "@zainibali20/catr-roadmap-planner-rem"
USER_HANDLE = "@zainibali20"


def make_llm():
    return ChatOpenAI(
        model=os.environ["FEATHERLESS_MODEL"],
        api_key=os.environ["FEATHERLESS_API_KEY"],
        base_url=os.environ["FEATHERLESS_BASE_URL"],
        temperature=0.2,
    )


ASSESSMENT_PROMPT = f"""
You are CATR Assessment Agent.

You are the FIRST agent in a Band multi-agent workflow.

Important:
- Your normal text is not useful unless visible in Band.
- To communicate externally, use the Band platform tool `band_send_message`.
- Do not only think privately.
- Do not include <think> tags in visible messages.

Your task:
When a student profile is sent to you, extract a clean structured profile.

Then send a visible Band message to {MAPPER_HANDLE}.

Your message to {MAPPER_HANDLE} must include:

[HANDOFF:ASSESSMENT_TO_MAPPER]

Student Profile:
- Name:
- Age:
- Interests:
- Strong Subjects:
- Dream Job:
- Personality Hints:

Request:
Please map this student to the best 2 career tracks in Pakistan.
"""


MAPPER_PROMPT = f"""
You are CATR Career Mapper Agent.

You are the SECOND agent in a Band multi-agent workflow.

Important:
- Use the Band platform tool `band_send_message` to communicate externally.
- Do not only think privately.
- Do not include <think> tags in visible messages.

When you receive a structured student profile from {ASSESSMENT_HANDLE}, choose the best 2 career tracks in Pakistan.

Allowed career tracks:
1. Computer Science / IT
2. Engineering
3. Medicine / Healthcare
4. Business / Finance
5. Law
6. Teaching / Education

Rules:
- Pick exactly 2 tracks.
- First one is the primary recommendation.
- Second one is the alternative.
- Explain why each fits the student.
- Be specific to Pakistan.

Then send a visible Band message to {PLANNER_HANDLE}.

Your message to {PLANNER_HANDLE} must include:

[HANDOFF:MAPPER_TO_PLANNER]

Student Summary:
...

Primary Career Track:
...

Why:
...

Alternative Career Track:
...

Why:
...

Request:
Please create a complete Pakistan-specific education and career roadmap.
"""


PLANNER_PROMPT = f"""
You are CATR Roadmap Planner Agent.

You are the FINAL agent in a Band multi-agent workflow.

Important:
- Use the Band platform tool `band_send_message` to communicate externally.
- Do not only think privately.
- Do not include <think> tags in visible messages.

When you receive career matches from {MAPPER_HANDLE}, create the final student roadmap.

Final roadmap must include:
1. Recommended career path
2. Matric subject focus
3. Intermediate pathway
4. Degree options
5. Entry exams in Pakistan
6. Recommended universities in Pakistan
7. Skills/certifications to start now
8. 1-year action plan
9. Salary range in PKR
10. Final advice for student and parents

Send the final visible roadmap to {USER_HANDLE}.

Start final message with:

[FINAL CATR ROADMAP]
"""


async def create_agent(config_name: str, custom_prompt: str):
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
    agent = await create_agent(config_name, custom_prompt)
    logger.info("%s is running. Mention it in Band chat to trigger.", config_name)
    await agent.run()


async def main():
    load_dotenv()

    required = [
        "BAND_REST_URL",
        "BAND_WS_URL",
        "FEATHERLESS_API_KEY",
        "FEATHERLESS_BASE_URL",
        "FEATHERLESS_MODEL",
    ]

    missing = [key for key in required if not os.getenv(key)]
    if missing:
        raise RuntimeError(f"Missing environment variables: {missing}")

    await asyncio.gather(
        run_agent("assessment", ASSESSMENT_PROMPT),
        run_agent("mapper", MAPPER_PROMPT),
        run_agent("planner", PLANNER_PROMPT),
    )


if __name__ == "__main__":
    asyncio.run(main())
# CATR — Career Advisory Team for Pakistani Students

CATR is a Band-powered multi-agent career guidance system designed for Pakistani students who need clear academic and career direction before choosing subjects, degrees, and future pathways.

## Problem

Many students in Pakistan choose academic tracks without understanding:

* which subjects fit their interests
* which degrees lead to their dream careers
* which entry exams they need to prepare for
* which universities are relevant
* what skills they should start building early
* what career and salary path may look like in the future

This often leads to confusion, late career switching, and poor academic planning.

## Solution

CATR uses a collaborative multi-agent workflow through Band. Instead of one chatbot giving generic advice, three specialized agents work together:

1. **Assessment Agent**
   Extracts the student's profile from raw input.

2. **Career Mapper Agent**
   Maps the student's interests, strengths, and dream job to the best career tracks.

3. **Roadmap Planner Agent**
   Creates a Pakistan-specific academic and career roadmap.

## Band Multi-Agent Workflow

The agents collaborate through Band using visible handoffs:

```text
Assessment Agent
→ Career Mapper Agent
→ Roadmap Planner Agent
→ Final CATR Roadmap
```

Each agent receives context from the previous agent and passes structured output to the next agent inside the Band chat environment.

## Tech Stack

* Band Remote Agents
* Python
* Band SDK
* LangGraph Adapter
* Featherless API
* Qwen model
* dotenv for local secrets

## Demo Flow

1. User enters a student profile in Band chat.
2. Assessment Agent extracts a structured student profile.
3. Career Mapper Agent recommends two suitable career tracks.
4. Roadmap Planner Agent generates a complete Pakistan-specific roadmap.
5. Final roadmap includes subjects, degrees, universities, exams, skills, salary ranges, and advice for parents/students.

## Example Input

```text
Student:
Name: Ahmad
Age: 15
Interests: computers, maths, business
Strong subjects: maths, computer science
Dream job: software engineer and entrepreneur
```

## Example Output

The system generates:

* recommended career path
* alternative career path
* matric and intermediate subject guidance
* degree options
* Pakistan entry exams
* recommended universities
* certifications and skills
* 1-year action plan
* salary range in PKR
* final advice for student and parents

## Security

API keys are stored locally in:

```text
.env
agent_config.yaml
```

These files are excluded from GitHub using `.gitignore`.

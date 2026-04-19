# Prompt-forbedrer

A tool that takes a weak or vague AI prompt and rewrites it using prompt engineering best practices — then explains exactly what changed and why. Great for learning, onboarding, and helping non-technical users get better results from AI tools.

**Author:** Hanne Emaus — informatics student (robotics & AI) at UiO.

---

## Why I built this

One of the biggest barriers to getting value from AI tools is not knowing how to ask good questions. This tool teaches by doing: it improves your prompt and shows you the reasoning behind each change — making it a learning tool as much as a productivity tool.

Particularly relevant for organisations onboarding employees to AI tools (like AI coaching roles).

## What it does

- Takes any prompt as input
- Returns an improved version with specific context, role, format instructions, and audience definition
- Lists 3–5 concrete changes with explanations
- Lets you iterate immediately

## Setup

```bash
pip install anthropic python-dotenv
```

Create a `.env` file:
```
ANTHROPIC_API_KEY=your-key-here
```

## Usage

```bash
python prompt_forbedrer.py
```

## Example

**Input (weak prompt):**
> skriv noe om AI

**Output:**

```
FORBEDRET PROMPT:
Du er en erfaren teknologijournalist som skriver for et norsk næringslivsmagasin.
Skriv en introduksjonsartikkel på 300-400 ord om kunstig intelligens rettet mot
ledere uten teknisk bakgrunn. Artikkelen skal forklare hva AI er, gi ett konkret
eksempel på hvordan det brukes i norsk næringsliv i dag, og avslutte med ett
praktisk råd til ledere som vurderer å ta i bruk AI. Bruk et klart, direkte språk
uten teknisk sjargong.

HVA JEG ENDRET:
- Ga AI-en en tydelig rolle og ekspertise (teknologijournalist)
- Spesifiserte målgruppen (ledere uten teknisk bakgrunn)
- Definerte ønsket lengde (300-400 ord)
- La til krav om konkret eksempel og handlingsrettet avslutning
- Presiserte tone og språknivå (klart, uten sjargong)
```

## Prompt engineering principles applied

- **Role prompting** — give the AI a specific persona
- **Audience definition** — specify who the output is for
- **Format constraints** — length, structure, sections
- **Positive framing** — say what to do, not what to avoid
- **Concrete requirements** — examples, conclusions, tone

## Skills demonstrated

- Anthropic Python SDK
- Meta-prompting (using AI to improve prompts)
- Iterative CLI design
- Teaching-oriented tool design

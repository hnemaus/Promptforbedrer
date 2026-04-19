"""
Prompt-forbedrer
================
Tar inn en svak eller uklar prompt og gjør den bedre.
Viser både den forbedrede prompten og forklarer hva som ble endret.

Nyttig for å lære prompt engineering i praksis.

Krever: pip install anthropic python-dotenv
Forfatter: Hanne Emaus
"""

import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

SYSTEM = """Du er en ekspert på prompt engineering for store språkmodeller.

Du får en svak eller uklar prompt fra en bruker. Din jobb er å:
1. Forbedre prompten slik at den gir bedre resultater fra en AI
2. Forklare kort (3-5 punkter) hva du endret og hvorfor

Svar alltid på norsk i dette formatet:

FORBEDRET PROMPT:
[Den forbedrede prompten her]

HVA JEG ENDRET:
- [punkt 1]
- [punkt 2]
- [osv]

Prinsipper du bruker: gi kontekst og rolle, vær spesifikk på format og lengde, 
definer målgruppe, bruk positivt språk (si hva AI skal gjøre, ikke hva den ikke skal gjøre),
be om steg-for-steg tenkning der det er relevant."""


def forbedre_prompt(prompt: str) -> str:
    klient = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    respons = klient.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        system=SYSTEM,
        messages=[{"role": "user", "content": f"Svak prompt:\n{prompt}"}]
    )
    return respons.content[0].text


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("FEIL: Sett ANTHROPIC_API_KEY i .env-filen.")
        return

    print("=" * 54)
    print("  Prompt-forbedrer  |  Skrevet av Hanne Emaus")
    print("=" * 54)
    print("\nLim inn prompten du vil forbedre:\n")

    linjer = []
    while True:
        linje = input()
        if linje == "":
            break
        linjer.append(linje)

    if not linjer:
        print("Ingen prompt oppgitt.")
        return

    prompt = "\n".join(linjer)
    print("\nAnalyserer og forbedrer...\n")
    print("-" * 54)
    resultat = forbedre_prompt(prompt)
    print(resultat)
    print("-" * 54)

    print("\nVil du prøve en ny prompt? (j/n): ", end="")
    if input().strip().lower() == "j":
        main()


if __name__ == "__main__":
    main()

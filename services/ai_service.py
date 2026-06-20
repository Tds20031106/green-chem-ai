"""
AI Service — wraps an OpenRouter-hosted LLM for green chemistry Q&A.
Falls back to rule-based responses if API key is not set.
"""
import os
import random
import requests
from datetime import datetime

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_MODEL = os.environ.get("OPENROUTER_MODEL", "anthropic/claude-sonnet-4.6")


SYSTEM_PROMPT = """You are GreenChem AI — an expert assistant specialising in green chemistry,
sustainable chemical processes, and the application of artificial intelligence in chemistry.

Your expertise includes:
• The 12 Principles of Green Chemistry (Anastas & Warner, 1998)
• Atom economy, E-factor, PMI, RME and other green metrics
• Green solvent selection and solvent replacement strategies
• Catalysis (enzymatic, photocatalytic, organocatalytic)
• Bio-based feedstocks and renewable raw materials
• Process intensification and flow chemistry
• AI/ML applications in drug discovery, retrosynthesis, reaction prediction
• Life Cycle Assessment (LCA) for chemical processes
• Waste valorisation and circular economy in chemistry

Response style:
• Provide accurate, scientifically grounded information
• Use clear language — explain technical terms when introduced
• Give concrete examples wherever possible
• Suggest practical, actionable improvements
• When discussing metrics, include formulas and benchmark values
• Always consider economic feasibility alongside environmental benefits

If the question is outside green chemistry or AI in chemistry, politely redirect.
"""

GREEN_TIPS = [
    {"tip": "Water is the ultimate green solvent — non-toxic, non-flammable, and cheap. "
            "Many reactions that 'require' organic solvents can be performed in water with the right catalyst.",
     "principle": 5, "category": "Solvents"},
    {"tip": "The E-factor for the pharmaceutical industry averages 25–100 kg waste per kg product. "
            "Pharmaceutical R&D teams are using AI to identify greener synthetic routes early in discovery.",
     "principle": 1, "category": "Metrics"},
    {"tip": "Enzymatic catalysis typically operates at room temperature and neutral pH, "
            "making it one of the most energy-efficient catalytic strategies available.",
     "principle": 9, "category": "Catalysis"},
    {"tip": "Microwave-assisted synthesis can reduce reaction times from hours to minutes "
            "and often improves yields — cutting energy consumption dramatically.",
     "principle": 6, "category": "Energy"},
    {"tip": "Machine learning models like IBM's RXN for Chemistry can predict reaction outcomes "
            "and suggest greener conditions without running lab experiments.",
     "principle": 11, "category": "AI in Chemistry"},
    {"tip": "Atom economy for a Diels-Alder reaction is 100% — all atoms in the diene and "
            "dienophile appear in the product. It's a textbook example of green synthesis.",
     "principle": 2, "category": "Atom Economy"},
    {"tip": "Switchable solvents change polarity or miscibility on demand (e.g. with CO₂), "
            "enabling easy product separation and near-complete solvent recovery.",
     "principle": 5, "category": "Solvents"},
    {"tip": "Deep learning tools like AlphaFold 3 now predict protein-ligand interactions, "
            "reducing the need for large animal studies and cutting chemical waste in drug discovery.",
     "principle": 4, "category": "AI in Chemistry"},
    {"tip": "Solar photocatalysis uses sunlight as a free, renewable energy source to drive "
            "challenging oxidations and C-H functionalisations at room temperature.",
     "principle": 7, "category": "Energy"},
    {"tip": "Flow chemistry (continuous manufacturing) improves heat and mass transfer, "
            "enables safer handling of hazardous intermediates, and reduces solvent volumes.",
     "principle": 12, "category": "Process"},
    {"tip": "Life Cycle Assessment (LCA) looks beyond the reaction flask — transportation, "
            "raw material extraction, and end-of-life all matter for truly sustainable chemistry.",
     "principle": 1, "category": "Sustainability"},
    {"tip": "Supercritical CO₂ (scCO₂) is an excellent green extraction solvent. "
            "It is non-toxic, non-flammable, and CO₂ can be recycled after depressurisation.",
     "principle": 5, "category": "Solvents"},
]

FALLBACK_RESPONSES = {
    "atom economy": (
        "**Atom Economy (AE)** measures how efficiently a reaction incorporates reactant atoms "
        "into the desired product.\n\n"
        "**Formula:** AE = (MW of product / Sum of MW of reactants) × 100%\n\n"
        "**Benchmarks:**\n"
        "• >80% — Excellent ✅\n• 60–80% — Good 🟡\n• <40% — Needs redesign 🔴\n\n"
        "**Example:** Addition reactions (like Diels-Alder) have 100% AE because "
        "all atoms end up in the product, while substitution reactions generate leaving-group waste."
    ),
    "e-factor": (
        "**E-Factor (Environmental Factor)** was introduced by Roger Sheldon in 1992.\n\n"
        "**Formula:** E = mass of waste (kg) / mass of product (kg)\n\n"
        "**Industry benchmarks:**\n"
        "• Petrochemicals: 0.1\n• Bulk chemicals: 1–5\n"
        "• Fine chemicals: 5–50\n• Pharmaceuticals: 25–100+\n\n"
        "**Lower is greener.** A high E-factor signals a need for solvent reduction, "
        "recycling, or route redesign."
    ),
    "green solvent": (
        "**Green Solvent Selection Guide:**\n\n"
        "✅ **Recommended:** Water, ethanol, isopropanol, ethyl acetate, 2-MeTHF, "
        "methyl lactate, Cyrene™, supercritical CO₂\n\n"
        "⚠️ **Use with caution:** Acetone, methanol, toluene, THF\n\n"
        "❌ **Avoid:** Dichloromethane, chloroform, benzene, DMF, NMP, hexane\n\n"
        "Use the GSK solvent sustainability guide or the CHEM21 solvent selection toolkit "
        "to find the best fit for your application."
    ),
    "ai chemistry": (
        "**AI Applications in Green Chemistry:**\n\n"
        "1. **Retrosynthesis planning** — Tools like IBM RXN, AiZynthFinder, and Chemputer "
        "find greener synthetic routes using neural networks trained on millions of reactions.\n\n"
        "2. **Reaction prediction** — ML models predict yields, selectivity, and by-products "
        "without running experiments, saving materials and time.\n\n"
        "3. **Solvent screening** — Quantum chemistry + ML identifies novel green solvents "
        "faster than traditional screening.\n\n"
        "4. **Property prediction** — Graph neural networks predict toxicity, biodegradability, "
        "and environmental persistence of new molecules.\n\n"
        "5. **Process optimisation** — Bayesian optimisation automates the search for "
        "the greenest reaction conditions."
    ),
}


def chat_with_ai(message: str, history: list, api_key: str) -> dict:
    """
    Send a message to an OpenRouter-hosted model and return the response.
    Falls back to rule-based answers if API key is absent.
    """
    if not api_key:
        return _fallback_response(message)

    try:
        messages = [{'role': 'system', 'content': SYSTEM_PROMPT}]
        for h in history[-10:]:  # last 10 turns for context window
            if h.get('role') in ('user', 'assistant') and h.get('content'):
                messages.append({'role': h['role'], 'content': h['content']})
        messages.append({'role': 'user', 'content': message})

        resp = requests.post(
            OPENROUTER_URL,
            headers={
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json',
            },
            json={
                'model': OPENROUTER_MODEL,
                'max_tokens': 1024,
                'messages': messages,
            },
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        reply = data['choices'][0]['message']['content']
        return {
            'response': reply,
            'source': 'openrouter',
            'tokens_used': data.get('usage', {}).get('total_tokens'),
        }
    except Exception as e:
        return _fallback_response(message, error=str(e))


def get_green_tip() -> dict:
    """Return a random green chemistry tip of the day."""
    tip = random.choice(GREEN_TIPS)
    return {
        'tip': tip['tip'],
        'principle_number': tip['principle'],
        'category': tip['category'],
        'date': datetime.utcnow().strftime('%Y-%m-%d'),
    }


def _fallback_response(message: str, error: str = None) -> dict:
    """Return a rule-based response when the API is unavailable."""
    msg_lower = message.lower()
    for keyword, response in FALLBACK_RESPONSES.items():
        if keyword in msg_lower:
            return {
                'response': response,
                'source': 'fallback',
                'note': 'AI API not configured. Set OPENROUTER_API_KEY for full responses.'
            }
    return {
        'response': (
            "I'm running in offline mode (no API key set). "
            "I can answer questions about: **atom economy**, **e-factor**, "
            "**green solvents**, and **AI in chemistry**.\n\n"
            "Set your OPENROUTER_API_KEY in the .env file for full AI-powered responses!"
        ),
        'source': 'fallback',
        'error': error,
    }

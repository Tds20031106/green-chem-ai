"""
Reaction Analyzer & Green Chemistry Principles Service
"""

GREEN_SOLVENTS = {
    'water', 'ethanol', 'ethyl acetate', 'glycerol', 'lactic acid',
    'supercritical co2', 'scco2', 'isopropanol', '2-methylthf',
    'cyrene', 'limonene', 'dimethyl carbonate', 'methyl lactate',
}

HAZARDOUS_SOLVENTS = {
    'benzene', 'chloroform', 'carbon tetrachloride', 'dichloromethane',
    'methylene chloride', 'dmf', 'dimethylformamide', 'nmmp',
    'n-methyl-2-pyrrolidone', 'hexane', 'diethyl ether', 'thf',
    'acetonitrile', 'toluene', 'xylene', 'pyridine',
}

PRINCIPLES = [
    {
        "id": 1,
        "title": "Prevention",
        "short": "Prevent waste rather than treating it after formation.",
        "description": (
            "It is better to prevent waste than to treat or clean up waste after it has been "
            "created. Waste prevention eliminates handling, treatment and disposal costs and "
            "reduces risks to human health and the environment."
        ),
        "icon": "🚫",
        "example": "Using catalytic amounts of a reagent instead of stoichiometric quantities "
                   "eliminates reagent waste and by-product formation.",
        "keywords": ["waste", "prevention", "pollution", "minimize"],
    },
    {
        "id": 2,
        "title": "Atom Economy",
        "short": "Design syntheses so that the final product contains the maximum proportion of starting materials.",
        "description": (
            "Synthetic methods should be designed to maximise the incorporation of all materials "
            "used in the process into the final product. High atom economy means less waste and "
            "better use of raw materials."
        ),
        "icon": "⚛️",
        "example": "Diels-Alder cycloaddition incorporates all atoms of both diene and dienophile "
                   "into the product — 100% atom economy.",
        "keywords": ["atom economy", "efficiency", "incorporation"],
    },
    {
        "id": 3,
        "title": "Less Hazardous Syntheses",
        "short": "Use and generate substances with little or no toxicity.",
        "description": (
            "Wherever practicable, synthetic methods should be designed to use and generate "
            "substances that possess little or no toxicity to human health and the environment."
        ),
        "icon": "🛡️",
        "example": "Replacing phosgene (toxic) with dimethyl carbonate for carbonylation reactions.",
        "keywords": ["hazard", "toxicity", "safety", "non-toxic"],
    },
    {
        "id": 4,
        "title": "Designing Safer Chemicals",
        "short": "Design chemical products to preserve function while reducing toxicity.",
        "description": (
            "Chemical products should be designed to preserve efficacy of function while reducing "
            "toxicity. This means considering the molecular structure and how it influences "
            "environmental persistence, bioaccumulation, and health effects."
        ),
        "icon": "🧬",
        "example": "Designing biodegradable surfactants that maintain cleaning performance but "
                   "break down quickly in the environment.",
        "keywords": ["design", "safer chemicals", "biodegradable", "structure"],
    },
    {
        "id": 5,
        "title": "Safer Solvents & Auxiliaries",
        "short": "Avoid auxiliary substances wherever possible; use safer ones when necessary.",
        "description": (
            "The use of auxiliary substances (e.g. solvents, separation agents) should be made "
            "unnecessary wherever possible and, when used, as innocuous as possible. Water and "
            "bio-based solvents are preferred."
        ),
        "icon": "💧",
        "example": "Using supercritical CO₂ or water as a reaction medium instead of "
                   "chlorinated solvents like DCM or chloroform.",
        "keywords": ["solvent", "auxiliary", "water", "green solvent"],
    },
    {
        "id": 6,
        "title": "Design for Energy Efficiency",
        "short": "Minimise energy requirements; conduct reactions at ambient conditions.",
        "description": (
            "Energy requirements should be recognised for their environmental and economic "
            "impacts and should be minimised. Synthetic methods should be conducted at ambient "
            "temperature and pressure wherever possible."
        ),
        "icon": "⚡",
        "example": "Enzymatic reactions at room temperature replace high-temperature industrial "
                   "processes, dramatically cutting energy consumption.",
        "keywords": ["energy", "efficiency", "ambient", "temperature", "pressure"],
    },
    {
        "id": 7,
        "title": "Use of Renewable Feedstocks",
        "short": "Use renewable raw materials and feedstocks wherever practicable.",
        "description": (
            "A raw material or feedstock should be renewable rather than depleting whenever "
            "technically and economically practicable. Biomass, agricultural waste, and CO₂ "
            "are examples of renewable feedstocks."
        ),
        "icon": "🌱",
        "example": "Bio-ethanol from corn starch or sugarcane replacing petroleum-derived ethanol.",
        "keywords": ["renewable", "feedstock", "biomass", "sustainable"],
    },
    {
        "id": 8,
        "title": "Reduce Derivatives",
        "short": "Avoid unnecessary derivatisation to reduce waste.",
        "description": (
            "Unnecessary derivatisation (e.g. use of blocking groups, protection/deprotection, "
            "temporary modification of physical/chemical processes) should be minimised or "
            "avoided if possible."
        ),
        "icon": "✂️",
        "example": "Direct C-H functionalisation methods that skip protection/deprotection steps, "
                   "reducing the number of synthetic steps and waste generated.",
        "keywords": ["derivatives", "protection", "deprotection", "steps"],
    },
    {
        "id": 9,
        "title": "Catalysis",
        "short": "Use catalytic reagents — selective catalysts are superior to stoichiometric reagents.",
        "description": (
            "Catalytic reagents (as selective as possible) are superior to stoichiometric "
            "reagents. Catalysis improves atom economy, reduces waste, and often allows milder "
            "reaction conditions."
        ),
        "icon": "🔬",
        "example": "Palladium-catalysed cross-coupling (Suzuki, Heck) using ppm catalyst loadings "
                   "instead of stoichiometric organometallic reagents.",
        "keywords": ["catalyst", "catalysis", "stoichiometric", "selective"],
    },
    {
        "id": 10,
        "title": "Design for Degradation",
        "short": "Design products to break down into innocuous products after use.",
        "description": (
            "Chemical products should be designed so that at the end of their function they "
            "break down into innocuous degradation products and do not persist in the environment."
        ),
        "icon": "♻️",
        "example": "Biodegradable plastics like PLA (polylactic acid) that decompose in composting "
                   "conditions, unlike persistent conventional plastics.",
        "keywords": ["degradation", "biodegradable", "persistence", "environment"],
    },
    {
        "id": 11,
        "title": "Real-time Analysis for Pollution Prevention",
        "short": "Monitor and control during synthesis to minimise hazardous substance formation.",
        "description": (
            "Analytical methodologies need to be further developed to allow for real-time, "
            "in-process monitoring and control prior to the formation of hazardous substances. "
            "PAT (Process Analytical Technology) enables this."
        ),
        "icon": "📡",
        "example": "In-line IR spectroscopy monitoring reaction progress in flow chemistry, "
                   "enabling immediate adjustment to prevent over-reaction and waste.",
        "keywords": ["monitoring", "real-time", "analytical", "PAT", "process"],
    },
    {
        "id": 12,
        "title": "Inherently Safer Chemistry",
        "short": "Minimise accident potential — choose substances and processes to prevent accidents.",
        "description": (
            "Substances and the form of a substance used in a chemical process should be chosen "
            "to minimise the potential for chemical accidents, including releases, explosions, "
            "and fires."
        ),
        "icon": "🔒",
        "example": "Using aqueous hydrogen peroxide instead of peracids for epoxidation reactions "
                   "— safer to handle, store, and dispose of.",
        "keywords": ["safety", "accident", "explosion", "fire", "inherently safer"],
    },
]


def get_principles() -> list:
    return PRINCIPLES


def get_principle_by_id(principle_id: int) -> dict | None:
    for p in PRINCIPLES:
        if p['id'] == principle_id:
            return p
    return None


def analyze_reaction(reactants: list, products: list, solvent: str,
                     temperature_c: float, pressure_atm: float,
                     catalyst: str) -> dict:
    """
    Heuristic green chemistry analysis of a reaction.
    Returns a score and recommendations.
    """
    score = 100
    flags = []
    recommendations = []
    principles_applied = []

    # ── Solvent check ────────────────────────────────────────────────────────
    sol_lower = solvent.lower().strip()
    if sol_lower in GREEN_SOLVENTS:
        principles_applied.append(5)
        flags.append({'type': 'success', 'message': f'Green solvent "{solvent}" — excellent choice!'})
    elif sol_lower in HAZARDOUS_SOLVENTS:
        score -= 20
        flags.append({'type': 'warning',
                      'message': f'Hazardous solvent "{solvent}" detected. Consider greener alternatives.'})
        recommendations.append(f'Replace {solvent} with water, ethanol, or ethyl acetate.')
    elif sol_lower:
        flags.append({'type': 'info', 'message': f'Solvent "{solvent}" — verify environmental profile.'})

    # ── Catalyst check ───────────────────────────────────────────────────────
    if catalyst and catalyst.lower() not in ('none', ''):
        score += 5
        principles_applied.append(9)
        flags.append({'type': 'success',
                      'message': f'Catalyst "{catalyst}" used — supports Principle 9 (Catalysis).'})
    else:
        flags.append({'type': 'info',
                      'message': 'No catalyst specified. Could a catalyst improve efficiency?'})
        recommendations.append('Consider using a catalyst to improve selectivity and reduce waste.')

    # ── Temperature check ─────────────────────────────────────────────────────
    if temperature_c <= 50:
        principles_applied.append(6)
        flags.append({'type': 'success', 'message': f'Low temperature ({temperature_c}°C) supports energy efficiency.'})
    elif temperature_c > 150:
        score -= 10
        flags.append({'type': 'warning',
                      'message': f'High temperature ({temperature_c}°C). Consider milder conditions.'})
        recommendations.append('Explore enzyme catalysis or photocatalysis to reduce energy requirements.')

    # ── Pressure check ────────────────────────────────────────────────────────
    if pressure_atm <= 1.5:
        principles_applied.append(6)
    elif pressure_atm > 5:
        score -= 8
        flags.append({'type': 'warning',
                      'message': f'High pressure ({pressure_atm} atm) — increased accident potential.'})
        recommendations.append('Investigate atmospheric-pressure alternatives for safety.')

    # ── Reactant count ────────────────────────────────────────────────────────
    if len(reactants) > 3:
        score -= 5
        flags.append({'type': 'info',
                      'message': 'Many reactants. Explore multi-component or one-pot reactions to reduce steps.'})
        recommendations.append('One-pot multi-component reactions can improve atom economy significantly.')
    else:
        principles_applied.append(8)

    # ── Product count ─────────────────────────────────────────────────────────
    if len(products) > 2:
        score -= 10
        flags.append({'type': 'warning',
                      'message': 'Multiple products detected. Low selectivity increases waste.'})
        recommendations.append('Improve selectivity to minimise by-products.')

    score = max(0, min(100, score))

    if score >= 80:
        overall_rating, color = 'Excellent Green Chemistry', 'green'
    elif score >= 60:
        overall_rating, color = 'Good', 'lightgreen'
    elif score >= 40:
        overall_rating, color = 'Moderate — Room for Improvement', 'orange'
    else:
        overall_rating, color = 'Needs Significant Redesign', 'red'

    return {
        'green_score': score,
        'overall_rating': overall_rating,
        'color': color,
        'flags': flags,
        'recommendations': recommendations,
        'principles_applied': sorted(set(principles_applied)),
        'analysis_summary': {
            'reactant_count': len(reactants),
            'product_count': len(products),
            'solvent': solvent,
            'temperature_c': temperature_c,
            'pressure_atm': pressure_atm,
            'catalyst_used': bool(catalyst and catalyst.lower() not in ('none', '')),
        }
    }

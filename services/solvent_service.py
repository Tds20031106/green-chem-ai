"""
Green Solvent Database and Recommendation Service
Based on GSK Solvent Sustainability Guide & CHEM21 Selection Guide
"""

SOLVENTS_DB = {
    "water": {
        "name": "Water",
        "formula": "H₂O",
        "category": "Highly Recommended",
        "green_score": 98,
        "color": "green",
        "polarity": "polar protic",
        "protic": True,
        "bp_c": 100,
        "mp_c": 0,
        "density": 1.00,
        "hazard": "None",
        "biodegradable": True,
        "renewable": True,
        "gsk_rating": "Recommended",
        "description": "The greenest solvent available. Non-toxic, non-flammable, globally abundant.",
        "pros": ["Non-toxic", "Non-flammable", "Cheap & abundant", "Zero VOC emissions"],
        "cons": ["Limited solubility for hydrophobic compounds", "High boiling point for drying"],
        "applications": ["Aqueous reactions", "Extraction", "Crystallisation", "Biocatalysis"],
        "green_alternatives_for": ["DCM", "Chloroform", "Acetonitrile"],
    },
    "ethanol": {
        "name": "Ethanol",
        "formula": "C₂H₅OH",
        "category": "Recommended",
        "green_score": 85,
        "color": "green",
        "polarity": "polar protic",
        "protic": True,
        "bp_c": 78.4,
        "mp_c": -114,
        "density": 0.789,
        "hazard": "Flammable",
        "biodegradable": True,
        "renewable": True,
        "gsk_rating": "Recommended",
        "description": "Bio-renewable solvent from fermentation. Low toxicity and widely available.",
        "pros": ["Bio-renewable", "Biodegradable", "Low toxicity", "Good solvation power"],
        "cons": ["Flammable", "Forms azeotrope with water"],
        "applications": ["Extractions", "Crystallisation", "Pharmaceutical processing"],
        "green_alternatives_for": ["Methanol", "IPA (for some uses)"],
    },
    "ethyl acetate": {
        "name": "Ethyl Acetate",
        "formula": "CH₃COOC₂H₅",
        "category": "Recommended",
        "green_score": 80,
        "color": "green",
        "polarity": "polar aprotic",
        "protic": False,
        "bp_c": 77.1,
        "mp_c": -83.6,
        "density": 0.897,
        "hazard": "Flammable",
        "biodegradable": True,
        "renewable": True,
        "gsk_rating": "Recommended",
        "description": "Widely used in pharma chromatography. Can be produced from bio-based feedstocks.",
        "pros": ["Low toxicity", "Bio-based production possible", "Good chromatography solvent"],
        "cons": ["Flammable", "Hydrolysis in water", "Moderate boiling point"],
        "applications": ["Column chromatography", "Extractions", "Coatings"],
        "green_alternatives_for": ["DCM", "Hexane (partly)"],
    },
    "2-methylthf": {
        "name": "2-MeTHF",
        "formula": "C₅H₈O",
        "category": "Recommended",
        "green_score": 78,
        "color": "green",
        "polarity": "polar aprotic",
        "protic": False,
        "bp_c": 80,
        "mp_c": -136,
        "density": 0.855,
        "hazard": "Flammable",
        "biodegradable": True,
        "renewable": True,
        "gsk_rating": "Recommended",
        "description": "Bio-derived from furfural. Excellent THF replacement with better green profile.",
        "pros": ["Bio-renewable source", "Separates from water (easy workup)", "Similar to THF", "Less peroxide formation"],
        "cons": ["Flammable", "Still forms peroxides (needs inhibitor)", "Limited biodegradation data"],
        "applications": ["Grignard reactions", "Reductions", "Organometallic chemistry"],
        "green_alternatives_for": ["THF", "Diethyl ether", "Dioxane"],
    },
    "cyrene": {
        "name": "Cyrene (Dihydrolevoglucosenone)",
        "formula": "C₆H₈O₂",
        "category": "Recommended",
        "green_score": 88,
        "color": "green",
        "polarity": "polar aprotic",
        "protic": False,
        "bp_c": 227,
        "mp_c": None,
        "density": 1.25,
        "hazard": "Low",
        "biodegradable": True,
        "renewable": True,
        "gsk_rating": "Recommended",
        "description": "Produced from cellulose. An excellent green alternative to DMF and NMP.",
        "pros": ["100% bio-renewable", "Non-toxic", "Biodegradable", "High boiling point"],
        "cons": ["Relatively expensive", "Limited commercial availability", "High boiling point (hard to remove)"],
        "applications": ["Peptide coupling", "C-C bond forming reactions", "Polymer synthesis"],
        "green_alternatives_for": ["DMF", "NMP", "DMSO"],
    },
    "isopropanol": {
        "name": "Isopropanol (IPA)",
        "formula": "(CH₃)₂CHOH",
        "category": "Recommended",
        "green_score": 75,
        "color": "lightgreen",
        "polarity": "polar protic",
        "protic": True,
        "bp_c": 82.5,
        "mp_c": -89,
        "density": 0.786,
        "hazard": "Flammable",
        "biodegradable": True,
        "renewable": True,
        "gsk_rating": "Recommended",
        "description": "Low toxicity alcohol. Widely used in pharma cleaning and crystallisation.",
        "pros": ["Low toxicity", "Good solvating power", "Widely available"],
        "cons": ["Flammable", "Azeotrope with water", "Fossil-derived (typically)"],
        "applications": ["Pharmaceutical manufacturing", "Cleaning", "Crystallisation"],
        "green_alternatives_for": ["Ethanol (for some uses)"],
    },
    "acetone": {
        "name": "Acetone",
        "formula": "(CH₃)₂CO",
        "category": "Acceptable",
        "green_score": 60,
        "color": "orange",
        "polarity": "polar aprotic",
        "protic": False,
        "bp_c": 56.1,
        "mp_c": -95,
        "density": 0.791,
        "hazard": "Highly Flammable",
        "biodegradable": True,
        "renewable": False,
        "gsk_rating": "Acceptable",
        "description": "Common solvent with reasonable green profile. Produced industrially from propylene.",
        "pros": ["Biodegradable", "Miscible with water", "Low toxicity"],
        "cons": ["Highly flammable", "Low boiling point", "Fossil-derived"],
        "applications": ["General solvent", "Polymer dissolution", "Cleaning"],
        "green_alternatives_for": ["MEK"],
    },
    "methanol": {
        "name": "Methanol",
        "formula": "CH₃OH",
        "category": "Acceptable",
        "green_score": 55,
        "color": "orange",
        "polarity": "polar protic",
        "protic": True,
        "bp_c": 64.7,
        "mp_c": -98,
        "density": 0.792,
        "hazard": "Toxic, Flammable",
        "biodegradable": True,
        "renewable": True,
        "gsk_rating": "Acceptable",
        "description": "Useful but toxic. Bio-methanol from renewable sources is preferred.",
        "pros": ["Good solvating power", "Bio-based production possible", "Low boiling point"],
        "cons": ["Toxic (causes blindness)", "Flammable", "Metabolised to formaldehyde"],
        "applications": ["HPLC mobile phase", "Transesterification", "Extractions"],
        "green_alternatives_for": ["Ethanol is preferred"],
    },
    "thf": {
        "name": "Tetrahydrofuran (THF)",
        "formula": "C₄H₈O",
        "category": "Problematic",
        "green_score": 38,
        "color": "red",
        "polarity": "polar aprotic",
        "protic": False,
        "bp_c": 66,
        "mp_c": -108,
        "density": 0.889,
        "hazard": "Flammable, Peroxide formation",
        "biodegradable": False,
        "renewable": False,
        "gsk_rating": "Problematic",
        "description": "Widely used but problematic — forms explosive peroxides and is not biodegradable.",
        "pros": ["Excellent solvating power", "Miscible with water", "Low boiling point"],
        "cons": ["Forms explosive peroxides", "Not biodegradable", "Fossil-derived", "Reproductive hazard"],
        "applications": ["Organometallic reactions", "Polymer chemistry", "Grignard reactions"],
        "green_alternatives_for": [],
        "greener_alternatives": ["2-MeTHF", "Cyclopentyl methyl ether (CPME)", "Ethyl acetate"],
    },
    "dichloromethane": {
        "name": "Dichloromethane (DCM)",
        "formula": "CH₂Cl₂",
        "category": "Avoid",
        "green_score": 20,
        "color": "red",
        "polarity": "polar aprotic",
        "protic": False,
        "bp_c": 39.6,
        "mp_c": -95,
        "density": 1.325,
        "hazard": "Carcinogen suspect, Narcotic",
        "biodegradable": False,
        "renewable": False,
        "gsk_rating": "Undesirable",
        "description": "Common but highly hazardous. Ozone-depleting, probable carcinogen, narcotic.",
        "pros": ["Excellent solvating power", "Dense (easy separation)", "Low boiling point"],
        "cons": ["Probable carcinogen", "Ozone depleting", "Not biodegradable", "Narcotic"],
        "applications": ["Extractions", "Chromatography", "Pharmaceutical synthesis"],
        "green_alternatives_for": [],
        "greener_alternatives": ["Ethyl acetate", "2-MeTHF", "Cyclopentyl methyl ether", "Water + surfactant"],
    },
    "dmf": {
        "name": "N,N-Dimethylformamide (DMF)",
        "formula": "C₃H₇NO",
        "category": "Avoid",
        "green_score": 15,
        "color": "red",
        "polarity": "polar aprotic",
        "protic": False,
        "bp_c": 153,
        "mp_c": -61,
        "density": 0.944,
        "hazard": "Reproductive toxin (CMR)",
        "biodegradable": False,
        "renewable": False,
        "gsk_rating": "Undesirable",
        "description": "Reproductive toxin (SVHC under REACH). Should be replaced in all processes.",
        "pros": ["Excellent solvating power", "High boiling point", "Wide liquid range"],
        "cons": ["Reproductive toxin", "Difficult to remove", "REACH SVHC", "Not biodegradable"],
        "applications": ["Amide coupling reactions", "Polymer dissolution", "MOF synthesis"],
        "green_alternatives_for": [],
        "greener_alternatives": ["Cyrene", "DMSO (where applicable)", "N-butyl pyrrolidone (NBP)"],
    },
    "toluene": {
        "name": "Toluene",
        "formula": "C₇H₈",
        "category": "Problematic",
        "green_score": 35,
        "color": "orange",
        "polarity": "nonpolar",
        "protic": False,
        "bp_c": 110.6,
        "mp_c": -95,
        "density": 0.867,
        "hazard": "Reproductive toxin (suspected), Flammable",
        "biodegradable": True,
        "renewable": False,
        "gsk_rating": "Problematic",
        "description": "Suspected reproductive toxin. Better alternatives now exist for most uses.",
        "pros": ["Good solvating for non-polars", "Moderate boiling point"],
        "cons": ["Reproductive toxin suspected", "Flammable", "VOC concerns"],
        "applications": ["Non-polar extractions", "Paint", "Adhesives"],
        "green_alternatives_for": [],
        "greener_alternatives": ["Cyrene", "Cyclopentyl methyl ether", "2-MeTHF"],
    },
    "hexane": {
        "name": "n-Hexane",
        "formula": "C₆H₁₄",
        "category": "Avoid",
        "green_score": 22,
        "color": "red",
        "polarity": "nonpolar",
        "protic": False,
        "bp_c": 68.7,
        "mp_c": -95,
        "density": 0.659,
        "hazard": "Neurotoxin, Highly Flammable",
        "biodegradable": False,
        "renewable": False,
        "gsk_rating": "Undesirable",
        "description": "Neurotoxic (peripheral neuropathy). Avoid in favour of heptane or bio-based alternatives.",
        "pros": ["Good for non-polar extraction", "Low boiling point"],
        "cons": ["Neurotoxic", "Highly flammable", "Not biodegradable", "High VOC"],
        "applications": ["Oil extraction", "Chromatography", "Polymerisation"],
        "green_alternatives_for": [],
        "greener_alternatives": ["Heptane (less toxic)", "Cyclopentane", "Bio-based hydrocarbons"],
    },
    "ethyl lactate": {
        "name": "Ethyl Lactate",
        "formula": "C₅H₁₀O₃",
        "category": "Recommended",
        "green_score": 87,
        "color": "green",
        "polarity": "polar aprotic",
        "protic": False,
        "bp_c": 154,
        "mp_c": -26,
        "density": 1.03,
        "hazard": "Low",
        "biodegradable": True,
        "renewable": True,
        "gsk_rating": "Recommended",
        "description": "100% bio-renewable from lactic acid fermentation. Excellent green solvent with good solvating power.",
        "pros": ["100% bio-renewable", "Non-toxic", "Biodegradable", "FDA GRAS"],
        "cons": ["Relatively high boiling point", "Limited availability"],
        "applications": ["Coatings", "Pharmaceutical", "Electronics cleaning"],
        "green_alternatives_for": ["DMF", "Toluene", "Ketones"],
    },
}


def get_all_solvents(category: str = None) -> list:
    solvents = list(SOLVENTS_DB.values())
    if category:
        cat_lower = category.lower()
        solvents = [s for s in solvents if s['category'].lower() == cat_lower]
    return sorted(solvents, key=lambda x: x['green_score'], reverse=True)


def get_solvent_details(name: str) -> dict | None:
    name_lower = name.lower().replace(' ', '').replace('-', '')
    for key, sol in SOLVENTS_DB.items():
        if (key.replace(' ', '').replace('-', '') == name_lower or
                sol['name'].lower().replace(' ', '').replace('-', '') == name_lower):
            return sol
    return None


def recommend_solvents(current_solvent: str, application: str,
                       polarity_needed: str, protic) -> list:
    """Recommend greener solvents based on constraints."""
    recommendations = []
    sol_lower = current_solvent.lower().strip()

    # Fetch alternatives listed directly for this solvent
    current = None
    for key, sol in SOLVENTS_DB.items():
        if key == sol_lower or sol['name'].lower() == sol_lower:
            current = sol
            break

    for key, sol in SOLVENTS_DB.items():
        score_boost = 0

        # Must be greener
        if sol['green_score'] < 70:
            continue

        # Polarity filter
        if polarity_needed not in ('any', '', None):
            if polarity_needed.lower() not in sol['polarity']:
                continue

        # Protic filter
        if protic is not None:
            if bool(protic) != sol['protic']:
                continue

        # Directly listed as alternative for the current solvent
        if current and sol['name'] in current.get('greener_alternatives', []):
            score_boost += 20

        # Application keyword match
        if application:
            app_lower = application.lower()
            for app in sol.get('applications', []):
                if any(word in app.lower() for word in app_lower.split()):
                    score_boost += 10
                    break

        recommendations.append({
            'name': sol['name'],
            'formula': sol['formula'],
            'green_score': sol['green_score'],
            'relevance_score': sol['green_score'] + score_boost,
            'category': sol['category'],
            'polarity': sol['polarity'],
            'hazard': sol['hazard'],
            'biodegradable': sol['biodegradable'],
            'renewable': sol['renewable'],
            'applications': sol['applications'],
            'description': sol['description'],
        })

    return sorted(recommendations, key=lambda x: x['relevance_score'], reverse=True)[:5]


def compare_solvents(a: str, b: str) -> dict:
    sol_a = get_solvent_details(a)
    sol_b = get_solvent_details(b)
    if not sol_a:
        return {'error': f'Solvent "{a}" not found'}
    if not sol_b:
        return {'error': f'Solvent "{b}" not found'}

    winner = sol_a['name'] if sol_a['green_score'] >= sol_b['green_score'] else sol_b['name']
    return {
        'solvent_a': sol_a,
        'solvent_b': sol_b,
        'greener': winner,
        'score_difference': abs(sol_a['green_score'] - sol_b['green_score']),
    }


def search_solvents(query: str) -> list:
    q = query.lower()
    results = []
    for sol in SOLVENTS_DB.values():
        if (q in sol['name'].lower() or
                q in sol['polarity'].lower() or
                q in sol['category'].lower() or
                any(q in app.lower() for app in sol.get('applications', []))):
            results.append(sol)
    return sorted(results, key=lambda x: x['green_score'], reverse=True)

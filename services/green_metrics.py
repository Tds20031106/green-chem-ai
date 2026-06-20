"""
Green Chemistry Metrics Service
Implements the standard green chemistry metrics:
  - Atom Economy (AE)        – Trost, 1991
  - E-Factor                 – Sheldon, 1992
  - Process Mass Intensity   – ACS GCI, 2011
  - Reaction Mass Efficiency – Curzons et al., 2001
"""


def calculate_atom_economy(reactant_mw_list: list, product_mw: float) -> float:
    """
    AE = (MW of desired product / sum of MW of all reactants) × 100
    Returns percentage (0-100).
    """
    total_reactant_mw = sum(reactant_mw_list)
    if total_reactant_mw <= 0:
        return 0.0
    ae = (product_mw / total_reactant_mw) * 100
    return round(min(ae, 100.0), 2)


def calculate_e_factor(waste_g: float, product_g: float) -> float:
    """
    E = mass of waste (g) / mass of product (g)
    Lower is greener. Ideal = 0.
    """
    if product_g <= 0:
        return float('inf')
    return waste_g / product_g


def calculate_pmi(total_materials_g: float, product_g: float) -> float:
    """
    PMI = total mass of all process materials (g) / mass of product (g)
    Includes solvents, reagents, catalysts, water used.
    Ideal PMI = 1 (everything ends up in product).
    """
    if product_g <= 0:
        return float('inf')
    return total_materials_g / product_g


def calculate_rme(actual_yield_g: float, theoretical_yield_g: float,
                  atom_economy_pct: float, stoichiometric_factor: float = 1.0) -> float:
    """
    RME = (yield% / 100) × AE × (1 / SF) × 100
    Combines yield, atom economy, and stoichiometry into one efficiency %.
    """
    if theoretical_yield_g <= 0 or stoichiometric_factor <= 0:
        return 0.0
    percent_yield = actual_yield_g / theoretical_yield_g
    ae = atom_economy_pct / 100.0
    rme = percent_yield * ae * (1.0 / stoichiometric_factor)
    return round(min(rme * 100, 100.0), 2)


def calculate_rxe(actual_yield_g: float, theoretical_yield_g: float) -> float:
    """Reaction yield as a simple percentage."""
    if theoretical_yield_g <= 0:
        return 0.0
    return round((actual_yield_g / theoretical_yield_g) * 100, 2)


def get_overall_green_score(metrics: dict) -> dict:
    """
    Aggregate an overall green score (0–100) from available metrics.
    """
    scores = []

    if 'atom_economy' in metrics:
        scores.append(metrics['atom_economy']['value'])

    if 'rme' in metrics:
        scores.append(metrics['rme']['value'])

    if 'percent_yield' in metrics:
        scores.append(metrics['percent_yield']['value'])

    if 'e_factor' in metrics:
        ef = metrics['e_factor']['value']
        # Convert E-factor to a 0-100 score (lower EF → higher score)
        ef_score = max(0, 100 - ef * 4)
        scores.append(ef_score)

    if 'pmi' in metrics:
        pmi = metrics['pmi']['value']
        pmi_score = max(0, 100 - (pmi - 1) * 2)
        scores.append(pmi_score)

    if not scores:
        return {'score': 0, 'rating': 'N/A', 'color': 'grey', 'tips': []}

    overall = round(sum(scores) / len(scores), 1)

    if overall >= 80:
        rating, color = 'Excellent', 'green'
    elif overall >= 60:
        rating, color = 'Good', 'lightgreen'
    elif overall >= 40:
        rating, color = 'Moderate', 'orange'
    else:
        rating, color = 'Needs Improvement', 'red'

    tips = _generate_tips(metrics, overall)
    return {'score': overall, 'rating': rating, 'color': color, 'tips': tips}


def _generate_tips(metrics: dict, score: float) -> list:
    tips = []
    if 'atom_economy' in metrics and metrics['atom_economy']['value'] < 60:
        tips.append('Redesign the synthesis route to maximise atom economy — '
                    'consider condensation or addition reactions over substitution.')
    if 'e_factor' in metrics and metrics['e_factor']['value'] > 10:
        tips.append('High E-factor detected. Reduce solvent usage or switch to '
                    'solvent-free conditions and recycle waste streams.')
    if 'pmi' in metrics and metrics['pmi']['value'] > 20:
        tips.append('PMI is high. Audit all auxiliary materials; eliminate '
                    'unnecessary reagents and minimise solvent volumes.')
    if 'percent_yield' in metrics and metrics['percent_yield']['value'] < 70:
        tips.append('Optimise reaction conditions (temperature, time, catalyst '
                    'loading) to improve yield and reduce raw material consumption.')
    if score >= 80:
        tips.append('Great green chemistry profile! Consider a full LCA to '
                    'identify any remaining environmental hotspots.')
    return tips

from flask import Blueprint, request, jsonify
from services.green_metrics import (
    calculate_atom_economy, calculate_e_factor,
    calculate_pmi, calculate_rme, calculate_rxe,
    get_overall_green_score
)

metrics_bp = Blueprint('metrics', __name__)


@metrics_bp.route('/calculate', methods=['POST'])
def calculate_all_metrics():
    """
    Calculate all green chemistry metrics.
    Body JSON:
    {
      "reactant_mw_list": [float],   # MW of all reactants in g/mol
      "product_mw": float,           # MW of desired product in g/mol
      "actual_yield_g": float,       # mass of product obtained (g)
      "theoretical_yield_g": float,  # theoretical max product mass (g)
      "waste_kg": float,             # total waste generated (kg)
      "total_materials_kg": float,   # all materials used incl. solvents (kg)
      "stoichiometric_factor": float # default 1.0
    }
    """
    data = request.get_json(silent=True) or {}

    try:
        reactant_mw_list    = [float(x) for x in data.get('reactant_mw_list', [])]
        product_mw          = float(data.get('product_mw', 0))
        actual_yield_g      = float(data.get('actual_yield_g', 0))
        theoretical_yield_g = float(data.get('theoretical_yield_g', 0))
        waste_kg            = float(data.get('waste_kg', 0))
        total_materials_kg  = float(data.get('total_materials_kg', 0))
        stoich_factor       = float(data.get('stoichiometric_factor', 1.0))
    except (TypeError, ValueError) as e:
        return jsonify({'error': f'Invalid numeric input: {e}'}), 400

    if not reactant_mw_list or product_mw <= 0:
        return jsonify({'error': 'reactant_mw_list and product_mw are required'}), 400

    results = {}

    # Atom Economy
    ae = calculate_atom_economy(reactant_mw_list, product_mw)
    results['atom_economy'] = {
        'value': ae,
        'unit': '%',
        'description': 'Percentage of reactant atoms incorporated into the desired product',
        'rating': _rate(ae, [(80, 'Excellent'), (60, 'Good'), (40, 'Fair'), (0, 'Poor')])
    }

    # E-Factor (Environmental Factor)
    if actual_yield_g > 0:
        ef = calculate_e_factor(waste_kg * 1000, actual_yield_g)
        results['e_factor'] = {
            'value': round(ef, 3),
            'unit': 'kg waste / kg product',
            'description': 'Mass of waste generated per unit mass of desired product',
            'rating': _rate_inverse(ef, [(1, 'Excellent'), (5, 'Good'), (25, 'Fair'), (9999, 'Poor')])
        }

    # PMI (Process Mass Intensity)
    if actual_yield_g > 0:
        pmi = calculate_pmi(total_materials_kg * 1000, actual_yield_g)
        results['pmi'] = {
            'value': round(pmi, 3),
            'unit': 'kg total input / kg product',
            'description': 'Total mass of all materials used per unit mass of product',
            'rating': _rate_inverse(pmi, [(5, 'Excellent'), (15, 'Good'), (50, 'Fair'), (9999, 'Poor')])
        }

    # Reaction Mass Efficiency
    if theoretical_yield_g > 0 and actual_yield_g > 0:
        rme = calculate_rme(actual_yield_g, theoretical_yield_g, ae, stoich_factor)
        results['rme'] = {
            'value': round(rme, 2),
            'unit': '%',
            'description': 'Overall efficiency combining yield, atom economy & stoichiometry',
            'rating': _rate(rme, [(70, 'Excellent'), (50, 'Good'), (30, 'Fair'), (0, 'Poor')])
        }

    # Reaction Yield %
    if theoretical_yield_g > 0 and actual_yield_g > 0:
        yield_pct = (actual_yield_g / theoretical_yield_g) * 100
        results['percent_yield'] = {
            'value': round(yield_pct, 2),
            'unit': '%',
            'description': 'Actual yield as a percentage of theoretical maximum',
            'rating': _rate(yield_pct, [(90, 'Excellent'), (70, 'Good'), (50, 'Fair'), (0, 'Poor')])
        }

    overall = get_overall_green_score(results)
    return jsonify({
        'metrics': results,
        'overall_score': overall['score'],
        'overall_rating': overall['rating'],
        'overall_color': overall['color'],
        'tips': overall['tips']
    })


@metrics_bp.route('/atom-economy', methods=['POST'])
def atom_economy():
    """Quick atom economy calculation."""
    data = request.get_json(silent=True) or {}
    try:
        reactant_mws = [float(x) for x in data.get('reactant_mw_list', [])]
        product_mw   = float(data.get('product_mw', 0))
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400
    if not reactant_mws or product_mw <= 0:
        return jsonify({'error': 'reactant_mw_list and product_mw are required'}), 400
    ae = calculate_atom_economy(reactant_mws, product_mw)
    return jsonify({'atom_economy_percent': ae, 'rating': _rate(ae, [(80,'Excellent'),(60,'Good'),(40,'Fair'),(0,'Poor')])})


@metrics_bp.route('/e-factor', methods=['POST'])
def e_factor():
    """Quick E-factor calculation."""
    data = request.get_json(silent=True) or {}
    try:
        waste_g   = float(data.get('waste_g', 0))
        product_g = float(data.get('product_g', 0))
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400
    if product_g <= 0:
        return jsonify({'error': 'product_g must be > 0'}), 400
    ef = calculate_e_factor(waste_g, product_g)
    return jsonify({'e_factor': round(ef, 4),
                    'rating': _rate_inverse(ef, [(1,'Excellent'),(5,'Good'),(25,'Fair'),(9999,'Poor')])})


# ── helpers ────────────────────────────────────────────────────────────────
def _rate(value, thresholds):
    """Higher is better."""
    for cutoff, label in thresholds:
        if value >= cutoff:
            return label
    return 'Poor'


def _rate_inverse(value, thresholds):
    """Lower is better."""
    for cutoff, label in thresholds:
        if value <= cutoff:
            return label
    return 'Poor'

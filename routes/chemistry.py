from flask import Blueprint, request, jsonify
from services.reaction_analyzer import analyze_reaction, get_principles, get_principle_by_id

chemistry_bp = Blueprint('chemistry', __name__)


@chemistry_bp.route('/principles', methods=['GET'])
def get_all_principles():
    """Return all 12 principles of green chemistry."""
    principles = get_principles()
    return jsonify({'principles': principles, 'count': len(principles)})


@chemistry_bp.route('/principles/<int:principle_id>', methods=['GET'])
def get_principle(principle_id):
    """Return a specific green chemistry principle by ID (1-12)."""
    if not 1 <= principle_id <= 12:
        return jsonify({'error': 'Principle ID must be between 1 and 12'}), 400
    principle = get_principle_by_id(principle_id)
    if not principle:
        return jsonify({'error': 'Principle not found'}), 404
    return jsonify(principle)


@chemistry_bp.route('/analyze', methods=['POST'])
def analyze():
    """
    Analyze the green chemistry score of a reaction.
    Body JSON: { reactants, products, solvent, temperature_c, pressure_atm, catalyst }
    """
    data = request.get_json(silent=True) or {}
    reactants  = data.get('reactants', [])
    products   = data.get('products', [])
    solvent    = data.get('solvent', 'water')
    temp_c     = data.get('temperature_c', 25)
    pressure   = data.get('pressure_atm', 1.0)
    catalyst   = data.get('catalyst', '')

    if not reactants or not products:
        return jsonify({'error': 'reactants and products are required'}), 400

    result = analyze_reaction(reactants, products, solvent, temp_c, pressure, catalyst)
    return jsonify(result)


@chemistry_bp.route('/carbon-footprint', methods=['POST'])
def carbon_footprint():
    """
    Estimate the carbon footprint of a chemical process.
    Body JSON: { energy_kwh, solvent_liters, solvent_type, waste_kg, transport_km }
    """
    data = request.get_json(silent=True) or {}
    energy_kwh    = float(data.get('energy_kwh', 0))
    solvent_l     = float(data.get('solvent_liters', 0))
    solvent_type  = data.get('solvent_type', 'ethanol')
    waste_kg      = float(data.get('waste_kg', 0))
    transport_km  = float(data.get('transport_km', 0))

    # Emission factors (kg CO2-eq per unit)
    energy_factor   = 0.233   # kg CO2/kWh (average grid)
    solvent_factors = {
        'ethanol': 1.5, 'methanol': 0.9, 'acetone': 2.1,
        'dichloromethane': 3.4, 'toluene': 2.8, 'water': 0.0003,
        'ethyl acetate': 1.8, 'dmso': 1.6, 'thf': 2.5,
        'hexane': 2.7, 'dmf': 2.0, 'acetonitrile': 3.2,
    }
    waste_factor     = 0.5    # kg CO2/kg waste (avg treatment)
    transport_factor = 0.096  # kg CO2/km (road freight, per tonne assumed 1t)

    sf = solvent_factors.get(solvent_type.lower(), 2.0)
    energy_co2    = energy_kwh * energy_factor
    solvent_co2   = solvent_l  * sf
    waste_co2     = waste_kg   * waste_factor
    transport_co2 = transport_km * transport_factor

    total = energy_co2 + solvent_co2 + waste_co2 + transport_co2

    # Rating
    if total < 5:
        rating, color = 'Excellent', 'green'
    elif total < 15:
        rating, color = 'Good', 'lightgreen'
    elif total < 30:
        rating, color = 'Moderate', 'orange'
    else:
        rating, color = 'High Impact', 'red'

    return jsonify({
        'total_co2_kg': round(total, 3),
        'breakdown': {
            'energy_co2_kg':    round(energy_co2, 3),
            'solvent_co2_kg':   round(solvent_co2, 3),
            'waste_co2_kg':     round(waste_co2, 3),
            'transport_co2_kg': round(transport_co2, 3),
        },
        'rating': rating,
        'color':  color,
        'recommendations': _co2_recommendations(total, energy_co2, solvent_co2),
    })


def _co2_recommendations(total, energy, solvent):
    tips = []
    if energy / (total + 0.001) > 0.4:
        tips.append('Switch to renewable energy sources to cut the largest share of emissions.')
    if solvent / (total + 0.001) > 0.3:
        tips.append('Replace conventional solvents with water or bio-based green alternatives.')
    if total > 20:
        tips.append('Consider flow chemistry to improve energy efficiency and reduce waste.')
    tips.append('Apply life-cycle assessment (LCA) to identify further reduction opportunities.')
    return tips

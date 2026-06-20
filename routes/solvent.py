from flask import Blueprint, request, jsonify
from services.solvent_service import (
    get_all_solvents, recommend_solvents, get_solvent_details,
    compare_solvents, search_solvents
)

solvent_bp = Blueprint('solvent', __name__)


@solvent_bp.route('/list', methods=['GET'])
def list_solvents():
    """Return all solvents with optional category filter."""
    category = request.args.get('category', None)
    solvents = get_all_solvents(category)
    return jsonify({'solvents': solvents, 'count': len(solvents)})


@solvent_bp.route('/recommend', methods=['POST'])
def recommend():
    """
    Recommend green solvents for a given use case.
    Body JSON: { current_solvent, application, polarity_needed, protic }
    """
    data = request.get_json(silent=True) or {}
    current_solvent  = data.get('current_solvent', '')
    application      = data.get('application', '')
    polarity_needed  = data.get('polarity_needed', 'any')
    protic           = data.get('protic', None)

    recommendations = recommend_solvents(current_solvent, application, polarity_needed, protic)
    return jsonify({'recommendations': recommendations,
                    'query': {'current_solvent': current_solvent, 'application': application}})


@solvent_bp.route('/details/<solvent_name>', methods=['GET'])
def details(solvent_name):
    """Return detailed info about a specific solvent."""
    sol = get_solvent_details(solvent_name.lower())
    if not sol:
        return jsonify({'error': f'Solvent "{solvent_name}" not found'}), 404
    return jsonify(sol)


@solvent_bp.route('/compare', methods=['POST'])
def compare():
    """
    Compare two solvents side by side.
    Body JSON: { solvent_a: str, solvent_b: str }
    """
    data = request.get_json(silent=True) or {}
    a = data.get('solvent_a', '').lower()
    b = data.get('solvent_b', '').lower()
    if not a or not b:
        return jsonify({'error': 'solvent_a and solvent_b are required'}), 400
    result = compare_solvents(a, b)
    if 'error' in result:
        return jsonify(result), 404
    return jsonify(result)


@solvent_bp.route('/search', methods=['GET'])
def search():
    """Search solvents by name or property."""
    query = request.args.get('q', '').strip()
    if not query:
        return jsonify({'error': 'Search query "q" is required'}), 400
    results = search_solvents(query)
    return jsonify({'results': results, 'count': len(results), 'query': query})

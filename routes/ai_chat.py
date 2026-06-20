from flask import Blueprint, request, jsonify, current_app
from services.ai_service import chat_with_ai, get_green_tip

ai_chat_bp = Blueprint('ai_chat', __name__)


@ai_chat_bp.route('/message', methods=['POST'])
def chat():
    """
    AI chat endpoint for green chemistry questions.
    Body JSON: { message: str, history: [{ role, content }] }
    """
    data = request.get_json(silent=True) or {}
    message = data.get('message', '').strip()
    history = data.get('history', [])

    if not message:
        return jsonify({'error': 'Message cannot be empty'}), 400
    if len(message) > 2000:
        return jsonify({'error': 'Message too long (max 2000 chars)'}), 400

    api_key = current_app.config.get('OPENROUTER_API_KEY', '')
    response = chat_with_ai(message, history, api_key)
    return jsonify(response)


@ai_chat_bp.route('/tip', methods=['GET'])
def daily_tip():
    """Return a green chemistry tip of the day."""
    return jsonify(get_green_tip())


@ai_chat_bp.route('/quick-answer', methods=['POST'])
def quick_answer():
    """
    Quick one-shot answer for green chemistry questions (no history).
    Body JSON: { question: str }
    """
    data = request.get_json(silent=True) or {}
    question = data.get('question', '').strip()
    if not question:
        return jsonify({'error': 'question is required'}), 400

    api_key = current_app.config.get('OPENROUTER_API_KEY', '')
    response = chat_with_ai(question, [], api_key)
    return jsonify(response)

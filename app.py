from flask import Flask, jsonify
from flask_cors import CORS
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    from routes.chemistry import chemistry_bp
    from routes.ai_chat import ai_chat_bp
    from routes.metrics import metrics_bp
    from routes.solvent import solvent_bp

    app.register_blueprint(chemistry_bp, url_prefix='/api/chemistry')
    app.register_blueprint(ai_chat_bp, url_prefix='/api/chat')
    app.register_blueprint(metrics_bp, url_prefix='/api/metrics')
    app.register_blueprint(solvent_bp, url_prefix='/api/solvent')

    @app.route('/api/health')
    def health():
        return jsonify({
            'status': 'ok',
            'message': 'GreenChem AI API is running 🌿',
            'version': '1.0.0'
        })

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({'error': 'Endpoint not found'}), 404

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({'error': 'Internal server error'}), 500

    return app

app = create_app()

if __name__ == '__main__':
    cfg = Config()
    app.run(
        debug=cfg.DEBUG,
        host='0.0.0.0',
        port=int(os.environ.get("PORT", 5000))
    )
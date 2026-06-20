# GreenChem AI — Flask Backend

A comprehensive REST API for the Green Chemistry & AI mobile application.

## Features
- 🤖 **AI Chat** — Powered by Claude (Anthropic) for expert green chemistry Q&A
- ⚗️ **Reaction Analyzer** — Heuristic green score for chemical reactions
- 📊 **Metrics Calculator** — Atom Economy, E-Factor, PMI, RME, % Yield
- 🧪 **Solvent Database** — 13+ solvents with green ratings, comparison & recommendations
- 📚 **12 Principles** — Full guide to Anastas & Warner's 12 Green Chemistry Principles
- 🌍 **Carbon Footprint** — Process CO₂-equivalent estimator

## Setup

```bash
# 1. Create and activate virtual environment
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY

# 4. Run the server
python app.py
```

The API will start at `http://0.0.0.0:5000`

## API Endpoints

### Health
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Server health check |

### Chemistry
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/chemistry/principles` | All 12 green chemistry principles |
| GET | `/api/chemistry/principles/<id>` | Single principle (1–12) |
| POST | `/api/chemistry/analyze` | Analyze reaction green score |
| POST | `/api/chemistry/carbon-footprint` | Estimate CO₂ footprint |

### AI Chat
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/chat/message` | AI-powered green chemistry chat |
| GET | `/api/chat/tip` | Random green chemistry tip |
| POST | `/api/chat/quick-answer` | One-shot question |

### Metrics
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/metrics/calculate` | Calculate all green metrics |
| POST | `/api/metrics/atom-economy` | Quick atom economy |
| POST | `/api/metrics/e-factor` | Quick E-factor |

### Solvents
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/solvent/list` | All solvents (filter by category) |
| POST | `/api/solvent/recommend` | Get green solvent recommendations |
| GET | `/api/solvent/details/<name>` | Detailed solvent info |
| POST | `/api/solvent/compare` | Compare two solvents |
| GET | `/api/solvent/search?q=<query>` | Search solvents |

## Example Requests

### Analyze a Reaction
```bash
curl -X POST http://localhost:5000/api/chemistry/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "reactants": ["benzaldehyde", "acetophenone"],
    "products": ["chalcone"],
    "solvent": "ethanol",
    "temperature_c": 25,
    "catalyst": "NaOH"
  }'
```

### Calculate Metrics
```bash
curl -X POST http://localhost:5000/api/metrics/calculate \
  -H "Content-Type: application/json" \
  -d '{
    "reactant_mw_list": [106.1, 58.1],
    "product_mw": 146.2,
    "actual_yield_g": 12.5,
    "theoretical_yield_g": 15.0,
    "waste_kg": 0.05,
    "total_materials_kg": 0.5
  }'
```

### Chat with AI
```bash
curl -X POST http://localhost:5000/api/chat/message \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What is atom economy and why does it matter?",
    "history": []
  }'
```

## Notes
- Without `ANTHROPIC_API_KEY`, the chat endpoint uses rule-based fallback responses
- Flutter app connects to `http://10.0.2.2:5000` on Android emulator (localhost mapping)
- For physical devices, update the `baseUrl` in the Flutter `api_service.dart`

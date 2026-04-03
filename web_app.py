from flask import Flask, render_template, request, jsonify
import os
from models.llm import call_llm

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def root():
    return render_template('dashboard.html', metrics=_load_metrics())

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', metrics=_load_metrics())

@app.route('/textgen')
def textgen():
    return render_template('textgen.html')

@app.route('/manual')
def manual():
    return render_template('manual.html')

@app.route('/automation')
def automation():
    return render_template('automation.html')

@app.route('/api/metrics', methods=['GET'])
def metrics_api():
    return jsonify(_load_metrics())

@app.route('/api/textgen', methods=['POST'])
def textgen_api():
    data = request.get_json(force=True)
    prompt = data.get('prompt', '').strip()
    model = data.get('model', 'mistral')
    temperature = float(data.get('temperature', 0.2))
    max_tokens = int(data.get('max_tokens', 512))

    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    try:
        response_text = call_llm(prompt, model=model, temperature=temperature, max_tokens=max_tokens)
        return jsonify({'prompt': prompt, 'result': response_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


def _load_metrics():
    # Placeholder metrics for dashboard.
    # Later this can read actual files from output/ or derive from logs.
    return {
        'active_tests': 256,
        'generated_cases': 712,
        'pass_rate': 91.4,
        'total_api_calls': 3878,
        'last_run': '2026-04-03 12:45:00',
        'chart': {
            'labels': ['-11h', '-10h', '-9h', '-8h', '-7h', '-6h', '-5h', '-4h', '-3h', '-2h', '-1h', 'Now'],
            'values': [14, 12, 21, 18, 24, 33, 27, 35, 40, 38, 42, 46]
        }
    }


if __name__ == '__main__':
    os.environ.setdefault('FLASK_ENV', 'development')
    app.run(host='127.0.0.1', port=5000, debug=True)

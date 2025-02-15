import os
import warnings
from datetime import datetime
DATA_DIR = os.path.join(os.getenv('HOME', '/home'), 'data')
os.makedirs(DATA_DIR, exist_ok=True)

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

# Add the parent directory to sys.path to import the crew
#sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import the crew
#from agent_one.src.agent_one.crew import AgentOne
from src.agent_one.crew import AgentOne

from flask import Flask, request, jsonify, render_template

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Initialize Flask app
app = Flask(__name__)

def run(topic):
    """
    Run the crew with the provided topic.
    """
    inputs = {
        'topic': topic,
        'current_year': str(datetime.now().year)
    }
    
    try:
        # Kickoff the crew with the provided inputs
        output = AgentOne().crew().kickoff(inputs=inputs)
        
        # Return the output
        return str(output)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {str(e)}")

@app.route('/run', methods=['POST'])
def handle_run():
    """
    Flask endpoint to handle POST requests for running the crew.
    Expects JSON input with a 'topic' field.
    """
    try:
        # Parse JSON data from the request
        data = request.get_json()
        if not data or 'topic' not in data:
            return jsonify({"error": "Missing 'topic' in request body"}), 400
        
        # Extract the topic from the request
        topic = data['topic']
        
        # Run the crew with the provided topic
        result = run(topic) 
        
        # Return the result as a JSON response
        return jsonify({"message": "Crew executed successfully", "result": result}), 200
    
    except Exception as e:
        # Handle any exceptions and return an error response
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    """
    Serve the HTML frontend.
    """
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask app
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

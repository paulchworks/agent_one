import sys
import warnings

from datetime import datetime

#from agent_one.src.agent_one.crew import AgentOne

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

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
        #result = AgentOne().crew().kickoff(inputs=inputs)
        
        # Simulate the result of running the crew
        result = f"Crew executed successfully for topic: {topic}"
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

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
    app.run(host='0.0.0.0', port=5000)
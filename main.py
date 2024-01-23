
# Import necessary modules
from flask import Flask, render_template, request, jsonify
import vllm

# Initialize the Flask application
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    """Renders the home page."""

    # Return the index.html file
    return render_template('index.html')

# Define the chat route
@app.route('/chat', methods=['POST'])
def chat():
    """Handles AJAX requests for generating chatbot responses."""

    # Get the user's message
    message = request.get_json()['message']

    # Generate a response using the vLLM model
    response = vllm.generate_response(message)

    # Return the response as JSON data
    return jsonify({'response': response})

# Define the static route to serve static files
@app.route('/static/<path:path>')
def static_files(path):
    """Serves static files."""

    return app.send_static_file(path)

# Run the application
if __name__ == '__main__':
    app.run()

import os
import sys
import logging
from flask import Flask, request, jsonify
#from flask_cors import CORS


#from serve import get_model_api


# define the app
app = Flask(__name__)
#CORS(app) # needed for cross-domain requests, allow everything by default

# load the model
#model_api = get_model_api()


# API route
@app.route('/api/audio', methods=['POST'])
def heartbeat_handler():
    """API function
    All model-specific logic to be defined in the get_model_api()
    function
    """
    input_data = request.json
    app.logger.debug("api_input: " + str(input_data))
    app.logger.debug("data type: " + input_data['type'])
    #output_data = model_api(input_data)
    output_data = {
                      "RestServer": "ali-id",
                      "quality": "good",
                      "process_t": "1467059712633",
                      "heart_rate_max": "100",
                      "heart_rate_min": "72",
                      "CAD_score": 75
                   }

    app.logger.debug("api_output: " + str(output_data))
    response = jsonify(output_data)
    return response


@app.route('/')
def index():
    return "Index API"

# HTTP Errors handlers
@app.errorhandler(404)
def url_error(e):
    return """
    Wrong URL!
    <pre>{}</pre>""".format(e), 404


@app.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    try:
        port=int(os.environ["HEARTBEAT_PORT"])
    except:
        port=8080;
    # This is used when running locally.
    app.run(host='0.0.0.0', port=port, debug=True)
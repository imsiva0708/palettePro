# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     input_data = request.form['input_data']
#     result = process_input(input_data)  # Call a function to process the input
#     return result  # Return the result directly

# def process_input(input_data):
#     # Process your input here
#     # For example, convert to uppercase
#     return input_data.upper()

# if __name__ == '__main__':
#     app.run(debug=True)


test = 'TEST'
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('result.html'
                           )

@app.route('/submit', methods=['POST'])
def submit():
    input_values = request.json  # Retrieve input values from JSON request
    print("Received inputs:", input_values)  # Print received inputs
    # Process input_values as needed
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
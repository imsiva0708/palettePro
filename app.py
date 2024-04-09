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


from flask import Flask, render_template, request, jsonify
from main import dictionarify

# dictRecommendations = [{'link': 'https://www.indianhealthyrecipes.com/palak-paneer-recipe-easy-paneer-recipes-step-by-step-pics/', 'title': "Palak Paneer Recipe (Indian Spinach Paneer) - Swasthi's Recipes", 'img': 'https://www.indianhealthyrecipes.com/wp-content/uploads/2021/06/palak-paneer.jpg.webp'}, {'link': 'https://www.indianhealthyrecipes.com/dosa-recipe-dosa-batter/', 'title': "Dosa Recipe, How to Make Dosa Batter - Swasthi's Recipes", 'img': 'https://www.indianhealthyrecipes.com/wp-content/uploads/2020/07/dosa-recipe.jpg.webp'}, {'link': 'https://www.indianhealthyrecipes.com/soft-idli-recipe-using-idli-rava/', 'title': "Idli Recipe (Idli Batter Recipe with Pro Tips) - Swasthi's Recipes", 'img': 'https://www.indianhealthyrecipes.com/wp-content/uploads/2021/06/idli.jpg.webp'},{'link': 'https://www.indianhealthyrecipes.com/palak-paneer-recipe-easy-paneer-recipes-step-by-step-pics/', 'title': "Palak Paneer Recipe (Indian Spinach Paneer) - Swasthi's Recipes", 'img': 'https://www.indianhealthyrecipes.com/wp-content/uploads/2021/06/palak-paneer.jpg.webp'}, {'link': 'https://www.indianhealthyrecipes.com/dosa-recipe-dosa-batter/', 'title': "Dosa Recipe, How to Make Dosa Batter - Swasthi's Recipes", 'img': 'https://www.indianhealthyrecipes.com/wp-content/uploads/2020/07/dosa-recipe.jpg.webp'}, {'link': 'https://www.indianhealthyrecipes.com/soft-idli-recipe-using-idli-rava/', 'title': "Idli Recipe (Idli Batter Recipe with Pro Tips) - Swasthi's Recipes", 'img': 'https://www.indianhealthyrecipes.com/wp-content/uploads/2021/06/idli.jpg.webp'},{'link': 'https://www.indianhealthyrecipes.com/palak-paneer-recipe-easy-paneer-recipes-step-by-step-pics/', 'title': "Palak Paneer Recipe (Indian Spinach Paneer) - Swasthi's Recipes", 'img': 'https://www.indianhealthyrecipes.com/wp-content/uploads/2021/06/palak-paneer.jpg.webp'}, {'link': 'https://www.indianhealthyrecipes.com/dosa-recipe-dosa-batter/', 'title': "Dosa Recipe, How to Make Dosa Batter - Swasthi's Recipes", 'img': 'https://www.indianhealthyrecipes.com/wp-content/uploads/2020/07/dosa-recipe.jpg.webp'}, {'link': 'https://www.indianhealthyrecipes.com/soft-idli-recipe-using-idli-rava/', 'title': "Idli Recipe (Idli Batter Recipe with Pro Tips) - Swasthi's Recipes", 'img': 'https://www.indianhealthyrecipes.com/wp-content/uploads/2021/06/idli.jpg.webp'},{'link': 'https://www.indianhealthyrecipes.com/palak-paneer-recipe-easy-paneer-recipes-step-by-step-pics/', 'title': "Palak Paneer Recipe (Indian Spinach Paneer) - Swasthi's Recipes", 'img': 'https://www.indianhealthyrecipes.com/wp-content/uploads/2021/06/palak-paneer.jpg.webp'}, {'link': 'https://www.indianhealthyrecipes.com/dosa-recipe-dosa-batter/', 'title': "Dosa Recipe, How to Make Dosa Batter - Swasthi's Recipes", 'img': 'https://www.indianhealthyrecipes.com/wp-content/uploads/2020/07/dosa-recipe.jpg.webp'}, {'link': 'https://www.indianhealthyrecipes.com/soft-idli-recipe-using-idli-rava/', 'title': "Idli Recipe (Idli Batter Recipe with Pro Tips) - Swasthi's Recipes", 'img': 'https://www.indianhealthyrecipes.com/wp-content/uploads/2021/06/idli.jpg.webp'}]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('result.html')

@app.route('/submit', methods=['POST'])
def submit():
    input_values = request.json  # Retrieve input values from JSON request
    print("Received inputs:", input_values)
    global dictRecommendations
    dictRecommendations = dictionarify(input_values)
    return None
    

@app.route("/result")
def result():
    return render_template('finalresult.html',
                           recommendations = dictRecommendations)

if __name__ == '__main__':
    app.run(debug=True)
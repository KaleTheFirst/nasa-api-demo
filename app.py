from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'GET':
        input = request.args['fname']
    else:
        input = request.form['fname']
    
    response = requests.get(f'https://fruityvice.com/api/fruit/{input}')
    data = response.json()
    # data = {
    # "genus": "Citrus",
    # "name": "Orange",
    # "id": 2,
    # "family": "Rutaceae",
    # "order": "Sapindales",
    # "nutritions": {
    #     "carbohydrates": 8.3,
    #     "protein": 1,
    #     "fat": 0.2,
    #     "calories": 43,
    #     "sugar": 8.2
    # }
    # }   
    return render_template('result.html' , data = data)


if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')
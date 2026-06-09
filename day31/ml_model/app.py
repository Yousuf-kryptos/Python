from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

with open("model.pkl","rb") as file:
    model = pickle.load(file)

mapping_dict = {'income':{0:'<=50k',1:'>50k'}}

@app.route('/')
def home():
    return  render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
    try:
        features = [
             int(request.form['age']),
            int(request.form['w_class']),
            int(request.form['edu']),
            int(request.form['martial_stat']),
            int(request.form['occup']),
            int(request.form['relation']),
            int(request.form['gender']),
            int(request.form['race']),
            int(request.form['c_gain']),
            int(request.form['c_loss']),
            int(request.form['hours_per_week']),
            int(request.form['native-country'])
        ]

        prediction = model.predict([features])[0]
        predicted_income = mapping_dict['income'][prediction]

        return render_template('index.html', prediction_text = f"Predicted Income:{predicted_income}")
    
    except Exception as e:
        return render_template('index.html', prediction_text =f"Error:{str(e)}")
    
if __name__ == '__main__':
    app.run(debug=True)
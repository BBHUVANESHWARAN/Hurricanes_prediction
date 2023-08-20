from flask import Flask, render_template, request
import pickle
import numpy as np

model1 = pickle.load(open(r'C:\Users\RETECH\Desktop\Project Code\hurricanes\LSTM_model1.pkl', 'rb'))  

app = Flask(__name__)  # initializing Flask app


@app.route("/",methods=['GET'])
def hello():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST': 
        d1 = request.form['T']
        d2 = request.form['TM']
        d3 = request.form['Tm']
        d4 = request.form['SLP']
        d5 = request.form['H']
        d6 = request.form['VV']
        d7 = request.form['V']
        d8 = request.form['VM']

        arr = np.array([[ d1,d2,d3,d4,d5,d6,d7,d8]])
        print([ d1,d2,d3,d4,d5,d6,d7,d8])
        pred1 = model1.predict(arr)
        print(pred1)
        if pred1<150:
            pred1="Hurricanes Detected"
            print("Hurricanes Detected")
        else:   
            pred1="No Hurricanes Detected"
            print("No Hurricanes Detected")


        

    return render_template('result.html',prediction_text1=pred1)
    
if __name__ == '__main__':
    app.run(debug=True)
    
#app.run(host="0.0.0.0")            # deploy
            # run on local system

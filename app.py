from flask import Flask ,request ,render_template ,url_for
import pickle
import numpy as np

app = Flask(__name__ ,static_url_path='/static')
model = pickle.load(open('model.pkl' ,'rb'))


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict' ,methods=['POST'])
def prediction():
    distance = int(request.form['distance'])
    age = int(request.form['age'])
    rate = float(request.form['rate'])
    features = np.array([[distance, age, rate]])
  
    predictions = model.predict(features)
   

    return render_template('index.html' , prediction_text='Delivery person will take {} mins'.format(round(predictions[0,0]),2))



if __name__=="__main__":
    app.run(debug=True)
import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
## Load the model
regmodel = pickle.load(open("reg_model.pkl","rb"))
scalar = pickle.load(open("scalar.pkl","rb"))

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/predict_api",methods=["POST"])
def predict_api():
    # Get form data from the request
    data = [float(x) for x in request.form.values()]
    print(data)
    new_data = np.array(data).reshape(1, -1)
    
    # Assuming scalar is pre-loaded or imported globally
    # new_data = scalar.transform(np.array(list(data.values())).reshape(1,-1))
    new_data = scalar.transform(new_data)
    output = regmodel.predict(new_data)
    
    return render_template("home.html", prediction_text="Predicted House Price: {}".format(output[0]))



if __name__=="__main__":
#	app.run(debug=True)
	app.run(host='0.0.0.0', port=5000, debug=True)


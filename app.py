import numpy as np
from flask import Flask, request, jsonify, render_template

import pickle

app = Flask(__name__)
run_with_ngrok(app)

model = pickle.load(open(file_path, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
	
    labels=['BATTERY NEGATIVE','BATTERY POSITIVE','CAMERA NEGATIVE','CAMERA POSITIVE','DISPLAY NEGATIVE','DISPLAY POSITIVE','PERFORMANCE NEGATIVE','PERFORMANCE POSITIVE',
        	'PRICE NEGATIVE','PRICE POSITIVE','SENSOR NEGATIVE','SENSOR POSITIVE']
    
    data = request.values.get ("Review")
    
    final=[]
    output=[]
    Ypredict = model.predict(data)
    predictions=Ypredict[0]
    #print(predictions)
    pred=[]
    pred=predictions[0]-1
   #print(pred)
    pred2=predictions[1]
  #print(pred2)
    list2=[pred,pred2]

#print(list(np.array(labels)[pred]))
    output=(list(np.array(labels)[list2]))
    final.append(output[0])
    print(final)

    

    return render_template('index.html', prediction_text='Aspect and Polarity should be 		{}'.format(final))


if __name__="__main__":
	app.run(debug=False)

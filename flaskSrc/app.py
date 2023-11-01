from flask import Flask, render_template,request

from prediction import get_prediction_from_model

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/predictionFromModel', methods=['GET', 'POST'])
def predictcion_from_model():
	"""
	This function helps to predict whether loan should
	be given or not for an applicant
	Parameter
	---------
		LIMIT_BAL
	    PAY_SEPT
	    BILL_AMT_MAY
	    BILL_AMT_APRIL
	    PAY_AMT_SEPT
	    PAY_AMT_JULY
	    PAY_AMT_JUNE
	    PAY_AMT_MAY
	    PAY_AMT_APRIL
	Returns 
	--------
		Prediction from model
	"""
	LIMIT_BAL = request.form.get("LIMIT_BAL")
	PAY_SEPT = request.form.get("PAY_SEPT")
	BILL_AMT_MAY = request.form.get("BILL_AMT_MAY")
	BILL_AMT_APRIL = request.form.get("BILL_AMT_APRIL")
	PAY_AMT_SEPT = request.form.get("PAY_AMT_SEPT")
	PAY_AMT_JULY = request.form.get("PAY_AMT_JULY")
	PAY_AMT_JUNE = request.form.get("PAY_AMT_JUNE")
	PAY_AMT_MAY = request.form.get("PAY_AMT_MAY")
	PAY_AMT_APRIL = request.form.get("PAY_AMT_APRIL")

	dict_test_data = {"LIMIT_BAL" : LIMIT_BAL,
					  "PAY_SEPT" : PAY_SEPT,
    				  "BILL_AMT_MAY" : BILL_AMT_MAY,
                      "BILL_AMT_APRIL" : BILL_AMT_APRIL,
                      "PAY_AMT_SEPT" : PAY_AMT_SEPT,
                      "PAY_AMT_JULY" : PAY_AMT_JULY,
                      "PAY_AMT_JUNE" : PAY_AMT_JUNE,
                      "PAY_AMT_MAY" : PAY_AMT_MAY,
                      "PAY_AMT_APRIL" :PAY_AMT_APRIL,
					}

	prediction = get_prediction_from_model(dict_test_data)
	return render_template('index.html', 
			prediction = str(prediction))
	"""
	if check_input(data_input):
		output = predict(data_input)
		return render_template('index.html', 
			prediction = str(output))
	else:
		return render_template('index.html', 
			prediction = str("Input should be integer"))
	"""

if __name__ == "__main__":
	app.run(host='127.0.0.1',port=5000,debug=True,threaded=True)

from os.path import join as join

from sklearn.ensemble import GradientBoostingClassifier

from catboost import CatBoostClassifier
from xgboost import XGBClassifier

import pickle

from preprocess_utils import *
from logging_utils import logger

datafiles_path = ".//..//dataFiles"

result_to_string = {1:"Credit Card Holder is default in next month", 
				    0:"Credit Card Holder is not default in next month"}


def load_model():
	"""
	This function helps to load the model
	Parameters
	----------
	None
	Returns
	--------
	model:object
	"""
	try:
		model_path = join(datafiles_path,
			"stacking_final_model.pkl")
		with open(model_path, "rb") as file_pointer:
			model = pickle.load(file_pointer)
		logger.info("model loaded successfully")
		return model
	except Exception as e:
		logger.error("Something went wrong while loading model "
                     + f": {e}", exc_info=True)
		raise e
	

def get_prediction_from_model(dict_input_data):
	"""
	This function gives prediction from model
	Parameters
	----------
	dict_input_data: dict()
				     keys will be column name 
				     and values will column value
	Returns
	-------
	Prediction:str
	"""
	model = load_model()
	dict_input_data = input_data_checker(dict_input_data)
	if dict_input_data:
		df = preprocess_data(dict_input_data)
		prediction = model.predict(df)[0]
		prediction = result_to_string[prediction]
		return prediction
	else:
		logger.warning("Invalid data type numeric type expected")
		return "invalid input type"


"""
dict_test_data = {
    "LIMIT_BAL" : 90000,
    "PAY_SEPT" : 0,
    "BILL_AMT_MAY" : 14948,
    "BILL_AMT_APRIL" : 15549,
    "PAY_AMT_SEPT" : 1518,
    "PAY_AMT_JULY" : 1000,
    "PAY_AMT_JUNE" : 1000,
    "PAY_AMT_MAY" : 1000,
    "PAY_AMT_APRIL" : 5000
}
print(get_prediction_from_model(dict_test_data))

"""
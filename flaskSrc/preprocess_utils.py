from os.path import join as join

import pandas as pd
import json

from logging_utils import logger

datafiles_path = ".//..//dataFiles"

def load_scaling_data():
	"""
	This function loads scaling params json file
	Parameters
	----------
	None
	Returns
	-------
	data : dict
		   Json loaded data
	"""
	try:
		json_file_path = join(datafiles_path,
			"minMaxScalingValues.json")
		with open(json_file_path,"r") as fp:
			data = json.load(fp)
		return data
	except Exception as e:
		logger.error("something went wrong while loading"
			+f"minMaxScalingValues.json file: {e}",exc_info=True)
		raise e

def min_max_scaler(column_name,value):
	"""
	This function helps to scale the data
	Parameters
	----------
	column_name: str
				 name of the column
	value: number
		   value want to be scaled
	Returns
	-------
	scaled_value: Number
	"""
	try:
		scaling_params = load_scaling_data()
		minimum = scaling_params[column_name]['min']
		maximum = scaling_params[column_name]['max']
		scaled_value = (value-minimum)/(maximum-minimum)
		return scaled_value
	except Exception as e:
		logger.error("something went wrong while normalizing"
			+f": {e}",exc_info=True)
		raise e
	
def preprocess_data(data_input):
	'''
	This function helps to preprocess the input
	Parameters
	----------
	data_input:dict()
	Returns
	--------
	data_input:pandas.dataframe
	'''
	try:
		list_columns = ["LIMIT_BAL","BILL_AMT_MAY",
		"BILL_AMT_APRIL","PAY_AMT_SEPT","PAY_AMT_JULY",
		"PAY_AMT_JUNE","PAY_AMT_MAY","PAY_AMT_APRIL"]
		for column_name in list_columns:
			data_input[column_name] = min_max_scaler(column_name,
				data_input[column_name])
		data_input = pd.DataFrame(data_input, 
			index = [0])
		logger.info("successfully completed preprocessing the inputs")
		return data_input
	except Exception as e:
		logger.error("something went wrong while preprocessing"
			+f"input : {e}",exc_info=True)
		raise e


def input_data_checker(dict_input_data):
	"""
	This function helps to check all
	input type is numeric or not
	Parameters
	----------
	dict_input_data:dict()
	Returns
	-------
	dict_input_data:dict()
					converted to all integer type
	"""
	try:
		for column_name, value in dict_input_data.items():
			dict_input_data[column_name] = int(value)
		logger.info("all inputs are in required format")
		return dict_input_data
	except ValueError as e:
		logger.error(f"inputs are not in numeric type : {e}",
			exc_info=True)
		return None
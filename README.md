# Credit-Card-Default-Classification

## Problem Statement
Financial threats are displaying a trend about the credit risk of commercial banks as the
incredible improvement in the financial industry has arisen. In this way, one of the biggest
threats faces by commercial banks is the risk prediction of credit clients.

## Dataset Information
The datasets has been provided by [Kaggle]. This dataset contains details of credit card holders in _Taiwan from April 2005 to September 2005_.

## Technical Details
The mainly divided into three parts
1. Exploratory Data Analysis:
           1. In this part we will get details of each feature using various visualization plots.
           2. And we will do preprocessing things like Treating Null values, Outliers detection and treatment, Scaling the features and Treating imbalanced dataset.
2. Model building and Evaluation:
           1. In this we will split dataset into two parts training and testing sets.
           2. We will use various algorithm KNN, Logistic Regression and all CART algorithms.
           3. Among all these models Gradient Boosting, Catboost, XGBoost performed well so we use these models for building stacking classifiers.
3. Deployment using Flask
           Here we will use HTML and CSS for designing UI and Flask for deploying model.

## Project Structure

```
├── dataFiles 
│   └── feature_importance.csv
│   └── minMaxScalingValues.json
│   └── preprocessed_dataset.csv
│   └── stacking_final_model.pkl
│   └── UCI_Credit_Card.csv
├── jupyterNotebook
│   └── ExploratoryDataAnalysis.ipynb
│   └── baseModelTraining.ipynb
│   └── model_params.py
│   └── modelTesting.ipynb
├── flaskSrc
│   └── static
│         └── indexx.css
│   └── templates
│         └── index.html
│   └── app.py
│   └── prediction.py
│   └── preprocess_utils.py
│   └── logging_utils.py
```
## Istallation

## Technologies Used

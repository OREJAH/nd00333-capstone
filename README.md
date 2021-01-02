#  CAPSTONE PROJECT

#  Table of Contents

## . Project Overview

## . Project Set Up

## . Dataset

   ### - Overview
   ### - Task
   ### - Access
   
## . Automated ML
           - Settings
           - Configuration

   ###  Results
   
## . Hyperparameter Tuning   
          - Model
          - Parameters
          
   ###  Results
   
## . Model Deployment

## . Screen Recording

## . Standout Suggestions
   
## Project overview

  This project will demonstrate my ability to use an external dataset in Azure workspace, train a model using the different tools available in the AzureML framework as well as my ability to deploy the model as a web service. I'll create a machine learning model that can assess the likelihood of a death by heart failure event. In this project, I will create two models: one using Automated ML (denoted as AutoML from now on) and one customized model whose hyperparameters are tuned using HyperDrive. I will then compare the performance of both the models and deploy the best performing model. I will lastly enable logging in my deloyed web app, this will log useful data about the requests being sent to the webapp including the inference time and the time at which the request arrived.

![workflow](https://github.com/OREJAH/nd00333-capstone/blob/master/starter_file/workflow.PNG)

### Project Set Up

•	Set up your workspace: Create a new workspace, if you haven’t already.

•	Set up your Azure Development Environment: Create a compute instance VM to run jupyter notebooks.

•	Download starter files: These files have some boilerplate code and TODOs that will help you start working on your project. You can find them in this link: https://github.com/udacity/nd00333-capstone/tree/master/starter_file

•	Choose a dataset:  Working with Kaggle heart failure dataset, it can be found in the link: https://www.kaggle.com/andrewmvd/heart-failure-clinical-data/download

Note: If you choose to work with any other external dataset, before choosing a task and dataset, make sure that it is supported by Azure ML's automl API.

•	Train a model using Automated ML: The automl.ipynb file contains a starter code to help you train a model using Automated ML. 

•	Train a model with HyperDrive: The hyperparameter_tuning.ipynb file contains some starter codes to help you train a model and perform hyperparameter tuning using HyperDrive.

•	Model Deployment: After you have trained your models. You will have to deploy your best model as a webservice and test the model endpoint.

## Dataset

### Overview

This is an analyzed dataset containing the medical records of 299 heart failure patients collected at the Faisalabad Institute of Cardiology and at the Allied Hospital in Faisalabad (Punjab, Pakistan), during April–December 2015. The patients consisted of 105 women and 194 men, and their ages range between 40 and 95 years old. All 299 patients had left ventricular systolic dysfunction and had previous heart failures that put them in classes III or IV of New York Heart Association (NYHA) classification of the stages of heart failure. As done by the original data curators, this dataset was represented as a table having 299 rows (patients) and 13 columns (features).

Cardiovascular diseases (CVDs) are the number 1 cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worlwide. Heart failure is a common event caused by CVDs and this dataset contains 12 features that can be used to predict mortality by heart failure. Most cardiovascular diseases can be prevented by addressing behavioural risk factors such as tobacco use, unhealthy diet and obesity, physical inactivity and harmful use of alcohol using population-wide strategies. People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help.

This heart failure dataset was gotten from kaggle's repository.

### Task

With the kaggle heart failure dataset I'll be using the knowledge I have obtained from the Machine Learning Engineer with Microsoft Azure Nanodegree Program to create a machine learning model that can assess the likelihood of a death by heart failure event. This can be used to help hospitals in assessing the severity of patients with cardiovascular disease. In this project, I will create two models: one using Automated ML (denoted as AutoML from now on) and one customized model whose hyperparameters are tuned using HyperDrive.

#### Features of the dataset

The dataset contains 13 features, which report clinical, body, and lifestyle information (Table 1), that we briefly describe here. Some features are binary: anaemia, high blood pressure, diabetes, sex, and smoking. The hospital physician considered a patient having anaemia if haematocrit levels were lower than 36%. Unfortunately, the original dataset manuscript provides no definition of high blood pressure.

Regarding the features, the creatinine phosphokinase (CPK) states the level of the CPK enzyme in blood. When a muscle tissue gets damaged, CPK flows into the blood. Therefore, high levels of CPK in the blood of a patient might indicate a heart failure or injury. The ejection fraction states the percentage of how much blood the left ventricle pumps out with each contraction. The serum creatinine is a waste product generated by creatine, when a muscle breaks down. Especially, doctors focus on serum creatinine in blood to check kidney function. If a patient has high levels of serum creatinine, it may indicate renal dysfunction. Sodium is a mineral that serves for the correct functioning of muscles and nerves. The serum sodium test is a routine blood exam that indicates if a patient has normal levels of sodium in the blood. An abnormally low level of sodium in the blood might be caused by heart failure. The death event feature, that we use as the target in our binary classification study, states if the patient died or survived before the end of the follow-up period, that was 130 days on average. The original dataset article unfortunately does not indicate if any patient had primary kidney disease, and provides no additional information about what type of follow-up was carried out. Regarding the dataset imbalance, the survived patients (death event = 0) are 203, while the dead patients (death event = 1) are 96. In statistical terms, there are 32.11% positives and 67.89% negatives.

### Access

I downloaded the Heart Failure Dataset from kaggle as a csv file, then i registered it in the Azure Workspace under Dataset as a Tabular dataset. Then uploaded it from the local files in my system. I also made it accessible in the jupyter notebook by using the code: dataset= Dataset.get_by_name(ws, name="heart-failure).

![access dataset](https://github.com/OREJAH/nd00333-capstone/blob/master/starter_file/heart%20failure%20dataset.PNG)

### Automated ML
TODO: Give an overview of the automl settings and configuration you used for this experiment

### Results
TODO: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

TODO Remeber to provide screenshots of the RunDetails widget as well as a screenshot of the best model trained with it's parameters.

### Hyperparameter Tuning

I chose a custom-coded model — a standard Scikit-learn Logistic Regression for this experiment. Logistic Regression is a classification algorithm that is used to predict the probability of a categorical dependent variable. In the case of this capstone experiment, I chose the model because the decision boundary of logistic regression model is a linear binary classifier that seperate the two classes I want to predict using a hperdrive service.

The parameters I used for the hyperparameter search are:

Regularization Strength (C) with range 0.1 to 1.0 -- Inverse of regularization strength. Smaller values cause stronger regularization
Max Iterations (max_iter) with values 50, 100, 150 and 200 -- Maximum number of iterations to converge.

![parameters](https://github.com/OREJAH/nd00333-capstone/blob/master/starter_file/hyperparameters.PNG)
![run in progress](https://github.com/OREJAH/nd00333-capstone/blob/master/starter_file/hyperdrive%20widgets%20in%20progress.PNG)
![run completed](https://github.com/OREJAH/nd00333-capstone/blob/master/starter_file/hyperdrive%20widget.PNG)

### Results

The best hyperparameters for the hyperdrive model is:

'Regularization Strength: ': 0.05203245378731211

'Max iterations: ': 75

This hyperparameters generated an accuracy of  0.7833333333333333 for the hyperdrive model.

I could have improved the model through the use of Bayesian optimization algorithm that allows for the use of a different kind of statistical technique to improve the kind of hyperparameter. It picks samples based on how previous samples performed, so that new samples improve the primary metric and its search is potentially efficient.

![hyperdrive_best_id](https://github.com/OREJAH/nd00333-capstone/blob/master/starter_file/HYPERDRIVE%20BEST_RUN_ID.PNG)


Model Deployment
TODO: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

Screen Recording
TODO Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

A working model
Demo of the deployed model
Demo of a sample request sent to the endpoint and its response
Standout Suggestions
TODO (Optional): This is where you can provide information about any standout suggestions that you have attempted.

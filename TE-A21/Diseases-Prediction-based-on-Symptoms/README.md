# Disease Prediction Based on Symptoms

![Disease Prediction Basaed on Symptoms]

## Overview

The core of this project lies in a Jupyter Notebook, [Disease Prediction based on Symptoms.ipynb](Disease_Prediction_based_on_symptoms.ipynb). This notebook utilizes a Random Forest Classifier (RFC) to make accurate predictions about diseases based on a set of symptoms.

## Table of Contents

1. [Introduction](#introduction)
2. [Exploratory Data Analysis (EDA)](#eda)
   - [1. Import Dependencies](#dependencies)
   - [2. Load the Dataset](#load-dataset)
   - [3. Statistical Details](#statistical-details)
   - [4. Convert Categorical Data](#convert-categorical)
   - [5. Handle Missing Values](#handle-missing)
   - [6. Symptoms Severity](#symptoms-severity)
   - [7. Split Dataset](#split-dataset)
3. [Model Selection](#model-selection)
   - [1. Random Forest Classifier](#random-forest)
   - [2. Neural Network (MLPClassifier)](#neural-network)
4. [Evaluate Models](#evaluate-models)
   - [1. Random Forest Classifier Evaluation](#evaluate-rfc)
   - [2. Neural Network (MLPClassifier) Evaluation](#evaluate-mlpc)
5. [Save Model](#save-model)
6. [Test the Model Manually](#test-manually)
7. [Symptom Input](#symptom-input)
8. [Usage with App.py](#usage-with-app)

## Introduction <a name="introduction"></a>

Discover how machine learning can revolutionize disease prediction. The RFC model achieves an outstanding 99% accuracy, making it a reliable tool for healthcare professionals and enthusiasts alike.

## Exploratory Data Analysis (EDA) <a name="eda"></a>

Explore the step-by-step process of preparing the data, training the model, and evaluating its performance.

### 1. Import Dependencies <a name="dependencies"></a>

Import the necessary libraries and modules for data analysis and model implementation.

### 2. Load the Dataset <a name="load-dataset"></a>

Load the dataset from a CSV file containing information about various diseases and their associated symptoms.

- [Dataset.csv](Dataset/dataset.csv) <-- (Take a look on data, used to build this model)

<div style="display: flex;">
</div>

### 3. Statistical Details <a name="statistical-details"></a>

Understand the dataset better with statistical details, including mean, standard deviation, and quartiles.


### 4. Handle Missing Values <a name="handle-missing"></a>

Handle missing values in the dataset by replacing them with zeros.


### 5. Symptoms Severity <a name="symptoms-severity"></a>

Encode symptoms severity using a separate dataset for training the model. This Dataset assign the respective weight to each Symptoms.


With the help of this data, we will encode our original dataset.

### 6. Convert Categorical Data <a name="convert-categorical"></a>

Convert categorical data into numerical format using Severity dataset, ensuring consistency.
- Dataset after converting Categorical Data into Numerical Data.
- Now, its Ready to train the models.

<div style="display: flex;">
</div>

### 7. Split Dataset <a name="split-dataset"></a>
Firstly, Splits the Clean Dataset into Training data and Label data.


Then, it time to split the dataset into training and testing sets for model training and evaluation, using module `train_test_spilt`.

## Model Selection <a name="model-selection"></a>

### 1. Random Forest Classifier (RFC) <a name="random-forest"></a>

Train and evaluate the RFC model, achieving an impressive accuracy of 99%.

### 2. Neural Network (MLPClassifier) <a name="neural-network"></a>

Implement and evaluate a Multi-Layer Perceptron (MLP) Classifier with a similar accuracy of 99%.

## Evaluate Models <a name="evaluate-models"></a>

Detailed classification reports are provided for both the Random Forest Classifier and the MLPClassifier.

### 1. Random Forest Classifier Evaluation <a name="evaluate-rfc"></a>

Precision, recall, and accuracy scores showcase the effectiveness of the Random Forest Classifier.
 - Accuracy Proof:
<div style="display: flex;">
</div>

### 2. Neural Network (MLPClassifier) Evaluation <a name="evaluate-mlpc"></a>

Metrics calculated for the MLPClassifier demonstrate its comparable performance.
- Accuracy Proof:
<div style="display: flex;">
</div>

## Save Model <a name="save-model"></a>

- Save the trained Random Forest Classifier model using the joblib library for future use.
- Used Python library `joblib`.


## Test the Model Manually <a name="test-manually"></a>

Manually test the model with a sample set of symptoms, demonstrating its predictive capability.

<div style="display: flex;">
</div>

## Symptom Input <a name="symptom-input"></a>

- Capture user input for specific symptoms to predict the associated disease.

<div style="display: flex;">
</div>

## Usage with App.py <a name="usage-with-app"></a>

Utilize the [app.py](app.py) file to allow outsiders to use the model on their local machines. This file enables seamless interaction with the model, providing a user-friendly interface.

Prerequisites: 
- Load [dataset.csv](Dataset/dataset.csv)
- Load  [Severity-Symptom.csv](Dataset/Symptom-severity.csv) 
- Load model `model_RFC.joblib` (Replace 'model_RFC.joblib' with your model name)

 [app.py](app.py).

---

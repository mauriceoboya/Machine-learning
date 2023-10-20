# Machine-learning
Machine learning is a branch of computer science in which machines learn and make predictions without explicit programming. It is divided into three categories: supervised, unsupervised, and reinforcement learning. In this project, we will engage in hands-on projects that encompass all three of these categories.

## Supervised Learning

# Credit Card Approval Prediction

This project focuses on predicting credit card approval decisions based on various features using machine learning techniques. It involves data preprocessing, missing value imputation, and the application of classification algorithms.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Data Cleaning](#data-cleaning)
- [Handling Missing Values](#handling-missing-values)
- [Machine Learning Models](#machine-learning-models)
- [Results](#results)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The objective of this project is to predict whether a credit card application will be approved or denied based on various customer attributes. We perform data cleaning, handle missing values, and apply machine learning models to make predictions.

## Dataset

The dataset used in this project is named 'cc_approvals.csv' and contains the following columns:

- Gender
- Age
- Debt
- Married
- BankCustomer
- EducationLevel
- Ethnicity
- YearsEmployed
- PriorDefault
- Employed
- CreditScore
- DriversLicense
- Citizen
- ZipCode
- Income
- ApprovalStatus

## Data Cleaning

- Cleaned and transformed the data to make it suitable for machine learning.
- Handled missing values by using K-Nearest Neighbors (KNN) imputation.
- Encoded categorical variables to numerical values.

## Handling Missing Values

Missing values are common in datasets. To address this issue, we used the K-Nearest Neighbors (KNN) imputer to impute missing values in the dataset.

## Machine Learning Models

We applied two classification models for credit card approval prediction:

1. **K-Nearest Neighbors (KNN):**
   - Trained a KNN classifier to predict approval status.
   - Evaluated the model's performance using classification reports.

2. **Logistic Regression:**
   - Trained a Logistic Regression model to predict approval status.
   - Evaluated the model's performance using classification reports.

3. ** Naive-Bayes Classifier:**
   -Bayes' theorem is a fundamental concept in probability theory, often used in various fields, including machine learning and statistics. It describes how to    update the probability for a hypothesis based on new evidence. The formula for Bayes' theorem is as follows:
   
  $P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$
Where:
- \(P(A|B)\) is the probability of event A occurring given that event B has occurred.
- \(P(B|A)\) is the probability of event B occurring given that event A has occurred.
- \(P(A)\) is the prior probability of event A.
- \(P(B)\) is the prior probability of event B.

   - Trained a navie bayes model to predict approval status.
   - Evaluated the model's performance using classification reports.

## Results

The project provides insights into credit card approval prediction using machine learning techniques. It demonstrates the importance of data preprocessing and imputation of missing values for accurate predictions.

## Usage

To use this code, follow these steps:

1. Clone the repository: `git clone https://github.com/mauriceoboya/machine-learning.git`
2. Navigate to the project directory: `cd machine-learning`
3. Run the code in your preferred Python environment.

Make sure to have the required libraries installed in your environment.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify the README according to your project's specific needs. Add sections, explanations, or any other information that you think would be helpful for users and contributors.

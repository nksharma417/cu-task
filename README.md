# Student Career Recommendation System Using AI

## Project Overview

The Student Career Recommendation System is an Artificial Intelligence based application that predicts suitable career options for students based on their academic background, skills, interests, personality, and preferences.

The system uses Machine Learning classification algorithms to analyze student profiles and recommend a suitable career path.

## Features

- Student profile based career prediction
- Uses academic details like 10th marks, 12th marks, stream, degree, and CGPA
- Considers skills and interests
- Machine Learning based prediction
- Interactive Streamlit web interface
- Multiple ML models tested and compared

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

## Machine Learning Models Used

The following classification algorithms were tested:

- Decision Tree Classifier
- Random Forest Classifier
- Extra Trees Classifier
- Gradient Boosting Classifier
- K-Nearest Neighbors Classifier

Random Forest Classifier was selected as the final model because it achieved the highest accuracy.

## Dataset

The dataset was generated using rule-based synthetic data.

It contains student information such as:

- Age
- 10th Percentage
- 12th Percentage
- Stream
- Degree
- CGPA
- Programming Skill
- Communication Skill
- Leadership
- Creativity
- Problem Solving
- Career Interests
- Personality
- Hobby

Total records: 5550 students

## Project Workflow

1. Generate student career dataset
2. Perform data preprocessing
3. Encode categorical features
4. Split data into training and testing sets
5. Train multiple classification models
6. Compare model performance
7. Select the best model
8. Deploy using Streamlit

## Model Accuracy

Final model performance:

Random Forest Accuracy: ~78%

## Project Structure

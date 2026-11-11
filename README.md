# Equipment Failure Prediction

## Project Overview

This project uses Machine Learning to predict whether industrial equipment is likely to experience a failure based on sensor data.

The goal is to support predictive maintenance by identifying potential equipment failures before they occur.

## Problem Statement

Unexpected machine failures can cause production downtime, maintenance costs, and operational losses.

This project uses historical machine sensor readings to predict machine failure.

## Dataset

- Dataset: AI4I 2020 Predictive Maintenance Dataset
- Total records: 10,000
- Total columns: 14
- Target variable: Machine failure

### Features Used

- Machine Type
- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- FastAPI
- Pydantic
- Joblib
- Pytest
- Docker

## Machine Learning Model

Random Forest Classifier was used for machine failure prediction.

The model includes:
- Numerical feature scaling using StandardScaler
- Categorical feature encoding using OneHotEncoder
- Class balancing using `class_weight="balanced"`
- Train-test split with stratification

## Model Performance

Evaluation results on the test dataset:

| Metric | Score |
|---|---:|
| Accuracy | 97.95% |
| Precision | 72.13% |
| Recall | 64.71% |
| F1 Score | 68.22% |
| ROC-AUC | 96.12% |

Note: Accuracy alone does not represent failure detection performance. Recall and precision are also important because missed failures can be costly.

## Project Structure

```text
equipment-failure-prediction/
|-- data/
|   |-- raw/
|   |-- processed/
|-- notebooks/
|-- src/
|   |-- equipment_failure/
|-- api/
|-- models/
|-- reports/
|   |-- figures/
|-- sql/
|-- tests/
|-- Dockerfile
|-- docker-compose.yml
|-- requirements.txt
|-- README.md
```

##
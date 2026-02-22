# Loan Approval Predictor

A machine learning model that predicts whether a loan will be approved or rejected based on applicant details.

## Dataset
- Source: [Kaggle](https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset)
- 4269 records, 13 columns

## Models Used
| Model | Accuracy |
|-------|----------|
| Logistic Regression | 80% |
| Random Forest | 98% |

Random Forest was chosen as the final model due to significantly better performance, especially on detecting rejections.

## Features Used
- Number of dependents, Education, Self employed status
- Income, Loan amount, Loan term
- CIBIL score, Residential/Commercial/Luxury/Bank assets

## How to Run
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Open `loan_prediction.ipynb` in Jupyter
4. Run all cells

## Limitations
- Trained on Kaggle data, real-world performance may vary
- Model may need retraining on newer, diverse data for production use

## License
MIT

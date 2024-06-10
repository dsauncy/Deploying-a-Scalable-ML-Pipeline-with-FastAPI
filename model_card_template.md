# Model Card

## Model Details
• Model name / type: Logistic Regression

• Model purpose: To predict salary range based on categorical features.

• Dataset: publicly available Census Bureau data (census.csv)
https://archive.ics.uci.edu/dataset/20/census+income
• Developed by Douglas Sauncy, a student at Western Governors University.  Version 1.0.  06/2024


## Intended Use
• Intended to be used for predicting whether an individual makes more or less than 50k

• Not intended for gambling purposes.

## Training Data
• Dataset: https://archive.ics.uci.edu/dataset/20/census+income

• Data includes the following 14 features:
age,
workclass,
fnlwgt,
education,
education-num,
marital-status,
occupation,
relationship,
race,
sex.

The training data will be 80% of the overall data.

## Evaluation Data
The evaluation data will be 20% of the overall data.

## Metrics
• The model's performance was evaluated using the Precision, Recall, and F-1 score as metrics:
Precision: 0.7101 | Recall: 0.2683 | F1: 0.3895

## Ethical Considerations
• This model was created for educational and training purposes only.

• This model may contain personal data which must be treated with privacy and anonymity in mind.

## Caveats and Recommendations
• Feature bias can arise from data imbalances in some features.  Continuous monitoring and adjustments are recommended to mitigate the problem.
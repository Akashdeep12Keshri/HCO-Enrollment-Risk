# Health & Welfare Enrollment Risk Prediction

## Business Context
Health & Welfare (HCO/H&W) operations support US employees during benefit
enrollments, elections, and life events. Missed enrollments lead to escalations,
manual corrections, and SLA breaches.

Due to confidentiality of real Health & Welfare data, this project uses an
enterprise HR dataset as a proxy to simulate enrollment behavior using
domain-driven assumptions.

---

## Objective
- Predict employees at high risk of missing benefit enrollment
- Enable proactive outreach by operations teams
- Reduce enrollment-related escalations and SLA violations

---

## Dataset
**IBM HR Analytics Employee Attrition Dataset (Kaggle)**

Mapped to Health & Welfare domain using business logic:

| HR Attribute | HCO Interpretation |
|-------------|-------------------|
| MonthlyIncome | Benefit affordability |
| JobLevel | Plan eligibility tier |
| YearsAtCompany | Enrollment familiarity |
| OverTime | Enrollment risk indicator |
| WorkLifeBalance | Engagement level |
| JobSatisfaction | Enrollment attentiveness |

---

## Feature Engineering
- Income Band (Low / Medium / High)
- Tenure Bucket (New Hire / Mid / Long)
- Engagement Score
- Overtime Risk Flag
- Simulated Enrollment Risk (Target Variable)

---

## Model
- Algorithm: **XGBoost Classifier**
- Metric Focus: **Recall & ROC-AUC**
- ROC-AUC: ~0.85 (varies by run)

---

## Business KPIs
- High-risk population identification
- Estimated reduction in missed enrollments
- Improved SLA adherence
- Reduced manual corrections

---

## Deployment
- Model persisted using pickle
- Streamlit application for ops users
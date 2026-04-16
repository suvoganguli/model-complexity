# Feature Engineering vs Model Complexity

This project explores a simple question:

> How far can a basic model go when the feature representation improves?

The focus is on predicting next-day electricity demand using different models and feature sets, and understanding the interaction between **feature engineering** and **model capability**.

---

## Motivation

Temperature is an obvious predictor of electricity demand. However, adding it directly to a linear model did not lead to significant improvement.

This raised a deeper question:

- Is the model too simple?
- Or is the feature representation insufficient?

---

## Approach

Three models are evaluated:

- Linear Regression
- Random Forest
- Gradient Boosting

Each model is tested under different feature configurations:

- Without temperature
- With temperature
- With engineered temperature features (e.g. quadratic term)

The goal is not to optimize performance, but to understand:

- how models use information
- where simple models break down
- how far feature engineering can go

---

## Key Observations

- Adding temperature alone provides limited benefit to linear models.
- Nonlinear models are able to leverage temperature more effectively.
- Introducing a quadratic temperature feature significantly improves the linear model.
- However, a performance gap remains compared to nonlinear models.

---

## Insight

The temperature–demand relationship is:

- nonlinear
- asymmetric
- influenced by interactions with other variables

A single global transformation (such as a quadratic term) captures the dominant structure, but not all of it.

This leads to a broader conclusion:

> Feature engineering can extend the usefulness of simple models, but cannot fully replace model flexibility when the underlying system is complex.

---


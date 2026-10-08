# Task 1.2 – Logistic Regression from Scratch

Predicting whether a criminal case is **closed** using logistic regression implemented from scratch with NumPy (no ML libraries).

---

## Problem Statement

Given `crime_train.csv`, train a logistic regression model to predict whether a case is closed (`Yes` / `No`), then evaluate it on `crime_test.csv`. The test file is never used for training. The evaluation metric is accuracy.

## Dataset

| File | Rows | Notes |
|---|---|---|
| `crime_train.csv` | 22,489 | 12 columns, target is `closed` |
| `crime_test.csv` | 9,639 | Same columns |

Columns include `city`, `area`, `crime_description`, `age`, `sex`, `weapon`, `domain`, `police_department`, `case_filed` (date and time), plus two ID columns.

## Approach

### 1. Data preparation
- Target: `closed` mapped to `Yes = 1`, `No = 0`.
- Missing `weapon` values (the only missing data) are treated as their own category, `None`.
- `case_filed` is split into hour, month, year and weekday.
- Text columns (`city`, `crime_description`, `sex`, `weapon`, `domain`) are one-hot encoded, built on train and test together so both have identical columns.
- ID columns (`Unnamed: 0`, `Num`) are dropped.

### 2. Feature scaling
Standardized with the training set's mean and standard deviation only, and the same values reused on the test set to avoid data leakage.

### 3. Model
A bias column of ones is added, and the prediction is a probability:

```
z = X · w
p = sigmoid(z) = 1 / (1 + e^(-z))
```

A case is predicted as closed when `p >= 0.5`.

### 4. Training (batch gradient descent)
- **Loss (log loss):** `J(w) = -(1/m) · Σ [ y·log(p) + (1 − y)·log(1 − p) ]`
- **Gradient:** `∇J = (1/m) · Xᵀ (p − y)`
- **Update:** `w = w − α · ∇J`
- Learning rate `α = 0.1`, `1000` epochs, weights initialised to zero.

### 5. Evaluation metric
Accuracy: the percentage of cases where the predicted class matches the real one.

## Results

| Metric | Value |
|---|---|
| Final loss | ~0.692 |
| Train accuracy | ~51.6 % |
| Test accuracy | ~49.2 % |

Train and test accuracy are printed for every epoch in the notebook, along with the loss-vs-epoch plot.

### Observation
Accuracy stays close to 50 % because the dataset carries almost no signal for the target:
- The two classes are balanced at about 50 / 50, so always guessing one class also scores about 50 %.
- Every category (city, crime type, weapon, age group) has a closed rate between roughly 47 % and 54 %, and no numeric column correlates with `closed` (correlations below 0.005).
- A stronger non-linear model (gradient boosting) also scored about 49 % on the test set.
- The loss of about 0.692 equals ln 2, the loss of predicting 50 / 50 for every case.

The result therefore reflects the data, not an error in the implementation.

## Libraries Used
- **NumPy** – matrix operations
- **Pandas** – reading and preparing data
- **Matplotlib** – plotting the loss curve


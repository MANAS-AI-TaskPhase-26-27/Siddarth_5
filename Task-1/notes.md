# Task 1.1 – Linear Regression from Scratch

Predicting the daily **Close price** of a stock using linear regression implemented from scratch with NumPy (no ML libraries).

---

## Problem Statement

Given `train.csv`, train a linear regression model to predict the `close` price, then evaluate it on `test.csv`. The test file is never used for training.

## Dataset

| File | Rows | Notes |
|---|---|---|
| `train.csv` | 283,085 | 19 columns, includes `close` (target) |
| `test.csv` | 177,063 | Same columns, different order |

Columns include `open`, `high`, `low`, `volume`, and several numeric indicators (`momentum_index`, `beta_indicator`, `risk_premium`, `alpha_signal`, etc.), plus `date`, `index` and `symbols`.

## Approach

### 1. Data cleaning
- Removed duplicate rows and rows with missing values from the training set.
- Dropped test rows with a missing `close` (cannot be scored).
- Filled remaining missing test features with the **training** column means.
- Dropped `date`, `index` (row ID) and `symbols` (text label); the remaining 15 numeric columns are the features.

### 2. Feature scaling
Standardized every feature: `x = (x - mean) / std`. Mean and std come from the training set only and are reused on the test set to avoid data leakage.

### 3. Model
A bias column of ones is added, so the prediction is:

```
ŷ = X · w
```

### 4. Training (batch gradient descent)
- **Cost:** `J(w) = (1 / 2m) · Σ (ŷ − y)²`
- **Gradient:** `∇J = (1 / m) · Xᵀ (ŷ − y)`
- **Update:** `w = w − α · ∇J`
- Learning rate `α = 0.1`, `1000` epochs, weights initialised to zero.

### 5. Evaluation metric
Accuracy is reported as the **R² score (%)**:

```
R² = 1 − Σ(y − ŷ)² / Σ(y − ȳ)²
```

Percentage-error metrics (MAPE) were avoided because `close` can be exactly 0.

## Results

| Metric | Value |
|---|---|
| Final cost | ~18.4 |
| Train accuracy (R²) | ~99.35 % |
| Test accuracy (R²) | ~96.2 % |

The cost drops steeply in the first few epochs and then flattens, showing convergence. Training and test accuracy are printed for every epoch in the notebook, along with the cost-vs-epoch plot.

## Libraries Used
- **NumPy** – matrix operations
- **Pandas** – reading and cleaning data
- **Matplotlib** – plotting the cost curve



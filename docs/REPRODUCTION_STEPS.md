# Full Reproduction Steps

## Step 1: Dataset Preparation
- Download NSL-KDD
- Download CSIC-2010
- Place in data directory

---

## Step 2: Preprocessing
python preprocessing/data_pipeline.py

---

## Step 3: Training
python models/train_models.py

---

## Step 4: Evaluation
python evaluation/metrics.py

---

## Step 5: SDN Deployment
ryu-manager sdn/controller.py

---

## Expected Results

- Accuracy
- Precision
- Recall
- F1-score
- ROC Curve
- PR Curve

---

## Reproducibility

All experiments are reproducible using:
- Provided scripts
- Same preprocessing
- Same hyperparameters
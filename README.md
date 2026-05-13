# SQL Injection Detection in SDN using Hybrid CNN–KNN Model

## Overview
This repository provides a hybrid CNN–KNN based framework for SQL injection detection in Software-Defined Networking (SDN).

The system uses a cross-layer approach:
- NSL-KDD dataset for network-level anomaly detection
- CSIC-2010 dataset for SQL injection detection

---

## Repository Structure

- preprocessing/ → Data cleaning and normalization
- models/ → CNN, KNN, Hybrid model training
- evaluation/ → Metrics and ROC/PR curves
- sdn/ → SDN controller (Ryu)
- docs/ → Setup and reproducibility documentation

---

## Requirements

Install dependencies:
pip install -r requirements.txt

---

## Execution Steps

### Step 1: Preprocessing
python preprocessing/data_pipeline.py

### Step 2: Model Training
python models/train_models.py

### Step 3: Evaluation
python evaluation/metrics.py

### Step 4: SDN Deployment
ryu-manager sdn/controller.py

---

## Reproducibility Details

- Same preprocessing pipeline across experiments
- 10-fold cross-validation applied
- Fixed random seed
- Hyperparameters defined in scripts

---

## Dataset Information

### NSL-KDD
- Network-level intrusion detection

### CSIC-2010
- SQL injection detection dataset

---

## Output

- Accuracy, Precision, Recall
- F1-score
- ROC Curve
- Precision-Recall Curve
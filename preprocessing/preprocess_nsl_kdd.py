
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess(input_path, output_path):
    df = pd.read_csv(input_path)
    df = df.dropna()

    scaler = MinMaxScaler()
    numeric_cols = df.select_dtypes(include=['int64','float64']).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    df.to_csv(output_path, index=False)
    print("NSL-KDD preprocessing complete.")

if __name__ == "__main__":
    preprocess("../data/raw/NSL_KDD/KDDTrain+.txt",
               "../data/processed/nsl_kdd_processed.csv")

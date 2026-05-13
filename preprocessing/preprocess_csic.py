
import pandas as pd

def preprocess(input_path, output_path):
    df = pd.read_csv(input_path)
    df = df.dropna()
    df['length'] = df['request'].apply(len)
    df.to_csv(output_path, index=False)
    print("CSIC preprocessing complete.")

if __name__ == "__main__":
    preprocess("../data/raw/CSIC_2010/csic.csv",
               "../data/processed/csic_processed.csv")

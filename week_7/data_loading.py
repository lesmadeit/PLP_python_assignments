from ucimlrepo import fetch_ucirepo
import pandas as pd

def load_dataset():
    """
    Fetches the Iris dataset from UCI ML repository and combines features and targets into a single DataFrame.
    """
    # Fetch dataset
    iris = fetch_ucirepo(id=53)
    
    # Combine features and targets into one DataFrame
    df = pd.concat([iris.data.features, iris.data.targets], axis=1)
    
    return df, iris.metadata, iris.variables

def clean_dataset(df):
    """
    Cleans the dataset by handling missing values.
    """
    # Check for missing values
    if df.isnull().sum().any():
        print("Missing values detected. Filling them with column mean...")
        df.fillna(df.mean(), inplace=True)
    else:
        print("No missing values detected.")
    return df

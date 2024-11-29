from ucimlrepo import fetch_ucirepo
import pandas as pd

def load_data():
    iris = fetch_ucirepo(id=53)
    X = iris.data.features
    y = iris.data.targets
    df = pd.concat([X, y], axis=1)
    return df, iris

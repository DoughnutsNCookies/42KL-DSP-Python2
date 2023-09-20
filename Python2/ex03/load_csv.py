import pandas as pd


def load(path: str):
    """
    Load a csv file into a pandas dataframe.
    """
    try:
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception as err:
        print(err)
        return None

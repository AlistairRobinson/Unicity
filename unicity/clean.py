import pandas as pd

def date_resolution(start: pd.DataFrame, end: pd.DataFrame, resolution: str):
    time = (end - start) / 2 + start
    return time.apply(lambda x: pd.Timestamp(x).round(resolution))
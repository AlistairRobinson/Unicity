import pandas as pd

def date_resolution(start: pd.DataFrame, end: pd.DataFrame, res: str):
    time = (end - start) / 2 + start
    return time.apply(lambda x: pd.Timestamp(x).round(res))

def clean_data(data: pd.DataFrame, res: str):
    data["time"] = date_resolution(data["start time"], data["end time"], res)
    data = data.drop(["start time", "end time", "month", "date"], axis=1)
    return data.drop_duplicates(subset=["user id", "time"])
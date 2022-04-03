import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


def refactor_data_frame(df: 'pd.DataFrame') -> 'pd.DataFrame':
    """
    Function to incorporate all the modifications on the Zepp/MiFit
    dataframe.
    The following are the principal modifications:
        - Refactor of the name type
        - Modify the time value for each value
            - Our current time is more detailed. The important information is based on minutes; no more!
            - YYYY-MM-DD HH-MM
    :param df: 'pd.DataFrame'
    :return: df: 'pd.DataFrame'
    """
    namesOfWorkout: 'dict' = {1: "Running",
                              16: "Freestyle",
                              21: "Jump Rope"}
    df['type'] = df['type'].replace(namesOfWorkout)
    df['startTime'] = pd.to_datetime(df['startTime']) \
        .dt.tz_convert("America/Mexico_City") \
        .apply(lambda x: x.strftime('%Y-%m-%d %H:%m:%s')) \
        .apply(lambda x: ":".join(x.split(":")[:2])) \
        .apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M'))

    return df


def read(path: 'str' = 'sport') -> 'pd.DataFrame':
    """
    Function to read and cast all the important information of the csv file.
    This is the following format of Zepp/MiFit

    Columns:
         - 'type', it is the type of workout
            - 1 -> Running
            - 16 -> Freestyle
            - 21 -> Jump rope
         - 'startTime', it is the time of init. The format is 'YYYY-MM-DD HH:MM:SS'
         - sportTime(s)', the time duration of the session
         - 'distance(m)',
         - 'calories(kcal)'

         The following depends on the exercises type.
         - 'minPace(/meter)',
         - 'avgPace(/meter)',


    :param path: str
    :return: pd.Dataframe
    """
    # TODO: Add a simple function to read the unique csv file in the folder.
    df = pd.DataFrame()
    if path == 'sport':
        df = pd.read_csv('data/sport/SPORT_1648939638346.csv')
    else:
        df = pd.read_csv(path)

    refactor_data_frame(df)

    return df


if __name__ == '__main__':
    pass

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime

#import zeppanalysis.util.
#import zeppanalysis.util
# import zeppanalysis.util as utilZepp
# from zeppanalysis.util import pd
#from ..util.files import get_path_first_file_by_prefix
#from ..util.files import pd
from zeppanalysis.util import files



NAME_RECORD: 'str' = "SPORT"
NAMES_TYPE_WORKOUT: 'dict' = {1: "Running",
                              16: "Freestyle",
                              21: "Jump Rope"}


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
    df['type'] = df['type'].replace(NAMES_TYPE_WORKOUT)
    df['startTime'] = pd.to_datetime(df['startTime']) \
        .dt.tz_convert("America/Mexico_City") \
        .apply(lambda x: x.strftime('%Y-%m-%d %H:%m:%s')) \
        .apply(lambda x: ":".join(x.split(":")[:2])) \
        .apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M'))

    return df


def get_data(path: 'str' = None) -> 'pd.DataFrame':
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
    if path is None:
        df = pd.read_csv(files.get_path_first_file_by_prefix(NAME_RECORD))
    else:
        df = pd.read_csv(path)

    refactor_data_frame(df)

    return df


if __name__ == '__main__':
    get_data()
    # utilZepp.get_path_first_file_by_prefix("SPORT")
    #print(help(files))

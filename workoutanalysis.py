import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ReadData

def read(path: 'str' = 'sport') -> 'pd.DataFrame':
    if path == 'sport':
        return pd.read_csv('data/sport/SPORT_1648939638346.csv')
    return pd.read_csv(path)


if __name__ == '__main__':
    df = read("data/sport/SPORT_1648939638346.csv")

import os
import logging
import pandas as pd

# TODO: Implement another type of records
TYPE_RECORDS = ["SPORT"]

PATH_DATA_FOLDER = "data"


def get_path_first_file_by_prefix(prefix: "str") -> "str":
    """
    Function to return the path of the first file in /data.

    Each file in zepp download section process has a pattern in the name.
    In this particular case,
        SPORT_SOMENUMBERS.csv is the file with all information about workout progress and more.
        etc.
    :param prefix: str
    :return: path: str
    """
    try:
        return os.path.join(
            PATH_DATA_FOLDER,
            next(
                filter(
                    lambda name_file: name_file.startswith(prefix),
                    os.listdir(PATH_DATA_FOLDER),
                )
            ),
        )
    except FileNotFoundError:
        logging.error(
            "[SYSTEM] There is no data folder in the root project. To fix it, change this path or make a folder in "
            "the root path. "
        )
    except StopIteration:
        logging.error(
            f"[SYSTEM] There is no file with the prefix {prefix} in the data folder."
        )


if __name__ == "__main__":
    print(get_path_first_file_by_prefix("SPORT"))

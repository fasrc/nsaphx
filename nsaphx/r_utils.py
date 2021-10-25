"""
r_utils.py
====================================
The core module for R data helper functions.
"""

import pyreadr
from pyreadr.custom_errors import PyreadrError

def read_rds(file_path):
    """
    Returns pandas data.frame 

    Inputs:
        | file_path: path to the rds file.

    """

    try:
        # read data
        r_data = pyreadr.read_r(file_path)
        data = r_data[None]
        return data
    except PyreadrError as e_pyr:
        # exception
        print(e_pyr)




# if __name__ == "__main__":
#     mydata = read_rds('filenotexist.rds')




"""
utils.py
====================================
The core module for utility functions.
"""


import xarray as xr


def load_rm_netcdf(file_path):
    """
    A temporal function to read Randall Martin research group's exposure data. 
    Returns DataArray object.

    Inputs:
        | file_path: path to the netcdf (.nc) file.

    """

    data = xr.open_dataarray(file_path)
    return(data)

    




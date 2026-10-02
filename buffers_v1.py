# -*- coding: utf-8 -*-
"""
Created on Thu 26th February 2026
making buffers
@author: simmers
"""

## this file takes the tracks of spraying vans for 3 years and makes buffers
# from them, based on a customisable distance

# V2 in the same folder does the same, but excludes all traps/buffers that
# are in ikaria

# -------- OUPUTS --------
# 1. buffers around spraying tracks

# importing relevant packages
import geopandas as gpd
import pandas as pd
import fiona
from shapely.geometry import Point, LineString, shape, Polygon
from io import StringIO
from pathlib import Path
import os
import numpy as np

# ============= IMPORT FILES & DEFINE DIRECTORY =============
# define folder variable & iterate through it
lines = gpd.read_file('../MY_INPUTS/spray_tracks.gpkg')


buffy = lines.to_crs('EPSG:2100')

buffy['geometry'] = buffy.buffer(distance = 50)

buffy_final = buffy.to_crs('EPSG:4326')

buffy_final.to_excel('./bufferexcel.xlsx')
buffy_final.to_file('../MY_INPUTS/buffers_50.gpkg')

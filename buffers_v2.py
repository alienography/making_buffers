# -*- coding: utf-8 -*-
"""
Created on Thu 26th February 2026
making buffers
@author: simmers
"""

## this file takes the tracks of spraying vans for 3 years and makes buffers
# from them, based on a customisable distance
# THIS VERSION excludes all points/buffers that are in ikaria not samos

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

# read in the geometry of samos to use as a filter
filterr = gpd.read_file('../MY_INPUTS/samos_filter.gpkg')

# convert both to the relevant CRS (Greek Grid)
buffr = lines.to_crs('EPSG:2100')
filteri = filterr.to_crs('EPSG:2100')

# filter out all tracks not in samos
buffer_filter = gpd.sjoin(
    buffr,
    filteri,
    predicate='intersects')

# create a 50m buffer around the spray tracks
buffer_filter['geometry'] = buffer_filter.buffer(distance = 50)

# for test purposes - print the head of the geometry
#heady = buffer_filter.head(5)
#heady.to_excel('./buffertest.xlsx')

# convert to WGS84 for final export
buffr_final = buffer_filter.to_crs('EPSG:4326')

# drop unnecessary columns that remained in the original dataframe
buffr_final = buffr_final.drop(['index_right', 'id'], axis=1)

# for test purposes, print only unique buffer dates
#buffy_dates = buffy_final['date'].unique()
# save this text to allow for a comparison with spraying dates known
#np.savetxt('./comparedates2.txt', buffy_dates)

# export to excel/geopackage
buffr_final.to_excel('./bufferexcel2.xlsx')
buffr_final.to_file('../MY_INPUTS/buffer50.gpkg', driver='GPKG')

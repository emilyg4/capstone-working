import os
import arcpy
from arcpy import env

env.workspace = "C:\Users\egree\Documents\MSGT\Capstone\mysite\cruisertime\data"
env.overwriteOutput = True
outpath = "C:\Users\egree\Documents\MSGT\Capstone\mysite\cruisertime\data"

newjson = arcpy.FeaturesToJSON_conversion("SPLocations.shp", "SPLocations4.json", "FORMATTED") # convert .shp to .json
print "Success! Your new GeoJSON file is located here: " + str(newjson)

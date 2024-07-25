# Point Address Locator Creation with ArcPy

This repository contains a script for creating a point address locator using ArcPy. The locator is designed to work with a master address table containing addresses in Mecklenburg County. The script sets up the necessary environment, checks the ArcPy version, and creates the locator using specified field mappings.

## Prerequisites

Ensure you have the following installed:

- Python
- ArcPy (version 2.7)
- pandas
- numpy

## Script Overview

### Import Libraries


import arcpy 
import pandas as pd 
import numpy as np
import os

### Check ArcPy Version
The script checks the installed version of ArcPy to ensure compatibility.

print(f"ArcPy Version: {arcpy.GetInstallInfo()['Version']}")

## Set Path
Set the path where your address locator will be saved.

path = "C:\\Users\\padu\\Desktop\\UrbanInstitute\\Proximity Variables\\"
os.chdir(path)

## Set Working Directory
Set the working environment to the geodatabase where your master address table and street centerline feature class are stored.

ProjectGDB =  r"C:\\Users\\padu\\Desktop\\UrbanInstitute\\Proximity Variables\\Proximity Variables.gdb"
arcpy.env.overwriteOutput = True
arcpy.env.workspace = ProjectGDB

### Create a Point Address Locator
To create a point address locator, you need a point feature class master address table with all the addresses in Mecklenburg County.

countrycode = "USA"   
primary_table = "MAT2022 PointAddress"                       
field_mapping =   "'PointAddress.ADDRESS_JOIN_ID  MAT2022.OBJECTID';"\
                  "'PointAddress.HOUSE_NUMBER MAT2022.txt_street';"\
                  "'PointAddress.STREET_NAME MAT2022.nme_street';"\
                  "'PointAddress.STREET_SUFFIX_TYPE MAT2022.repl_txt_r';"\
                  "'PointAddress.FULL_STREET_NAME MAT2022.address';"\
                  "'PointAddress.CITY MAT2022.nme_po_cit';"\
                  "'PointAddress.REGION_ABBR MAT2022.state';"\
                  "'PointAddress.POSTAL MAT2022.cde_zip1';"\
                  "'PointAddress.DISPLAY_X MAT2022.POINT_X';"\
                  "'PointAddress.DISPLAY_Y MAT2022.POINT_Y'"
out_locator = "MAT2022_Locator"
languagecode = 'ENG' 
                             
arcpy.geocoding.CreateLocator(countrycode, primary_table, field_mapping, out_locator, languagecode, None, None, None, "GLOBAL_HIGH")

** Running the Script in the Future
If you need to create a locator for a new master address table (e.g., MAT2023):

Use Find and Replace to update the fields and run the script.
Ensure all fields present in MAT2022 are also in MAT2023. If field names have changed, update the names in the script accordingly.
Check the ArcPy version to ensure consistency with your installed version.
For documentation on Field Mapping rules for the latest ArcPy version, refer to the ArcPy documentation.

Contributing
If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.




#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Author : Providence Adu, PhD
'''


# ### Import Libraries

# In[1]:


import arcpy 
import pandas as pd 
import numpy as np
import os


# `Check Arcpy Version: This locator was created you ArcPy Version 2.7`

# In[5]:


print(arcpy.GetInstallInfo()['Version'])


# ### Set Path
# - This is the path where you address locator will be saved

# In[6]:


path = "C:\\Users\\padu\\Desktop\\UrbanInstitute\\Proximity Variables\\"
os.chdir(path)


# ### Set working directory
# - This directory will be the geodatabase where you Master Address Table and Street Centerline feature class are stored
# - Set working environment: set work space to your geodatabase and overwrite to true

# In[7]:


ProjectGDB =  r"C:\\Users\\padu\\Desktop\\UrbanInstitute\\Proximity Variables\\Proximity Variables.gdb"
arcpy.env.overwriteOutput = True
arcpy.env.workspace = ProjectGDB


# ### Create  A Point Address Locator
# 
# - To create the a point Address locator, you need a [`point feature class master address table`](https://maps.mecknc.gov/openmapping/data.html#master%20address%20) with all the addresses in the Mecklenburg County
# - The master address table used in the example below is named `MAT2022`
# 
# - The locator needs five main fields: the `country code`, `primary table`, `field mapping`, `name of the output locator` and `language`
# - **Primary Table** : Specify the role of the address table being used, in the example below, we are using `PointAddress` 
# - **Field Mapping** : The field mapping allows you to match the fields in your address table to the locator role fields, for example in our master address table, the `address` field is the `FUll STREET NAME`, and `POSTAL`(zipcode)  is `zip1` , hence we map them accordingly. 
# - **Output Locator** : The name you given your Address Locator, in the example below, we call the locator `MAT2022_Locator`
# - **Language code** : The language code is English specified as `ENG`
# 
# 
# - This locator was created with `Arcpy 2.7`, check your version of Arcpy using the code `print(arcpy.GetInstallInfo()['Version'])` and make your the way you execute your field mappings matches how it's done in your Arcpy version. For documentation on `Field Mapping` rules for the latest Arcpy Version, check this **[`link`](https://pro.arcgis.com/en/pro-app/latest/tool-reference/geocoding/create-locator.html)**
# 
# **Running this script in the future**
# 
# - Suppose you have a point feature class master address table named MAT2023 in your geodatabase:
#     * You can use Find and Replace to update the fields and run the script to create an address locator for your MAT2023 table. 
#     * You can Find `MAT2022` and replace it with `MAT2023` then run the script to create your new locator
#     * Make sure your all the fields present in the `MAT2022` are also in the `MAT2023`, if the field names have been changed, you can update the names accordingly in the script
#     * Again check the `Arcpy Version` to ensure that the method being used in version 2.7 is consistent with your Arcpy Version. For example, in `Arcpy 3.3`, the `Field Mapping` uses a `List` instead of `Multiline String`

# In[8]:


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
                             
arcpy.geocoding.CreateLocator(countrycode, primary_table , field_mapping, out_locator,
                              languagecode, None, None, None, "GLOBAL_HIGH")


# ### Create  A Street Address Locator
# 
# 
# - To create the a Street Address locator, you need a [`street center line address table`](https://maps.mecknc.gov/openmapping/data.html#street%20centerline) with all the addresses in the Mecklenburg County
# 
# - The master address table used in the example below is named `streets_2022`
# 
# - The locator needs five main fields: the `country code`, `primary table`, `field mapping`, `name of the output locator` and `language`
# - **Primary Table** : Specify the role of the address table being used, in the example below, we are using `StreetAddress` 
# - **Field Mapping** : The field mapping allows you to match the fields in your address table to the locator role fields, for example in our master address table, the `wholestnam` field is the `FULL STREET NAME`, and `POSTAL_RIGHT`(zipcode on right side of the street)  is `r_zipcode` , hence we map them accordingly. 
# - **Output Locator** : The name you given your Address Locator, in the example below, we call the locator `StreetAddressLocator2022`
# - **Language code** : The language code is English specified as `ENG`
# 
# 
# - This locator was created with `Arcpy 2.7`, check your version of Arcpy using the code `print(arcpy.GetInstallInfo()['Version'])` and make your the way you execute your field mappings matches how it's done in your Arcpy version. For documentation on `Field Mapping` rules for the latest Arcpy Version, check this **[`link`](https://pro.arcgis.com/en/pro-app/latest/tool-reference/geocoding/create-locator.html)**
# 
# 
# **Running this script in the future**
# 
# - Suppose you have a point feature class master address table named streets_2023 in your geodatabase:
#     * You can use Find and Replace to update the fields and run the script to create an address locator for your MAT2023 table. 
#     * You can Find `streets_2022` and replace it with `streets_2023` then run the script to create your new locator
#     * Make sure your all the fields present in the `streets_2022` are also in the `streets_2023`, if the field names have been changed, you can update the names accordingly in the script
#     * Again check the `Arcpy Version` to ensure that the method being used in version 2.7 is consistent with your Arcpy Version. For example, in `Arcpy 3.3`, the `Field Mapping` uses a `List` instead of `Multiline String`

# In[10]:


countrycode = "USA"
primary_table = "streets_2022 StreetAddress"
field_mapping = "'StreetAddress.STREET_NAME_JOIN_ID streets_2022.OBJECTID';"\
                "'StreetAddress.HOUSE_NUMBER_FROM_LEFT streets_2022.ll_add';"\
                "'StreetAddress.HOUSE_NUMBER_TO_LEFT streets_2022.ul_add';"\
                "'StreetAddress.HOUSE_NUMBER_FROM_RIGHT streets_2022.lr_add';"\
                "'StreetAddress.HOUSE_NUMBER_TO_RIGHT streets_2022.ur_add';"\
                "'StreetAddress.STREET_NAME streets_2022.streetname';"\
                "'StreetAddress.STREET_SUFFIX_TYPE streets_2022.streettype';"\
                "'StreetAddress.FULL_STREET_NAME streets_2022.wholestnam';"\
                "'StreetAddress.CITY_LEFT streets_2022.l_juris';"\
                "'StreetAddress.CITY_RIGHT streets_2022.r_juris';"\
                "'StreetAddress.POSTAL_LEFT streets_2022.l_zipcode';"\
                "'StreetAddress.POSTAL_RIGHT streets_2022.r_zipcode'"
out_locator = "StreetAddressLocator2022"
languagecode = "ENG"
arcpy.geocoding.CreateLocator(countrycode, primary_table, field_mapping, out_locator,
                              languagecode, None, None, None, "GLOBAL_HIGH")


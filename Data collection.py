# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:25:12 2017

@author: Owner
"""

#%%
import os
folder="Data"
fileName="anes_timeseries_2012.dta"
fileToRead=os.path.join(folder,fileName)
#os.path.sep
# where am I?
#os.getcwd()
#os.chdir()
#%%
import pandas as pd
varsOfInterest=["libcpre_self","libcpo_self"]
import os
folder="Data"
fileName="anes_timeseries_2012.dta"
fileToRead=os.path.join(folder,fileName)
dataStata=pd.read_stata(fileToRead,columns=varsOfInterest)
dataStata.head()
#%%
#Step1: Set the enviroment variables
####################################
import os
os.environ['KAGGLE_USERNAME'] = "mujahedtrainer"  #manually input My_Kaggle User_Name 
os.environ['KAGGLE_KEY'] = "88213902c427e7b432aa81b68fe4aaac"  #manually input My_Kaggle Key 

#Step2: Install Kaggle Package
##############################
!pip install kaggle or !pip install -q kaggle

#Step3: Download DataSet using Kaggle Package
#############################################
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

#Step4: Manage Dataset
####################################
api.dataset_list(file_type="csv")
api.dataset_download_files('mujahedtrainer/handlepylogs', path='/content/', unzip=True)
api.dataset_download_files('mujahedtrainer/automobile')
api.dataset_download_file('mujahedtrainer/handlepylogs','ServerKeyEqualsValue.log')


#Step5: Unzip DataSet using Zip Package
#######################################
!ls
from zipfile import ZipFile
zf = ZipFile('handlepylogs.zip')
zf.extractall()   #extracted data is saved in the same directory as notebook
zf.close()

#Step6: Reading DataSet using Pandas package
############################################
import pandas as pd
data=pd.read_csv('ServerKeyEqualsValue.log',sep=';')
data

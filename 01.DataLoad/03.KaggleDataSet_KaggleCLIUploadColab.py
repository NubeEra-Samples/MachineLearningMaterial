									#########################################
									######### KAGGLE USING CLI ##############
									#########################################

#Step1: Uploading data from Local to Colab
##########################################
from google.colab import files
files.upload()  #this will prompt you to upload the kaggle.json. Download from Kaggle>Kaggle API-file.json. Save to PC to PC folder and choose it here
#Output Sample:
#kaggle.json
#kaggle.json(application/json) - 69 bytes, last modified: 29.06.2021 - 100% done
#Saving kaggle.json to kaggle.json
#{'kaggle.json': 
#b'{"username":"mujahedtrainer","key":"88213902c427e7b432aa81b68fe4aaac"}'}

#Step2: Creating Directory Structure for Kaggle Token
#####################################################
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!ls ~/.kaggle
!chmod 600 /root/.kaggle/kaggle.json  # set permission
#Output:
#kaggle.json

#Step3: Set the enviroment variables
####################################
import os
os.environ['KAGGLE_USERNAME'] = "mujahedtrainer"  				#manually input My_Kaggle User_Name 
os.environ['KAGGLE_KEY'] = "88213902c427e7b432aa81b68fe4aaac"  	#manually input My_Kaggle Key 

#Step4: Downloading DataSet using Kaggle CLI
############################################
!kaggle datasets download -d mujahedtrainer/handlepylogs #download dataset to default folder content/handlepylogs.zip if I want 


#find kaggle dataset link (for example) https://www.kaggle.com/willkoehrsen/home-credit-default-risk-feature-tools 
#and choose part_of_the_link - willkoehrsen/home-credit-default-risk-feature-tools
#set link_from Kaggle willkoehrsen/home-credit-default-risk-feature-tools
#set Colab folder download_to  /content/gdrive/My Drive/kaggle/credit/home-credit-default-risk-feature-tools.zip
!kaggle datasets download -d willkoehrsen/home-credit-default-risk-feature-tools -p /content/gdrive/My\ Drive/kaggle/credit 
#Output
#Downloading home-credit-default-risk-feature-tools.zip to /content/gdrive/My Drive/kaggle/credit
#100% 3.63G/3.63G [01:31<00:00, 27.6MB/s]
#100% 3.63G/3.63G [01:31<00:00, 42.7MB/s]



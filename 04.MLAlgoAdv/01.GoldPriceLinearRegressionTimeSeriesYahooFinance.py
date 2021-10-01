#!pip install yfinance

#Linear Regression Algorithm to use in Time Series dataset
from sklearn.linear_model import LinearRegression

#EDA operations required Pandas & Numpy
import pandas as pd
import numpy as np

#For Visualizations
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('seaborn-darkgrid')

#DataSet gathering From Yahoo Finance Department
import yfinance as yf

#Read Data
df=yf.download('GLD','2008-01-01','2021-9-19',auto_adjust=True)
df.head()

#Only Keep close column
df=df[["Close"]]

#Remove Missing Values
df=df.dropna()

#Plot the closing price of GLD stock
df.Close.plot(figsize=(10,7),color='r')
plt.ylabel("Gold Prices")
plt.title("Gold Prices Series")
plt.show()

#Finding Close Price of stock based on size as W=3 & 9
df["S3"]=df["Close"].rolling(window=3).mean()
df["S9"]=df["Close"].rolling(window=9).mean()

#Shifting From Tail by 1
df["next_day_price"]=df["Close"].shift(-1)

#Clean DataSet and Prepare X & Y
df=df.dropna()
X=df[['S3','S9']]
Y=df['next_day_price']

# Split the data into train and test dataset
t = .8
t = int(t*len(Df))

#Train Dataset(80%)
X_train=X[:t]
Y_train=Y[:t]

#Test Dataset(20%)
X_test=X[t:]
Y_test=Y[t:]

#Prepare Model to start training on 80% DataSet
linear=LinearRegression().fit(X_train,Y_train)

#Pridicting Time Series Linear Regression Gold price for 3 & 9 Days
print("Linear Regression model")
print("Gold Price(y)=%.2f*3 Days Moving Average(x1) + %.2f * 9 Days Moving Average(x2) + %.2f(constant) " 
      % (linear.coef_[0],linear.coef_[1],linear.intercept_))
__author__ = 'tavleen'
import pandas as pd
import numpy as np
from sklearn.naive_bayes import BernoulliNB
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
train = pd.read_csv('/home/tavleen/PycharmProjects/crime_clasification/train.csv', parse_dates=['Dates'])
test=pd.read_csv('/home/tavleen/PycharmProjects/crime_clasification/test.csv', parse_dates=['Dates'])
#print(train.head(5))


#print np.correlate(train['DayOfWeek'],train['Category'])
#Convert crime labels to numbers
le_crime = preprocessing.LabelEncoder()
crime = le_crime.fit_transform(train.Category)

#Get binarized weekdays, districts, and hours.
days = pd.get_dummies(train.DayOfWeek)
district = pd.get_dummies(train.PdDistrict)
#train["Dates"]=pd.to_datetime(train["Dates"])
time_train = pd.DatetimeIndex(train.Dates)
hour = time_train.hour
hour = pd.get_dummies(hour)

#Build new array
train_data = pd.concat([hour, days, district], axis=1)
train_data['crime']=crime

#Repeat for test data
days = pd.get_dummies(test.DayOfWeek)
district = pd.get_dummies(test.PdDistrict)
#print district

time_test = pd.DatetimeIndex(test.Dates)
hour = time_test.hour
hour = pd.get_dummies(hour)

test_data = pd.concat([hour, days, district], axis=1)
features = list(set(np.unique(train["DayOfWeek"])))
#print(features)
#print type(feature_day)
feature_district = list(set(np.unique(train["PdDistrict"])))
#print feature_district
features = features + feature_district
#print features

training, validation = train_test_split(train_data, train_size=.60)
#features = np.union1d(feature_day , feature_district)
#features = ['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday',
#'Wednesday', 'BAYVIEW', 'CENTRAL', 'INGLESIDE', 'MISSION',
#'NORTHERN', 'PARK', 'RICHMOND', 'SOUTHERN', 'TARAVAL', 'TENDERLOIN']
#print type(features)

model = BernoulliNB()
model.fit(train_data[features], train_data['crime'])
predicted = model.predict_proba(test_data[features])

#Write results
result=pd.DataFrame(predicted, columns=le_crime.classes_)
result.to_csv('testResult.csv', index = True, index_label = 'Id' )


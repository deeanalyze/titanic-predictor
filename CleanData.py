# -*- coding: utf-8 -*-
from scipy.stats import mode
import numpy as np
import pandas as pd
def CleanDataFrame(dataFrame) :
    
    dataFrame[['Age','Fare']][dataFrame.Fare<5]
    dataFrame.Fare = dataFrame.Fare.map(lambda x: np.nan if x==0 else x)
    dataFrame[['Age','Fare']][dataFrame.Fare==0]
    classmeans = dataFrame.pivot_table('Fare', rows='Pclass', aggfunc='mean')
    dataFrame.Fare = dataFrame[['Fare', 'Pclass']].apply(lambda x: classmeans[x['Pclass']] if pd.isnull(x['Fare']) else x['Fare'], axis=1 )
    meanAge=np.mean(dataFrame.Age)
    dataFrame.Age=dataFrame.Age.fillna(meanAge)
    dataFrame.Cabin=dataFrame.Cabin.fillna("Unknown")
    
    modeEmbarked = mode(dataFrame.Embarked)[0][0]
    dataFrame.Embarked = dataFrame.Embarked.fillna(modeEmbarked)
    
    dataFrame['bins_and_binned_fare'] = pd.qcut(dataFrame.Fare, 5 , retbins=True, labels=[0,1,2,3,4])[0]
    dataFrame['bins_and_binned_age'] = pd.qcut(dataFrame.Age, 5 , retbins=True, labels=[0,1,2,3,4])[0]
    dataFrame['Gender'] = dataFrame['Sex'].map( {'female': 0, 'male': 1} ).astype(float)
    dataFrame['Class'] = dataFrame['Pclass'].map({ 3 : 2, 2 : 1, 1 : 0}).astype(float)
    dataFrame['Embark'] = dataFrame['Embarked'].map({'S': 0, 'C' : 1, 'Q' : 2}).astype(float)
    
    new_dataFrame = dataFrame.drop(['Name', 'Sex', 'Ticket', 'Cabin', 'PassengerId', 'Embarked', 'Fare', 'Age'], axis=1)
    
    return new_dataFrame

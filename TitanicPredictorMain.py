# -*- coding: utf-8 -*-
import pandas as pd
import csv as csv
from CleanData import CleanDataFrame
from sklearn.ensemble import RandomForestClassifier
from PlotGraphs import PlotGraphs

import StringIO, pydot
from sklearn.tree import export_graphviz
from IPython.display import Image

traindf = pd.read_csv("Data/train.csv")
df = traindf
cleaned_traindf = CleanDataFrame(traindf).values

# specifies the parameters of our graphs
PlotGraphs(traindf)

print 'Training...'
forest = RandomForestClassifier(n_estimators=100)
forest = forest.fit(cleaned_traindf[0::,1::], cleaned_traindf[0::,0])
print "Training complete. Your ninja is ready to go!"

print 'Plotting this sexy tree'
dot_data = StringIO.StringIO()
export_graphviz(forest, out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())

testdf = pd.read_csv("Data/test.csv")
testDataPassengerIds = testdf['PassengerId'].values
cleaned_testdf = CleanDataFrame(testdf).values

print "Okay. We're ready to make a survival prediction"
print "Predicting..."
output = forest.predict(cleaned_testdf).astype(int)

# Write the predictions to a file
predictions_file = open("Data/MyPrediction.csv", "wb")
open_file_object = csv.writer(predictions_file)
open_file_object.writerow(["PassengerId","Survived"])
open_file_object.writerows(zip(testDataPassengerIds, output))
predictions_file.close()
print 'Done.'
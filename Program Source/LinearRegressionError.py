from sklearn import metrics
from scipy import stats
import pandas as pd
import numpy as np 

df = pd.read_csv('USAPopDeciEdit.csv')
y_true=df['2013']
y_pred=df['2013PREDINT']

# MAE
print("MAE: {}".format(metrics.mean_absolute_error(y_true, y_pred)))
# MSE
print("MSE: {}".format(metrics.mean_squared_error(y_true, y_pred)))
# RMSE
print("RMSE: {}".format(np.sqrt(metrics.mean_squared_error(y_true, y_pred))))
# R^2 (Coefficient of Determination) Regression Score
print("R Squared: {}".format(metrics.r2_score(y_true, y_pred)))
print("Accuracy Score: {}".format(metrics.accuracy_score(y_true, y_pred)))
print("Accuracy Score Exact: {}".format(metrics.accuracy_score(y_true, y_pred, normalize=False)))
# "Average Precision: {}" print(metrics.average_precision_score(y_true, y_pred))
print("T-Test: {}".format(stats.ttest_ind(y_true, y_pred)))

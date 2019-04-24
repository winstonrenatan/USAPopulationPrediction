# USA Population Prediction
This repository is created to explain our project on Operation Research 2019 on our major, Informatics. The goal of this software is to predict population in a county of all states based on current given data 2010-2016. This software will display the population spreaded in the map of United States of America. Therefore, there are two software in this project one for predicting and the one displaying the map. It is done that way in consideration of the time needed in processing the data in the same software. The prediction will be done with linear regression as there are no data provided besides the year and population, other data may not be connected to the population in a county.

## Authors
Alessandro Luiz Kartika (01082170029)<br>
Denny Raymond (01082170017)<br>
Winston Renatan (01082170030)<br>
Informatics 2017, Universitas Pelita Harapan Main Campus

## Requirement
[Python 3.7](https://www.python.org/downloads/) <br>
Guide on how to download: https://youtu.be/dX2-V2BocqQ

### Packages Needed
1. Pandas (pip install pandas)
2. Numpy (pip install numpy)
3. Dash (pip install dash)
4. Dash Table Experiments (pip install dash-table-experiments)

On Windows 10, open the command prompt and go to the folder you want and type the following.

## Installation/Running Instruction
- Download the files on folder "LinearRegression".
- Open and run "PredictorProgram.py", this will produce the file "USAPopulationStart.csv"<br>
  "USAPopDecit.csv" will contain the prediction result together with data that will be used for calculating the errors.<br>
  ![RunAndGet]()<br>
- Open "USAPopDeci.csv" using the floor function manually change the new result column to obtain whole number(integer).<br>
- Rename the file to "USAPopDeciEdit.csv" so it can be used in other program.<br>
  ![RenameFile](https://github.com/winstonrenatan/USAPopulationPrediction/blob/master/PicturesDocumentation/RenameFile.gif)<br>
- Open and run "LinearRegressionError.py" that will determine the results error.
- Open and run "MainProject.py" that will show up the map together with the population.

## USA Population Prediction Programs Details
### Predictor Program
In order to get the detail needed for all the equations below, first we need to start by finding the mean of the data which consist of X and Y. Where X is the years and Y is the population in county of a state.<br>
Here mean X will never change as the real data we got only from 2010-2016, with the mean of 2013.0.<br>
While mean Y will consistently change according to the population in that county.<br>
Where ![SSxy](https://latex.codecogs.com/gif.latex?SS%7Bxy%7D) is the sum of cross-deviations of x and y:<br>
![SSxyEq](https://latex.codecogs.com/gif.latex?SS%7Bxy%7D%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20%28x_%7Bi%7D%20-%20%5Coverline%7Bx%7D%29%28y_%7Bi%7D%20-%20%5Coverline%7By%7D%29)<br>
While ![SSxx](https://latex.codecogs.com/gif.latex?SS%7Bxx%7D) is the sum of squared deviations of x:<br>
![SSxxEq](https://latex.codecogs.com/gif.latex?SS%7Bxx%7D%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20%28x_%7Bi%7D%20-%20%5Coverline%7Bx%7D%29%5E%7B2%7D)<br>
As what is shown above, ![SSxx](https://latex.codecogs.com/gif.latex?SS%7Bxx%7D) will also maintain its value in 28.0 which is caused by the data that won't change as it is not affiliated with Y. <br>
Here are the mathematical detail to obtain the coefficients:<br>
![beta1](https://latex.codecogs.com/gif.latex?%5Cbeta1%20%3D%20%5Cfrac%7BSS%7Bxy%7D%7D%7BSS%7Bxx%7D%7D)<br>
![beta0](https://latex.codecogs.com/gif.latex?%5Cbeta0%20%3D%20%5Coverline%7By%7D%20-%20%5Cbeta%20%7B1%7D%5Coverline%7Bx%7D)<br>
Which all lead to the following main function to predict or we could call it the Regression Line Equation: 
![RegressionLineEq](https://latex.codecogs.com/gif.latex?h%28xi%29%3D%5Cbeta%7B0%7D%20&plus;%20%5Cbeta%7B1%7Dx%7Bi%7D)<br>
Further Explanation:<br>
![hxi](https://latex.codecogs.com/gif.latex?h%28xi%29): predicted response value for i-th observation.<br>
![b0b1xi](https://latex.codecogs.com/gif.latex?%5Cbeta0&plus;%5Cbeta%201%7Bx%7Bi%7D%7D): regression coefficients and represent y-intercept and slope of regression. <br>

As the population will always change, so will the coefficient and the final answer (prediction value). Of course, we would not want to process all the data manually one by one to find its predicted population for the following years. Thus, we need to use the function provided using pandas. We then need to create several columns with the equations we had above, which all useful in generating coefficients so it can predict the year we wanted. The result generated will be given in decimals.<br>
![PredictorSnippet](https://github.com/winstonrenatan/USAPopulationPrediction/blob/master/PicturesDocumentation/PredictorSnip.PNG)<br>
We also would like to train and test the data, which can be acquired from the snippet below. It is also should be convert to integer and be placed in the LinearRegressionError Program to have the error value determined. The final product from this program is a csv file where we will need to convert the values to an integer that can be used for the other programs below. <br>
![PredictorResult](https://github.com/winstonrenatan/USAPopulationPrediction/blob/master/PicturesDocumentation/ChangeToINT.gif)<br>
The yellow one means the things we have calculated from the equation above. <br>
The green one is used for the LinearRegressionError Program to calculate errors. <br>
While the blue label is the prediction result for year mentioned. <br>

### LinearRegressionError Program
From the "xxx.csv" which is the final result from the Predictor Program, we should convert all the number with decimals to an integer to be processed here. With the steps mentioned at the Installation/Running Instruction point 3. We then would like to see if our prediction is close to the actual value or not and see the errors. Here is some of the data that we use. <br>
![ExcelTrain](https://github.com/winstonrenatan/USAPopulationPrediction/blob/master/PicturesDocumentation/CompareLinReg.PNG)<br>

Here are the code snippet that is used to determined the values:<br>
![SnipOfLinReg](https://github.com/winstonrenatan/USAPopulationPrediction/blob/master/PicturesDocumentation/LinRegError%20Snip.PNG)<br>
Those function are used from the scikit learn to determine MAE, MSE, RMSE, R<sup>2</sup>, and Accuracy Score. While we need scipy to have the t-test result.<br>

MAE (Mean Absolute Error) measures the average magnitude of error in set of predictions. It’s the average over the test sample of the absolute differences between prediction and actual observation where all individual differences have equal weight.
Here is the mathematical equation for MAE: ![MAE](https://latex.codecogs.com/gif.latex?MAE%3D%5Cfrac%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%7Cp_%7Bi%7D-a_%7Bi%7D%29%7C%7D%7Bn%7D)<br>

RMSE (Root Mean Squared Error) is quadratic scoring rule that measures average magnitude of error. <br>
Following is the equation of MSE together with RMSE:<br>
![MSE](https://latex.codecogs.com/gif.latex?MSE%3D%5Cfrac%7B1%7D%7Bn%7D%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28y_%7Bi%7D-%5Coverline%7By%7D_%7Bi%7D%29%5E%7B2%7D%7D)<br>
![RMSE](https://latex.codecogs.com/gif.latex?RMSE%3D%5Csqrt%7B%5Cfrac%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28p_%7Bi%7D-a_%7Bi%7D%29%5E%7B2%7D%7D%7Bn%7D%7D)<br>

Besides, we also have the R<sup>2</sup> which measures the strength and direction of a linear relationship between two variables. The main goal is to get as close to -1 or +1. Where exactly –1 means its a perfect downhill (negative) linear relationship and on the other side exactly +1 means a perfect uphill (positive) linear relationship. With the following mathematical equation:
![RSquared](https://latex.codecogs.com/gif.latex?R%5E%7B2%7D%3D1-%5Cfrac%7BExplained%20Variation%7D%7BTotal%20Variation%7D)<br>

There is also an accuracy score, this function computes subset accuracy: the set of labels predicted for a sample must exactly match the corresponding set of labels in y_true. The normalize is default to false, it will divide amongstly. If the normalize is set to true, then it will just provide the number of exact value.<br>

The t-Test used is a two-sided test for the null hypothesis that 2 independent samples have identical average (expected) values. We use this in our situation because we would like to observe two independent samples from different population. Using this t-test the goal is to compare the mean between two samples, aiming for p-value around 0.05 or 5%. Here is the mathematical equation for t-test: ![Ttest](https://latex.codecogs.com/gif.latex?t%3D%5Cfrac%7B%5Coverline%7BX_%7B1%7D%7D-%5Coverline%7BX_%7B2%7D%7D%7D%7Bs_%7Bp%7D%5Csqrt%7B%5Cfrac%7B2%7D%7Bn%7D%7D%7D)<br>

### MainProject Program
The MainProject Program aims to view all the data we have in a United States Map. This program is built in Python Dash. Some of the features is to filter the county exposed based on the states together with FUNCSTAT. For better understanding of FUNCSTAT please do view the reference we have at the bottom of the repository. The features and main program demo can be seen at the Result.<br>

## Result
Here are the results from the LinearRegressionError Program we have which provide several things we can use to determine the accuracy of the prediction we had with the equation we had above.<br>
![ErrorResult](https://github.com/winstonrenatan/USAPopulationPrediction/blob/master/PicturesDocumentation/LinearRegressionError.gif)<br>
The result shows that from the data trained and tested.

|Evaluation of     |Value                     |
|------------------|--------------------------|
|MAE               |301.83503836317135        |
|MSE               |920496.7397698209         |
|RMSE              |959.4252132239495         |
|R<sup>2</sup>     |0.9999913896690903        |
|Accuracy Score    |0.005434782608695652      |
|Accuracy          |17                        |
|T-Test(Statistic) |-0.0020707888332106195    |
|T-Test(P-Value)   |0.9983478167887199        |

While we can see the Final Result of the Project is below.<br>
![MainGIF](https://github.com/winstonrenatan/USAPopulationPrediction/blob/master/PicturesDocumentation/DemoMain.gif)<br>

## References and Acknowledgements
- Keith Galli. 25 October 2018. https://youtu.be/vmEHCJofslg (Python Pandas Data Science)
- ProgrammingKnowledge. 21 November 2015. https://youtu.be/dX2-V2BocqQ (Install Python)
- JohnM from Kaggle. https://www.kaggle.com/jpmiller/publicassistance (Datasets)
- Deborah J. Rumsey. https://www.dummies.com/education/math/statistics/how-to-interpret-a-correlation-coefficient-r/ (Interpret Correlation Coefficient R)
- Scikit-Learn Developers. https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics (Class and Function)
- U.S. Census Bureau. https://www.census.gov/library/reference/code-lists/functional-status-codes.html (How to Read FUNCSTAT)

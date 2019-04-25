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
  "USAPopDeci.csv" will contain the prediction result together with data that will be used for calculating the errors.<br>
  ![RunAndGet](https://github.com/winstonrenatan/USAPopulationPrediction/blob/master/PicturesDocumentation/RunAndGet.gif)<br>
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
#### Predict Equation and Counting:
```Python
# Calculate Mean
MeanX=2013.0    #Final and never changes
df['meanY']=(df.iloc[:, 10:17].sum(axis=1))/7

# Deviation of X never changes. (SS_XX = np.sum(x*x) - n*m_x*m_x)
SS_XX=28.0
# Cross Deviation of X and Y (Subtract Yi with Mean then multiple with Xi subtracted with mean)
# Subtract Xi with mean: is absolute Year and its mean never change (2013.0)
df['SS_XY']=((df['2010']-df['meanY'])*-3)+((df['2011']-df['meanY'])*-2)+((df['2012']-df['meanY'])*-1)+((df['2013']-df['meanY'])*0)+((df['2014']-df['meanY'])*1)+((df['2015']-df['meanY'])*2)+((df['2016']-df['meanY'])*3)

# Regression Coefficients
df['b_1']=df['SS_XY']/SS_XX
df['b_0']=df['meanY']-df['b_1']*MeanX

# Prediction for Year
df['2013PRED']=df['b_0']+df['b_1']*2013 #Is used to count the error rate
df['2017PRED']=df['b_0']+df['b_1']*2017
df['2018PRED']=df['b_0']+df['b_1']*2018
df['2019PRED']=df['b_0']+df['b_1']*2019
df['2020PRED']=df['b_0']+df['b_1']*2020
```
#### Code to export the result to a csv:
```Python
# Save file to a csv formated file
df.to_csv('USAPopDeci.csv')
```
We also would like to train and test the data, which can be acquired from the snippet below. It is also should be convert to integer and be placed in the LinearRegressionError Program to have the error value determined. The final product from this program is a csv file where we will need to convert the values to an integer that can be used for the other programs below. <br>
![PredictorResult](https://github.com/winstonrenatan/USAPopulationPrediction/blob/master/PicturesDocumentation/ChangeToINT.gif)<br>
The yellow one means the things we have calculated from the equation above. <br>
The green one is used for the LinearRegressionError Program to calculate errors. <br>
While the blue label is the prediction result for year mentioned. <br>

### LinearRegressionError Program
From the "USAPopDeci.csv" which is the final result from the Predictor Program, we should convert all the number with decimals to an integer to be processed here after renaming it to "USAPopDeciEdit.csv". With the steps mentioned at the Installation/Running Instruction point 3. We then would like to see if our prediction is close to the actual value or not and see the errors. Here is some of the data that we use from the year 2013.<br>
![ExcelTrain](https://github.com/winstonrenatan/USAPopulationPrediction/blob/master/PicturesDocumentation/CompareLinReg.PNG)<br>

#### Import/access the dataset:
To compare on Python, having 2013 as TRUE value while 2013PREDINT as the PREDICTION<br>
```Python
df = pd.read_csv('USAPopDeciEdit.csv')
y_true=df['2013']
y_pred=df['2013PREDINT']
```

#### Determined the values:
Those function are used from the scikit learn to determine MAE, MSE, RMSE, R<sup>2</sup>, and Accuracy Score. While we need scipy to have the t-test result.<br>
```Python
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
```

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

#### The code for access the csv file:
```Python
df = pd.read_csv(r'USAPopDeciEdit.csv',engine='python',encoding='latin1')

# choose only certain column
df = df[["state_id","state_name","county_name","lat","lng","FUNCSTAT","2010","2011","2012","2013","2014","2015","2016","2017PREDINT","2018PREDINT","2019PREDINT","2020PREDINT"]].drop_duplicates()
```
#### The code to display the information inside the blue box:
```Python
 # Display the info in the box
df['text'] = df['county_name'] + ', ' + df['state_id'] + '<br>' + \
    df['FUNCSTAT'] + '<br>'+\
    '2010 :' + df['2010'] + '<br>' + \
    '2011 :' + df['2011'] + '<br>' + \
    '2012 :' + df['2012'] + '<br>' + \
    '2013 :' + df['2013'] + '<br>' + \
    '2014 :' + df['2014'] + '<br>' + \
    '2015 :' + df['2015'] + '<br>'+ \
    '2016 :' + df['2016'] + '<br>'+ \
    '2017 :' + df['2017PREDINT'] + '<br>'+ \
    '2018 :' + df['2018PREDINT'] + '<br>'+ \
    '2019 :' + df['2019PREDINT'] + '<br>'+ \
    '2020 :' + df['2020PREDINT']
```
#### The code for the layout table display:
```Python
layout_table = dict(
    autosize=True,
    height=500,
    font=dict(color="rgb(255,255,255)"),
    titlefont=dict(color="rgb(255,255,255)", size='14'),
    margin=dict(
        l=35,
        r=35,
        b=35,
        t=45
    ),
    hovermode="closest",
    plot_bgcolor='#fffcfc',
    paper_bgcolor='#fffcfc',
    legend=dict(font=dict(size=10), orientation='h'),
    )
layout_table['font-size'] = '12'
layout_table['margin-top'] = '20'
```
#### The code for the layout map display:
```Python
layout_map = dict(
        title = 'USA POPULATION'+ '<br>' + \
                'This software will display the population spreaded in the map of United States of America,which have real data from 2010-2016 while prediction from 2017-2020.'+ '<br>' + \
                'Here there are some filter that are available using the states and also FUNCSTAT.',
        colorbar = True,
        autosize = True,
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(0, 0,0)",
            countrycolor = "rgb(162, 162, 162)",
            countrywidth = 2,
            subunitwidth = 2
        ),
        height = 800,
        width = 1500
    )
```
#### The function to generate the USA map:
```Python
def gen_map(df):
    return{
        "data":[{
            "type" : "scattergeo",
            "locationmode" : "USA-states",
            "lon" : list(df['lng']),
            "lat" : list(df['lat']),
            "text" :list(df['text']),
            "mode" : "marker",
            "markers" : [{
                    "size" : 5,
                    "opacity" :0.8,
                    "reversescale" : True,
                    "autocolorscale" : False,
                    "symbol" : "circle",
                    "line" : [{
                        "width" : 1,
                        "color": "rgb(162, 162, 162 )"
                    }],
                    "colorscale" : "scl",
                    }]
            }],
        "layout": layout_map
    }
```
#### The code for the header:
```Python
html.Div(
                [
                    # Header
                    html.H1 (children="US Public Assistant for woman and children",
                             className="nine columns"),
                    html.Div(children=''' 
                            Dash app for RO Projects
                            ''',
                             className="nine columns"
                    )
                ], className="row"
            ),
```
#### The code for the selection state menu:
```Python
#selectors
    html.Div([

        html.Div(
             [
                html.P('Choose State:'),
                dcc.Checklist(
                    id = 'State',
                    options=[
                            {'label': 'Alabama', 'value': 'AL'},
                            {'label': 'Alaska', 'value': 'AK'},
                            {'label': 'Arizona' , 'value': 'AZ'},
                            {'label': 'Arkansas', 'value': 'AR'},
                            {'label': 'California ', 'value': 'CA'},
                            {'label': 'Colorado', 'value': 'CO'},
                            {'label': 'Connecticut', 'value': 'CT'},
                            {'label': 'Delaware', 'value': 'DE'},
                            {'label': 'Florida', 'value': 'FL'},
                            {'label': 'Georgia', 'value': 'GA'},
                            {'label': 'Hawaii', 'value': 'HI'},
                            {'label': 'Idaho', 'value': 'ID'},
                            {'label': 'Illinois', 'value': 'IL'},
                            {'label': 'Indiana', 'value': 'IN'},
                            {'label': 'Iowa', 'value': 'IA'},
                            {'label': 'Kansas', 'value': 'KS'},
                            {'label': 'Kentucky', 'value': 'KY'},
                            {'label': 'Louisiana', 'value': 'LA'},
                            {'label': 'Maine', 'value': 'ME'},
                            {'label': 'Maryland', 'value': 'MD'},
                            {'label': 'Massachusetts', 'value': 'MA'},
                            {'label': 'Michigan', 'value': 'MI'},
                            {'label': 'Minnesota', 'value': 'MN'},
                            {'label': 'Mississipi', 'value': 'MS'},
                            {'label': 'Missouri', 'value': 'MO'},
                            {'label': 'Montana', 'value': 'MT'},
                            {'label': 'Nebraska', 'value': 'NE'},
                            {'label': 'Nevada', 'value': 'NV'},
                            {'label': 'New Hampshire', 'value': 'NH'},
                            {'label': 'New Jersey', 'value': 'NJ'},
                            {'label': 'New Mexico', 'value': 'NM'},
                            {'label': 'New York', 'value': 'NY'},
                            {'label': 'North Carolina', 'value': 'NC'},
                            {'label': 'North Dakota', 'value': 'ND'},
                            {'label': 'Ohio', 'value': 'OH'},
                            {'label': 'Oklahoma', 'value': 'OK'},
                            {'label': 'Oregon', 'value': 'OR'},
                            {'label': 'Pennyslvania', 'value': 'PA'},
                            {'label': 'Rhode Island', 'value': 'RI'},
                            {'label': 'South Carolina', 'value': 'SC'},
                            {'label': 'South Dakota', 'value': 'SD'},
                            {'label': 'Tennessee', 'value': 'TN'},
                            {'label': 'Texas', 'value': 'TX'},
                            {'label': 'Utah', 'value': 'UT'},
                            {'label': 'Vermont', 'value': 'VT'},
                            {'label': 'Virginia', 'value': 'VA'},
                            {'label': 'Washington', 'value': 'WA'},
                            {'label': 'West Virginia', 'value': 'WV'},
                            {'label': 'Wisconsin', 'value': 'WI'},
                            {'label': 'Wyoming', 'value': 'WY'},
                    ],
                    values =['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'],
                    labelStyle={'display': 'inline-block'}
                ),
        ]
        ),
```
#### The code for dropdown menu:
```Python
html.Div(
                    [
                        html.P('FuncStat:'),
                        dcc.Dropdown(
                            id='funcstat',
                            options= [{'label': str(item),
                                                  'value': str(item)}
                                                 for item in set(df['FUNCSTAT'])],
                            multi=True,
                            value=list(set(df['FUNCSTAT']))
                        )
                    ],
                    style={'margin-top': '10'}
                )
            ],
            className='row'
        ),
```
#### The code for Display the Map and Table:
```Python
html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(id='map-graph',
                                  animate=True,
                                  style={'margin-top': '20'})
                    ], className = "six columns"
                ),
                html.Div(
                    [
                        html.H1(children="The Data Table",
                                className="nine columns"),
                        dt.DataTable(
                            rows=df.to_dict('records'),
                            columns=df.columns,
                            row_selectable=True,
                            filterable=True,
                            sortable=True,
                            selected_row_indices=[],
                            id='datatable'),
                    ],
                    style = layout_table,
                    className="six columns"
                ),
```
#### The code for the callbacks for the table, dropdown and selector:
```Python
@app.callback(
    Output('map-graph', 'figure'),
    [Input('datatable', 'rows'),
     Input('datatable', 'selected_row_indices')])
def map_selection(rows, selected_row_indices):
    aux = pd.DataFrame(rows)
    temp_df = aux.iloc[selected_row_indices, :]
    if len(selected_row_indices) == 0:
        return gen_map(aux)
    return gen_map(temp_df)

@app.callback(
    Output('datatable', 'rows'),
    [Input('funcstat', 'value'),
     Input('State', 'values')])
def update_selected_row_indices(funcstat, State):
    map_aux = df.copy()

    # Type filter
    map_aux = map_aux[map_aux['FUNCSTAT'].isin(funcstat)]
    # Boroughs filter
    map_aux = map_aux[map_aux["state_id"].isin(State)]

    rows = map_aux.to_dict('records')
    return rows
```
#### The code for the final touch, to run the dash local server:
```Python
if __name__ == '__main__':
    app.run_server(debug=True)
```
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
![MainGIF](https://github.com/winstonrenatan/USAPopulationPrediction/blob/master/PicturesDocumentation/MainDemo.gif)<br>

## References and Acknowledgements
- Keith Galli. 25 October 2018. https://youtu.be/vmEHCJofslg (Python Pandas Data Science)
- ProgrammingKnowledge. 21 November 2015. https://youtu.be/dX2-V2BocqQ (Install Python)
- JohnM from Kaggle. https://www.kaggle.com/jpmiller/publicassistance (Datasets)
- Deborah J. Rumsey. https://www.dummies.com/education/math/statistics/how-to-interpret-a-correlation-coefficient-r/ (Interpret Correlation Coefficient R)
- Scikit-Learn Developers. https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics (Class and Function)
- U.S. Census Bureau. https://www.census.gov/library/reference/code-lists/functional-status-codes.html (How to Read FUNCSTAT)

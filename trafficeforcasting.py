import  fbprophet
from pandas import read_csv
from pandas import to_datetime
from matplotlib import pyplot 
from fbprophet import Prophet
from pandas import DataFrame
import os
import glob


# GENTRATING THE CSCV FILES FOR EVERY STORE SEPERATELY 
storenames=[]
data=''
dateCount=[]

# READING FILES
with open('data.csv','r') as file: 
    for line in file.readlines():
        storename=line.split(',')[0]
        date=line.split(',')[1]
        count=line.split(',')[2]
        
        if storename not in storenames:
            storenames.append(storename)
            if len(storenames)>2:
                dateCount.append([storenames[-2],data])
            
                #CREATING FILES
                with open('data/'+storenames[-2]+'.csv','w') as w: 
                    w.writelines(data)
            data=''
        data+=date+','+count


for files in glob.glob("data/*.csv"):
    

    # path = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/monthly-car-sales.csv'
    df = read_csv(files, header=0)
    files=files.split('\\')[1]
    # prepare expected column names
    df.columns = ['ds', 'y']
    df['ds']= to_datetime(df['ds'])
    # define the model
    model = Prophet()
    # fit the model
    model.fit(df)
    # define the period for which we want a prediction
    future = list()
    for i in range(11,20):
        date = '2021-03-%02d' % i
        future.append([date])
    future = DataFrame(future)
    future.columns = ['ds']
    future['ds']= to_datetime(future['ds'])
    # use the model to make a forecast
    forecast = model.predict(future)
    # summarize the forecast
    print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head())
    # plot forecast
    # model.plot(forecast)
    model.plot_components(forecast)
    # pyplot.subplot()
    pyplot.show()
    pyplot.savefig('result/'+files[:-4]+'.png')



    

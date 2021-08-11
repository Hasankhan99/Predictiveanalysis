# from typing_extensions import Required
from TrafficCountWithImages.misreport.views import misCount
from collections import defaultdict
from django.shortcuts import redirect, render,HttpResponse
import  fbprophet
from pandas import read_csv
import pandas as pd
from pandas import to_datetime
from matplotlib import pyplot 
from fbprophet import Prophet
from pandas import DataFrame
from import_export import resources
import os
import glob
from .models import Prediction, StoreNames,misdata
from .forms import misdataForms
from django.http import JsonResponse
# from camsconfig.models import CamsData, MisTrafficCount
from .admin import MisResource
from tablib import Dataset
import tablib
from django.contrib import messages


def PredictiveCount(request):
    storename = StoreNames.objects.all()
    context = {
        'storename': storename
    }
    return render(request, 'predictionHome.html', context)    

def get_chart_storewise(request):
    storename = request.GET.get('storename')
    alldata = []
    data = Prediction.objects.filter(Store_name=storename)
    upper_count = 0
    lower_count = 0
    expected_Count = 0
    for dta in data:
        if int(str(dta.Upper_count).split('.')[0])>0:
            upper_count = int(str(dta.Upper_count).split('.')[0])
        if int(str(dta.Lower_count).split('.')[0])>0:
            lower_count = int(str(dta.Lower_count).split('.')[0])
        if int(str(dta.Expected_Count).split('.')[0])>0:
            expected_Count = int(str(dta.Expected_Count).split('.')[0])

        alldata.append({
            'date': dta.date,
            'upper_count':upper_count ,
            'lower_count': lower_count,
            'expected_Count': expected_Count,
        })
    return JsonResponse({'data': alldata})

def allstoreprediction(request):
    return render(request, 'allstoreprediction.html')

def allstorepredictionChart(request):    
    alldata = []
    stores = []

    storenames = StoreNames.objects.all()
    for store in storenames:
        pdata = Prediction.objects.filter(Store_name=store.store_name)   
        upper_count = 0
        lower_count = 0
        expected_Count = 0            
        for dta in pdata:
            if int(str(dta.Upper_count).split('.')[0])>0:
                upper_count = int(str(dta.Upper_count).split('.')[0])
            if int(str(dta.Lower_count).split('.')[0])>0:
                lower_count = int(str(dta.Lower_count).split('.')[0])
            if int(str(dta.Expected_Count).split('.')[0])>0:
                expected_Count = int(str(dta.Expected_Count).split('.')[0])
            alldata.append({
                'date': dta.date,
                'upper_count':upper_count ,
                'lower_count': lower_count,
                'expected_Count': expected_Count,
            })
        stores.append({
            'storename': store.store_name,
            'storedata': alldata
        })
        alldata = []

    return JsonResponse({'data': stores})


    # data = Prediction.objects.all()
    # for dta in data:
    #     stores.append()
    # for dta in data:
    #     alldata.append([{
    #         'date': dta.date,
    #         'upper_count': int(dta.Upper_count.split('.')[0]),
    #         'lower_count': int(dta.Lower_count.split('.')[0]),
    #         'expected_Count': int(dta.Expected_Count.split('.')[0]),
    #     }])
    return JsonResponse({'data': alldata})


def Realdata(request):
    data=misdata.objects.all()
    form=misdataForms()
    if request.method == "POST":
       form = misdataForms(request.POST)

       if form.is_valid():
          form.save()
       # this should be include if form validate failed
    return render(request,'realdata.html', {'mis':data,'form':form})

#Export All data   
def export_stores_xlsTS(request):
    misdata = MisResource()
    dataset = misdata.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="MistrafficCount.csv"'
    return response

def import_stores_xlsTS(request):
    if request.method == 'POST':
        book_resource = resources.modelresource_factory(model=misdata)()
        new_stores = request.FILES['misdata']
        dataset = tablib.Dataset().load(new_stores.read().decode(), format='csv', headers=True)
        result = book_resource.import_data(dataset, dry_run=True)
        messages.warning(request, 'Trying to imprt')

        if not result.has_errors():
            book_resource.import_data(dataset, dry_run=False)
            messages.success(request, 'File data has been imported successfully!')
            
        else:
            messages.warning(request, 'Faild to import Data,')
        return  redirect('Realdata')

def update_misdata(request,pk):
    

    editdata=misdata.objects.get(pk=pk)
    # form=misdataForms(request.POST)
    form = misdataForms(request.POST or None ,instance=editdata)
    data=misdata.objects.all()
    if request.method=='POST':
        if form.is_valid():
            # post = form.save(commit=False)
            form.save()
            return redirect('Realdata')
        
    return render(request,'realdata.html',{'form':form,'mis':data})

def delete_all_mis_data(request):
    alldata=misdata.objects.all()
    alldata.delete()
    return redirect('Realdata')
  

def delete_misdata(request,pk):
    delete_data=misdata.objects.get(pk=pk)
    delete_data.delete()
    return redirect("Realdata")
    
    
def generateData(request):
    # dataset=[]
    obj = misdata.objects.first()
    field_object = misdata._meta.get_field('Store_Name')
    field_value = getattr(obj, field_object.attname)
    mis=misdata.objects.all()
    data=mis.Store_Name
    print(field_value)
    
    
    return HttpResponse(data)

    
    



def generatePredection(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csvPath = os.path.join(BASE_DIR,'static/data.csv')
    dataPath = os.path.join(BASE_DIR,'static/data/')
    savefile = os.path.join(BASE_DIR,'static/savefile/')


# GENTRATING THE CSCV FILES FOR EVERY STORE SEPERATELY 
    storenames=[]
    data=''
    dateCount=[]

    # READING FILES
    with open(csvPath,'r') as file: 
        for line in file.readlines():
            storename=line.split(',')[0]
            date=line.split(',')[1]
            count=line.split(',')[2]
            if storename not in storenames:
                storenames.append(storename)
                if len(storenames)>2:
                    dateCount.append([storenames[-2],data])                
                    #CREATING FILES
                    with open(dataPath+storenames[-2]+'.csv','w') as w: 
                        w.writelines(data)
                data=''
            data+=date+','+count


    for files in glob.glob(dataPath+"*.csv"):       
        # path = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/monthly-car-sales.csv'
        df = read_csv(files, header=0)
        files=files.rsplit('/', 1)[-1]
        # prepare expected column names
        df.columns = ['ds', 'y']
        df['ds']= to_datetime(df['ds'])
        # define eth model
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
        # print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head())
        forecast['Storename']=files.split('\\')[1][:-4]
        ds=pd.DataFrame(forecast[['Storename','ds', 'yhat', 'yhat_lower', 'yhat_upper']])
        ds.to_csv(savefile+files)

        # print(Pdate)
        # plot forecast
        # model.plot(forecast)
        # model.plot_components(forecast)
        # pyplot.subplot()
        # pyplot.show()
    # print(prediction.keys)
    
    for filesd in glob.glob(savefile+"data/*.csv"):
        print(filesd)

    return render(request,'index.html')

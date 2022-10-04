################################################################구간 추출
import numpy as np
import pandas as pd
import os

os.chdir(r'F:\2020\study\03_운전자\SAS_VAR분석\구간나눈데이터')
filelist = os.listdir()

for files in filelist:
    data = pd.read_csv(files)
    data.columns = ['index','up','down','left','right','eye','mouth','y']
    data['y'] = data['y'].astype('int')
    
    
    list1 = list(data[data['y']==1]['index']) if len(data[data['y']==1]['index'])!=0 else [0]
    list2 = list(data[data['y']==2]['index']) if len(data[data['y']==2]['index'])!=0 else [0]
    list3 = list(data[data['y']==3]['index']) if len(data[data['y']==3]['index'])!=0 else [0]

    
    y_list=[]
    y_list.append(list1)    
    y_list.append(list2)    
    y_list.append(list3)    
    
    start, end, y_value= [], [], []
 
    for y_num,listset in enumerate(y_list):
        if listset==[0]:
            continue
        
        start.append(listset[0]+1)
        y_value.append(y_num+1)
        
        for i in range(0,len(listset)-1):
            if (listset[i+1]-listset[i]) != 1:
                end.append(listset[i]+1)
                start.append(listset[i+1]+1)
                y_value.append(y_num+1)
    
        end.append(listset[len(listset)-1]+1)       
       
    
    result = pd.DataFrame(start, columns=['start'])
    result['end'] = end
    result['y'] = y_value
    result = result.sort_values(by=['start'], axis=0)
    result['obs'] = list(i-1 for i in result['start'])
    
    num=[]
    for i,j in zip(result['start'],result['end']):
        num.append(j-i+1)
    result['num'] = num
    
    result = result[['obs','start','end','num','y']]
    result.to_csv(files.replace('.csv','_구간.csv'), index=False)
    
    
#%%
#############################################################y값 별 데이터 생성
import pandas as pd


for dataname in filelist:
    data = pd.read_csv(dataname)
    data.columns = ['index','up','down','left','right','eye','mouth','y']
    data['y'] = data['y'].astype('int')
    data01=data
    data01.loc[data01['y']!=1, 'y'] = 0
    data01.to_csv(dataname.replace('.csv','_주의분산.csv'), index=False)
    
    data = pd.read_csv(dataname)
    data.columns = ['index','up','down','left','right','eye','mouth','y']
    data['y'] = data['y'].astype('int')
    data02=data
    data02.loc[data02['y']!=2, 'y'] = 0
    data02.loc[data02['y']==2, 'y'] = 1
    data02.to_csv(dataname.replace('.csv','_피로.csv'), index=False)
    
    data = pd.read_csv(dataname)
    data.columns = ['index','up','down','left','right','eye','mouth','y']
    data['y'] = data['y'].astype('int')
    data03=data
    data03.loc[data03['y']!=3, 'y'] = 0
    data03.loc[data03['y']==3, 'y'] = 1
    data03.to_csv(dataname.replace('.csv','_졸음.csv'), index=False)
    

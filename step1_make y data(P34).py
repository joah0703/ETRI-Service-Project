# =============================================================================
# label에 y값 추가
# =============================================================================
import os 
import pandas as pd
import numpy as np

os.chdir(r'F:\2020\study\03_운전자\multinom분석\P23_1110') 
data=pd.read_csv('P23_B_2.csv',header=None) #원본데이터 불러오기
y_label=pd.read_csv('P23_feature.csv') #y값 추출된 데이터 불러오기 

result = pd.DataFrame(data=None) #결과 저장할 데이터 프레임

point = np.zeros((len(data))) #y를 표시할 데이터 프레임 
point = pd.DataFrame(point)

#y가 나타나는 구간에 체크
for k in range(0,len(y_label)):
    start = y_label.loc[k,'start']
    end = y_label.loc[k,'end'] 
    point.loc[start:end]=y_label.loc[k,'feature']

point = point.astype(int)

data_value=data.iloc[:,1:4]
result=pd.concat([data_value,point],axis=1)

result.to_csv('P23_y.csv')


#%%
# =============================================================================
# 데이터 밀면서 생성 & 퍼센트 구하기 -> jupyter code
# =============================================================================

# =============================================================================
# onehot encoding
# =============================================================================

#import os 
#import pandas as pd
#import numpy as np

#os.chdir(r'C:\Users\Yurim\Desktop\driver\multinom분석\P31_1차_1030') 
data=pd.read_csv('P34_30sec_data.csv')
del data['Unnamed: 0']
data.columns=['updown','leftright','eye','mouth','y']

for i in range(len(data)):
    if data.loc[i,'updown']<0.05:
        data.loc[i,'updown']=1
    elif data.loc[i,'updown']<0.1:
        data.loc[i,'updown']=2
    elif data.loc[i,'updown']<0.15:
        data.loc[i,'updown']=3
    elif data.loc[i,'updown']<0.2:
        data.loc[i,'updown']=4
    else:
        data.loc[i,'updown']=5
        
    if data.loc[i,'leftright']<0.005:
        data.loc[i,'leftright']=1
    elif data.loc[i,'leftright']<0.01:
        data.loc[i,'leftright']=2
    elif data.loc[i,'leftright']<0.015:
        data.loc[i,'leftright']=3
    elif data.loc[i,'leftright']<0.02:
        data.loc[i,'leftright']=4
    else:
        data.loc[i,'leftright']=5
    
    if data.loc[i,'eye']<0.07:
        data.loc[i,'eye']=1
    elif data.loc[i,'eye']<0.14:
        data.loc[i,'eye']=2
    elif data.loc[i,'eye']<0.21:
        data.loc[i,'eye']=3
    elif data.loc[i,'eye']<0.28:
        data.loc[i,'eye']=4
    else:
        data.loc[i,'eye']=5
        
    if data.loc[i,'mouth']<0.07:
        data.loc[i,'mouth']=1
    elif data.loc[i,'mouth']<0.14:
        data.loc[i,'mouth']=2
    elif data.loc[i,'mouth']<0.21:
        data.loc[i,'mouth']=3
    elif data.loc[i,'mouth']<0.28:
        data.loc[i,'mouth']=4
    else:
        data.loc[i,'mouth']=5
        
updown_class=np.array(data['updown']).reshape(-1,1)
leftright_class=np.array(data['leftright']).reshape(-1,1)
eye_class=np.array(data['eye']).reshape(-1,1)
mouth_class=np.array(data['mouth']).reshape(-1,1)

from sklearn.preprocessing import OneHotEncoder
enc=OneHotEncoder()
enc.fit(updown_class)
updown_onehot=enc.transform(updown_class).toarray()
updown_onehot=pd.DataFrame(updown_onehot)

enc=OneHotEncoder()
enc.fit(leftright_class)
leftright_onehot=enc.transform(leftright_class).toarray()
leftright_onehot=pd.DataFrame(leftright_onehot)

enc=OneHotEncoder()
enc.fit(eye_class)
eye_onehot=enc.transform(eye_class).toarray()
eye_onehot=pd.DataFrame(eye_onehot)

enc=OneHotEncoder()
enc.fit(mouth_class)
mouth_onehot=enc.transform(mouth_class).toarray()
mouth_onehot=pd.DataFrame(mouth_onehot)

Df = pd.concat([updown_onehot,leftright_onehot,eye_onehot,mouth_onehot,data['y']],axis=1)
#Df.to_csv('P31_30sec_multi.csv')


#%%
# =============================================================================
#multinom
# =============================================================================
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:19:01 2020

@author: Yurim
"""

from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import statsmodels.api as sm
import os 
import pandas as pd

data=Df

#os.chdir(r'C:\Users\Yurim\Desktop\driver\multinom분석\P34_1차_1102') 
#data=pd.read_csv('P31_30sec_multi.csv')
#data.drop(data.columns[[0]], axis='columns')
data.columns = ['updown_1', 'updown_2', 'updown_3', 'updown_4', 'updown_5', 'leftright_1', 'leftright_2', 'leftright_3', 'leftright_4', 'leftright_5', 'eye_1', 'eye_2', 'eye_3', 'eye_4', 'eye_5', 'mouth_1', 'mouth_2', 'mouth_3', 'mouth_4', 'mouth_5', 'y']

from sklearn.model_selection import train_test_split
#data=Df
# x(독립변수) y(종속 변수) 분리
index0 = data['y'] == 0
x0 = data[index0]
index1 = data['y'] == 1
x1 = data[index1]
index2 = data['y'] == 2
x2 = data[index2]
index3 = data['y'] == 3
x3 = data[index3]

#sum(x3['eye_5']==1)

df=x0.append(x1)
df=df.reset_index()
x=df.loc[:, 'updown_1':'mouth_5']
y=df.loc[:, 'y']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print(len(x_train))
print(len(x_test))
print(len(y_train))
print(len(y_test))



log_reg = LogisticRegression()
log_reg.fit(x_train, y_train)

 
const = sm.add_constant(x)
model = sm.OLS(y, const)
result = model.fit()
print(result.summary())
 
y_pred = log_reg.predict(x_test)
print(y_pred)
print(list(y_test)) 
print('정확도 :', metrics.accuracy_score(y_test, y_pred))


from sklearn.metrics import confusion_matrix
cf = confusion_matrix(y_test, y_pred)
print(cf)

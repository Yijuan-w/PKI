#-*- coding: utf-8 -*-

import pandas as pd
import numpy as np
#from sklearn import preprocessing

#df = pd.read_csv("4_saver_pcaresult.csv",index_col=0,header=0)
# values=df.values
# values=values.astype("float64")
# values2=preprocessing.scale(values)
# data=pd.DataFrame(values)
# data.columns=df.columns
# data.index=df.index
# data.to_csv("zscore-saver-fpca.csv")

data = pd.read_csv("saverdata2.csv",index_col=0,header=0)

#data = df.apply(np.log1p)

t0 = data.iloc[:, 0:91].mean(1)
t12 = data.iloc[:, 92:193].mean(1)
t24 = data.iloc[:, 194:259].mean(1)
t36 = data.iloc[:, 260:431].mean(1)
t72 = data.iloc[:, 432:569].mean(1)
t96 = data.iloc[:, 570:757].mean(1)
#
# tf = pd.read_csv('setTF.csv', index_col=0,header=0)
#
timedata=pd.concat([t0,t12,t24,t36,t72,t96], axis=1)
#timedata.to_csv("6timedata.csv")
# sixpointdata=pd.DataFrame()

# for i in tf['0']:
#     if i in data._stat_axis.values.tolist():
#         sixpointdata[i]=timedata.loc[i]
# sixpointdata=sixpointdata.T
# #sixpointdata.to_csv("sixpointdata.csv")

def diffdata(dataframe):
    data = pd.DataFrame()
    n=len(dataframe.iloc[0,:])
    for i in range(0,n-1):
        data[i]=dataframe.iloc[:,i+1]-dataframe.iloc[:,i]
    data.to_csv("diffdata.csv")
    return data

#diffdata(sixpointdata)

def process_rel(filename): #rel_f
    relationship = pd.read_csv(filename)
    all_target=[]

    relationship_f=[]

    for i in list(relationship['target']):
        if i not in all_target:
            all_target.append(i)

    for i in all_target:
        one=[]
        one.append(i)
        for j in range(0, len(relationship['target'])):
            if i==relationship["target"][j]:
                one.append(relationship['tf'][j])
                print (one)
        relationship_f.append(one)

    print (relationship_f)
    relationship_f=pd.DataFrame(relationship_f)
    relationship_f.to_csv("relationship_f6.csv")

process_rel("rel_f6.csv")
#diffdata(data)





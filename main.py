import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.responses import FileResponse
import base64


from lib.oracle_list import * 
from lib.data_preprocessing import * 



# initial FastAPI
app = FastAPI()

# post request
class PictureFormat(BaseModel):
    unit_1: str
    uni_num_1: str
    unit_2: str
    uni_num_2: str
    time: str


@app.post("/corr")
def pic_corr(request: PictureFormat):
    user = ""
    password = ""
    sqlStr="SELECT col_1, col_2\
            from Table1\
            INNER JOIN Table_2(Col_3)\
            INNER JOIN Table_3(Col_4)"

    
    initDbLink = Create()
    data = initDbLink.oracle_db(sqlStr,user,password)

    print(data)
    check = "Val"

    select_df_1 = Data_preprocessing(data,request.time,request.unit_1,check,request.uni_num_1)
    T1 = select_df_1.df_revrise() 

    select_df_2 = Data_preprocessing(data,request.time,request.unit_2,check,request.uni_num_2)
    T9 = select_df_2.df_revrise() 

    T19 = pd.concat([T1,T9],axis = 1)
    T19 = T19.fillna(method="ffill")
    T19 = T19.dropna(how='any')

    plt.figure()
    ax = sns.heatmap(T19.corr(),mask=np.triu(np.ones_like(T19.corr())), annot=True, cmap="PiYG")
    plt.title("Correlation", fontdict={'fontsize': 20})
    plt.xticks(rotation= 90)
    datapath = 'pic/'
    plt.savefig(datapath+'_corr.png',bbox_inches = 'tight')

    try :
        image_path = datapath+'_corr.png'
        return FileResponse(image_path)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


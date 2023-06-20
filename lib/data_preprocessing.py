import pandas as pd 

class Data_preprocessing(object):
    def __init__(self,data,time,unit,check,uni_num):
        self.data = data
        self.time = time
        self.unit = unit
        self.check = check
        self.uni_num = uni_num

    def df_revrise(self):
        ori = self.data.dropna()
        time_col = pd.to_datetime(ori[""]+" "+ori[""]).to_frame()
        time_col.rename(columns={0:"Time"},inplace=True)
        ans = pd.concat([time_col,ori],axis=1)
        ans = ans.sort_values(["Time"]) 
        ans = ans[ans.Time > self.time]
        ans = ans.drop_duplicates() 
        ans = ans[ans.U == self.unit]
        ans = ans[ans.C == self.check]
        ans = ans[ans.U == self.uni_num]
        ans = ans.sort_values(["Time"])
        # pivot
        ans['name'] = ans['']+"_"+ans['']
        ans = pd.pivot_table(ans,values='C',index='Time',columns='name')
        return ans

if __name__ == '__main__': 
    data =    
    time = ""
    #unit = ""   
    #check = ""
    #uni_num = ""
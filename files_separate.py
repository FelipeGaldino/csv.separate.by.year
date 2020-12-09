import pandas as pd #
import os 

SIZE  = "10"
TYPE  = "Ask"
STOCK = "btcusd"

years_list = ("2017","2018","2019","2020","2017-2018","2018-2019",\
              "2019-2020","2017-2018-2019","2018-2019-2020","2017-2018-2019-2020")

data = pd.read_csv(SIZE+"/"+STOCK+"_"+TYPE+"_"+SIZE+".csv")
data["timestamp"] = pd.to_datetime(data["timestamp"])

def generate_files(years):
    
    if len(years) == 4: 
        
        path_file = SIZE+"/"+years+"/"
        uni_year = int(years)
        
        novo = data.loc[data["timestamp"].dt.year == uni_year]
        novo.to_csv(path_file+"/"+years+"_"+STOCK+"_"+TYPE+"_"+SIZE+".csv",index=False)
      
    if len(years) == 9: 
        print(years)    
        one_year = years[:4]
        two_year = years[5:]
        
        data_one = pd.read_csv(SIZE+"/"+one_year+"/"+one_year+"_"+STOCK+"_"+TYPE+"_"+SIZE+".csv")
        data_two = pd.read_csv(SIZE+"/"+two_year+"/"+two_year+"_"+STOCK+"_"+TYPE+"_"+SIZE+".csv")
            
        frames = [data_one, data_two]
        result = pd.concat(frames)
        
        result.to_csv(SIZE+"/"+one_year+"-"+two_year+"/"
                          +one_year+"-"+two_year+"_"+STOCK+"_"+TYPE+"_"+SIZE+".csv",index=False)

    if len(years) == 14:  
        one_year  = years[:4]
        two_year  = years[5:9]
        thre_year = years[10:]

        data_one  = pd.read_csv(SIZE+"/"+one_year+"/"+one_year+"_"+STOCK+"_"+TYPE+"_"+SIZE+".csv")
        data_two  = pd.read_csv(SIZE+"/"+two_year+"/"+two_year+"_"+STOCK+"_"+TYPE+"_"+SIZE+".csv")
        data_thre = pd.read_csv(SIZE+"/"+thre_year+"/"+thre_year+"_"+STOCK+"_"+TYPE+"_"+SIZE+".csv")
            
        frames = [data_one, data_two, data_thre]
        result = pd.concat(frames)
        result.to_csv(SIZE+"/"+one_year+"-"+two_year+"-"+thre_year+"/"
                              +one_year+"-"+two_year+"-"+thre_year+"_"
                              +STOCK+"_"+TYPE+"_"+SIZE+".csv",index=False)

    if len(years) == 19: 
        print(years) 
        one_year  = years[:4]
        two_year  = years[5:9]
        thre_year = years[10:14]
        four_year = years[15:]
        
        data_one  = pd.read_csv(SIZE+"/"+one_year+"/"+one_year+"_btcusd_"+TYPE+"_"+SIZE+".csv")
        data_two  = pd.read_csv(SIZE+"/"+two_year+"/"+two_year+"_btcusd_"+TYPE+"_"+SIZE+".csv")
        data_thre = pd.read_csv(SIZE+"/"+thre_year+"/"+thre_year+"_btcusd_"+TYPE+"_"+SIZE+".csv")
        data_four = pd.read_csv(SIZE+"/"+four_year+"/"+four_year+"_btcusd_"+TYPE+"_"+SIZE+".csv")
        
        frames = [data_one, data_two, data_thre, data_four]
        result = pd.concat(frames)
        result.to_csv(SIZE+"/"+one_year+"-"+two_year+"-"+thre_year+"-"
                              +four_year+"/"+one_year+"-"+two_year+"-"
                              +thre_year+"-"+four_year+"_btcusd_"+TYPE+"_"+SIZE+".csv",index=False)

if __name__ == '__main__':

    for year_ in years_list:
        path_file = SIZE+"/"+year_+"/"
        
        if os.path.exists(path_file) == False:
            os.makedirs(path_file)  
            
        generate_files(year_)
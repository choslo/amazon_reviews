import pandas as pd 

def prepare_data(): 
    df = pd.read_json("data/art.json.gz.zip", lines= True, compression= "gzip")
    
    return df
    
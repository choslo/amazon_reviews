import pandas as pd
import os


def get_data(nb_label):
    
    # Get the data
    df = pd.read_json("data/art.json.gz.zip", lines= True, compression= "gzip")
    
    # Convert the type of columns 
    text_var = ('summary', 'reviewText', 'style', 'image')
    num_var = ('vote', 'asin')
    date_var = ('reviewTime')

    for var in text_var:
        df[var] = df[var].astype(str)
    for k in num_var:
        df[var] = pd.to_numeric(df[var], errors='coerce')
    for j in date_var:
        df[var] = pd.to_datetime(df[var])


    df['reviewTime'] = pd.to_datetime(df.reviewTime)
    df['vote'] = pd.to_numeric(df['vote'], errors='coerce')
    #df = df.drop('asin', axis= 'columns')
    
    # We drop the variable image because we have 97% of missing data 
    df = df.drop('image', axis= 'columns')
   
    # Create the target variable 
    
    if nb_label == 3: 
        label = ['positive' if df.overall[i] == 5 else 'neutral' if df.overall[i] == 4 else 'negative' for i in range(len(df.overall))]
        df['label'] = label

    return df
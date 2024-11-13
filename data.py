# curl -X GET "https://datasets-server.huggingface.co/rows?dataset=Biddls%2FOnion_News&config=default&split=train&offset=0&length=100" > onion.parquet
#!pip3 install fastparquet
#!pip3 install pyarrow

import pyarrow, fastparquet
import pandas as pd

# Read in Data
df = pd.read_parquet("onion.parquet")

# Take only headers
df['text'] = df['text'].str.split(' #~#').str[0]

# Convert text column into list 
d = list(df['text']) 
  
# Join with each row value as new line
e = '\n'.join(map(str, d))

# Export as text file (run .py to save output as text)
# python3 data.py > onion.txt
print(e)
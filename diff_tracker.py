import pandas as pd
import os
import time
import pandas as pd
import sys
import re
import schedule
from datetime import datetime
import random
"""
Program tracks difficulty for drops < 20% of avg hashrate from the past 10 mins
On difficulty drops it notifies discord of mining opportunity.
emptys all dirs on start
"""
def job():

    #stores groupby dfs
    dfs =[]
    #pool dict with links
    pool_list = {'angrypool': 'http://angrypool.com/explorer'}
    #takes from html table returns grouped df
    def getdif(url,pool):
        difTable = pd.read_html(url)
        difTable = difTable[0]
        diftable = difTable.dropna(axis=1, how='all')
        difTable = difTable.groupby(['Algo'])
        return difTable

    #loop through pool list add grouped dfs to dfs array
    for key, value in pool_list.items():
    	data = getdif(value)
    	dfs.append(data)

    algoHash ={'x11':1000000000000, 'scrypt': 1000000000000, 'neoscrypt': 1000000000, 'lyra2v2': 1000000000000,'lyra2z': 1000000000000}
    #loop through algos write to file
    for i,pool in enumerate(pool_list.keys()):
        path = "C:\\Users\\me\\Documents\\Scripts\\diffData\\"+str(pool)+"\\"
        for df in dfs:
            for algo in algoHash.keys():
                curr_folder = path+algo
                print(curr_folder)
                filename =curr_folder+"\\"+time.strftime("%M")+".csv"
                df.get_group(algo).to_csv(filename)
                #print(algo,"\n",df.get_group(algo),"\n---\n")
    sys.stdout.write("job done!\n")
    sys.stdout.flush()
t = random.randint(15,20)
schedule.every(t).seconds.do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)


# To clear all functions
# schedule.clear()
#C:\Users\me\Documents\Scriptspython tasktest.py

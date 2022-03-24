import numpy as np
import pandas as pd
import itertools
import random
from random import randrange
from pandas import ExcelWriter
import os

import sampleGenerator as sg

if os.path.isfile(./longInputFile.xls) == True:
    df =  pd.read_excel(longInputFile.xslx)
elif sg.sampleGenerator():
    df = pd.read_excel(sampleLong.xslx)


#groupy commodities in different sheets 
commodities =(
'Tea',
'Tobacco',
'Coffee',
'Cinnamon'
)
sales = (
'bae',
'sie'
)

toBeIterated = list(itertools.product(commodities, sales))

x,y = (0,0)
salesByGroupList =[]
salesByTransportedList =[]
salesByInvestmentList =[]
productByGroupAndConsentedList =[]
meanPriceByGroupList =[]
meanPriceByTransportedList =[]
totalSalesByConsentedList =[]
sheetNames =[]

for i in range(len(toBeIterated)):
    
    x,y = toBeIterated[i]
    
    salesByGroup = df[df['commodity']==x].pivot_table(
    index =['state'], 
    columns =['group'],
    values =y,
    aggfunc='sum'
    )
    salesByTransported = df[df['commodity']==x].pivot_table(
    index =['state'], 
    columns =['transported'],
    values =y,
    aggfunc='sum'
    )
    salesByInvestment = df[df['commodity']==x].pivot_table(
    index =['state'], 
    columns =['investment'],
    values =y,
    aggfunc='sum'
    )
    
    # productByGroupAndConsented = df[df['commodity']==x].pivot_table(
    # columns =['group', 'consent'],
    # values = ['product']    
    # )
    
    meanPriceByGroup = df[df['commodity']==x].pivot_table(
    index =['group'], 
    columns =['investment'],
    values =['price'],
    aggfunc='mean'
    )
    meanPriceByTransported = df.pivot_table(
    index =['transported'], 
    columns =['investment'],
    values =['price'],
    aggfunc='mean'
    )
    
    totalSalesByConsented = df[df['commodity']==x].pivot_table(
    index =['consent'], 
    values =y,
    aggfunc='sum'
    )
    
    salesByGroupList.append(salesByGroup)
    salesByTransportedList.append(salesByTransported)
    salesByInvestmentList.append(salesByInvestment)
    productByGroupAndConsentedList.append(productByGroupAndConsented)
    meanPriceByGroupList.append(meanPriceByGroup)
    meanPriceByTransportedList.append(meanPriceByTransported)
    totalSalesByConsentedList.append(totalSalesByConsented)
    sheetName = str(x+'-'+y)
    sheetNames.append(sheetName)
    #the format can be changed with startrow & startcol
    with ExcelWriter('./specific.xlsx') as writer:
        for i in range(len(salesByGroupList)):
            salesByGroupList[i].to_excel(writer, sheet_name=sheetNames[i], startrow=3, startcol=1)
            salesByTransportedList[i].to_excel(writer, sheet_name=sheetNames[i], startrow=3, startcol=6)
            salesByInvestmentList[i].to_excel(writer, sheet_name=sheetNames[i], startrow=3, startcol=11)
            productByGroupAndConsentedList[i].to_excel(writer, sheet_name=sheetNames[i], startrow=3, startcol=16)
            meanPriceByGroupList[i].to_excel(writer, sheet_name=sheetNames[i], startrow=3, startcol=25)
            meanPriceByTransportedList[i].to_excel(writer, sheet_name=sheetNames[i], startrow=11, startcol=25)
            totalSalesByConsentedList[i].to_excel(writer, sheet_name=sheetNames[i], startrow=35, startcol=5)
            
    #summary of sales per commodity per state
    with ExcelWriter("./specific.xlsx", mode="a", engine="openpyxl") as writer:

        df.pivot_table(
        index =['state'],
        columns =['commodity', 'consent'], 
        values =['sie'],
        aggfunc='sum'
        ).to_excel(writer, sheet_name="Summary")


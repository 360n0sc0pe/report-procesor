import numpy as np
import pandas as pd
import random


#generate data

def sampleGenerator():

    rows = 1000

    longData = []

    for row in range(rows):
        #if you need date then uncommented:
        #year = random.choice(["1705", "1706", "1707"])
        #month = random.choice(["oct", "nov", "dec"]) 
        state = random.choice([

        "Kabul", 
        "Kandahar", 
        "Delhic",
        "Kalingar",
        "Peshawar",
        "Jodhpur",
        "Udaipur",
        "Ujjain",
        "Jodhia",
        "Salaxu",
        "Somnath",
        "Daman",
        "Bassein",
        "Chaul",
        "Salsette",
        "Burhampur",
        "Munadganar",
        "Golconda",
        "Masulipatam",
        "Gon",
        "Kolhapur",
        "Pondicherry",
        "Sadras",
        "Dacon",
        "Negapatam",
        "Pulicat",

        ])

    #Categories to group
        group = random.choice(["Arabic", "Asian", "Indian"])
        transported = random.choice(["Monsoon", "Crate", "Barrel"])
        investment = random.choice(["I", "II", "III"])
    #products 
        commodity = random.choice(["Tea", "Coffee", "Cinnamon", "Tobacco"])
    #trade consented by ruler group
        consent = random.choice(["Maratha", "Mughal", "Local", "None"])
    #factory of origin
        product = random.choice(["FactoryA", "FactoryB", "FactoryC", "FactoryD"])    
    #amount bought at east
        bae = np.random.randint(10,100)
    #amount actually sold in europe, for simplicy, consider 80% of total
        sie = bae*0.8
    #price paid in the transaction
        price = np.random.randint(10000, 100000)
        
        longData.append([commodity, product, consent, investment, group, transported, state, bae, sie, price
        #month, year
        ])

    df = pd.DataFrame(longData, columns=[
    'commodity',
    'product',
    'consent', 
    'investment',
    'group',
    'transported',
    'state',
    'bae',
    'sie',
    'price',
    #'month', 'year'
    ]) 
                
    df.to_excel("./sampleLong.xlsx")  

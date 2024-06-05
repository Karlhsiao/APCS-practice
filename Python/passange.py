import pandas as pd
import numpy as np
from scipy.stats import levene
from scipy.stats import f_oneway

from random import randint
#Create samples

def random_gen(start, end):
    data = []
    for _ in range(10):
        data.append(randint(start, end))

    return data

df = pd.DataFrame({
    "台北":random_gen(0, 30),
    "台中":random_gen(20, 50),
    "澎湖":random_gen(40, 70),
    "台南":random_gen(60, 100)
})

#levene's test
statistic, p_value=levene(df["台北"], df["台中"], df["澎湖"], df["台南"])
print(df["台北"], "\n", df["台中"], "\n", df["澎湖"], "\n", df["台南"])
print("同質性檢定")
print('statistic:%.2f'%statistic)
print('p_value:%.2f'%p_value)

print("Anova檢定")
f_statistic, p_value = f_oneway(df["台北"],  df["台中"], df["澎湖"], df["台南"])
print("f_statistic:%.2f"%f_statistic)
print("p_value:%.2f"%p_value)
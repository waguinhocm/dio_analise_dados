import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)
print(df.head())
print(df.info())

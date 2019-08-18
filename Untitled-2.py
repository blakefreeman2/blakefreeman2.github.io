import numpy as np
import pandas as pd
from pandas import *

file_one = "CSV/cities.csv"
file_one_df = pd.read_csv(file_one)

file_one_df.to_html('file_one.html')

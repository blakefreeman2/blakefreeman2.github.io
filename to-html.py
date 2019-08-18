import numpy as np
import pandas as pd

file1 = "CSV/cities.csv"

file1_df = pd.read_csv(file1)
file1_df.to_html('file_one.html')

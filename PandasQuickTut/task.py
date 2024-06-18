import numpy as np
import pandas as pd

data = np.random.randint(0,101,size=(3,4))
column_names = ["Eleanor","Chidi","Tahani","Jason"]

df = pd.DataFrame(data=data,columns=column_names)
df["Janet"] = df["Tahani"]+df["Jason"]
print(df)
print(df["Eleanor"][1])
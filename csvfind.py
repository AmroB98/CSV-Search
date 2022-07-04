import glob
import pandas as pd
import os
import sys

path = sys.argv[0]
# check if path is valid
if not (os.path.isfile(path)):
    print("Given path is not valid")
    quit("program terminated")
# loop over all CSV files in directory
files = glob.glob(path + "/*.csv")

# store data
frame = pd.DataFrame()
content = []

for filename in files:
    df = pd.read_csv(filename, index_col=None)
    content.append(df)

# convert it to pandas matrix
data_frame = pd.concat(content)
print(data_frame)

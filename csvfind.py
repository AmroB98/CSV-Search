import csv
import os
import sys
import glob
import time
import random

mylist = []
# for i in range (700):
#     mylist.append(random.randrange(100,200))
# get command line arguments
path = sys.argv[1]
target_column = sys.argv[2]
target_str = sys.argv[3]
mylist = []

# set path
os.chdir(path)
isFolder = os.path.exists("output")
if not isFolder:
    os.mkdir("output")
if not os.path.exists("data"):
    os.mkdir("data")
if not os.path.exists("list"):
    os.mkdir("list")

if os.path.exists('output/output.csv'):
    inp = input("output.csv file already exist in output folder, Do you want to overwrite it? [Y/N]")
    if inp == "Y" or inp == "y":
        os.remove("output/output.csv")
    else:
        quit("Terminated.")

start_time = time.time()
with open('list/list.csv', 'r') as infile:
    #infile_object = csv.reader(infile)
    reader = csv.reader(infile)
    for rows in reader:
        print(rows[0])
        mylist.append(rows[0])

files = glob.glob('data/*.csv')
count = 0
for file in files:
    print("Proccessing file: " + file)
    with open(file) as cf:
        ob = csv.reader(cf)

        for rows in ob:
            for i in mylist:
                if rows[int(target_column)] == str(i).casefold():
                    count += 1
                    with open('output/output.csv', 'a', newline="") as outfile:
                        print("writing target row #" + str(count))
                        writer = csv.writer(outfile)
                        writer.writerow(rows)
                        outfile.close()
print("Total Targets found: " + str(count))
print("Execution time:  %.2f seconds " % (time.time() - start_time))

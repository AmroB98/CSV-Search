import csv
import os
import sys
import glob
import time
import random

print(len(sys.argv))

# default parameters
path = ""
target_column = 0
mylist = []


def print_help():
    print("to create root folder use command:\n     $ python csvfind [working directory] --init\ndata,lists,and output "
          "files will be created, \n ** if no directory was specified the current directory will be treated as root")


def init(pth):
    if not os.path.exists("output"):
        os.mkdir("output")
        if pth != "":
            print("output file created in current directory")
        else:
            print("output file created in " + str(pth))
    else:
        print("output file already exists in " + str(pth))
    if not os.path.exists("data"):
        os.mkdir("data")
        if pth != "":
            print("data file created in current directory")
        else:
            print("data file created in " + str(pth))
    else:
        print("data file already exists in " + str(pth))
    if not os.path.exists("lists"):
        os.mkdir("lists")
        if pth != "":
            print("lists file created in current directory")
        else:
            print("lists file created in " + str(pth))
    else:
        print("lists file already exists in " + str(pth))
    exit()


# command line options
if len(sys.argv) < 2:
    print_help()
    exit()
if "--init" in sys.argv and len(sys.argv) < 3:
    init(path)
elif "--init" in sys.argv and len(sys.argv) == 3:

    path = sys.argv[2]
    try:

        os.chdir(path)
    except:
        print("Invalid command-line input, Check usage: ")
        print_help()
        exit()
    init(path)
else:
    print("Invalid command-line inputs")
    print_help()
    exit()
# path = sys.argv[1]
# target_column = sys.argv[2]
# target_str = sys.argv[3]
mylist = []

# set path
os.chdir(path)
# if main files are missing from root directory
if not os.path.exists("output") or not os.path.exists("data") or not os.path.exists("lists"):
    print("main folders missing, use --init command to initialize main folders")
    print_help()

# Note: instead of overwriting output, add a new numbered file.
if os.path.exists('output/output.csv'):
    inp = input("output.csv file already exist in output folder, Do you want to overwrite it? [Y/N]")
    if inp == "Y" or inp == "y":
        os.remove("output/output.csv")
    else:
        quit("Terminated.")

start_time = time.time()
with open('list/list.csv', 'r') as infile:
    # infile_object = csv.reader(infile)
    reader = csv.reader(infile)
    for rows in reader:
        print(rows[0])
        mylist.append(rows[0])

files = glob.glob('data/*.csv')
count = 0
for file in files:
    print("Processing file: " + file)
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

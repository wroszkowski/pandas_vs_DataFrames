import pandas as pd
import time
import sys
import csv

path = sys.argv[1]


# define functions
def f_load_csv(path=path + 'data.csv'):
    t0 = time.time()
    df = pd.read_csv(path, sep=',')
    t1 = time.time() - t0
    return [df, t1]


def f_group_by(df, by=[]):
    t0 = time.time()
    df.groupby(by).sum()
    t1 = time.time() - t0
    return t1


def f_sort(df, by=[]):
    t0 = time.time()
    df.sort_values(by=by, inplace=True)
    t1 = time.time() - t0
    return t1


# load csv
load_csv_meta = f_load_csv(path=path + 'data.csv')
df = load_csv_meta[0]

load_time = load_csv_meta[1]
groupby_time = f_group_by(df=df, by=['key'])
sort_time = f_sort(df=df, by=['key'])

# print results
print('\nResults for Python script:')
print('Load csv execution time: ' + str(load_time))
print('Grouping execution time: ' + str(groupby_time))
print('Sort execution time: ' + str(sort_time))

# save csv ith results
results = [load_time, groupby_time, sort_time]
with open(path + "output_python.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(['load_time', 'groupby_time', 'sort_time'])
    writer.writerow(results)

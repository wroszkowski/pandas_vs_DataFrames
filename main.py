import pandas as pd
import subprocess as subp
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns

path = 'C:\\Users\\roszk\\PycharmProjects\\julia_sgh\\project\\'

# scripts in other files using one master python file
julia_exec = 'julia '
julia_file = 'script.jl'
python_exec = 'python '
python_file = 'script.py'

# data preparation
t0 = time.time()
data_min = 0
data_max = 10000000
n = 200000000

# create data
keys = np.random.randint(data_min, data_max, n)
values = np.random.normal(size=n)

df = pd.DataFrame()
df["key"] = keys
df["value"] = values

# save csv
df.to_csv(path + '/data.csv', index=False, encoding='utf-8')

t1 = time.time() - t0
print('Data prepared in {0} seconds'.format(t1))

# a = subp.check_output(str(python_exec + path + python_file + ' ' + path), shell=True)
a = subp.check_call(str(python_exec + path + python_file + ' ' + path), shell=True)
# b = subp.check_output(str(julia_exec + path.replace('/','\\') + julia_file), shell=True)
b = subp.check_call(str(julia_exec + path + julia_file + ' ' + path), shell=True)

# read results
results_df = pd.DataFrame()
for lang in ['python', 'julia']:
    results = pd.read_csv(path + 'output_{}.csv'.format(lang), sep=',')
    results['lang'] = lang
    results_df = pd.concat([results_df, results], ignore_index=True)

# plot results
plt.rcParams['figure.figsize'] = (9, 7)
sns.set_palette("muted")
sns.set(font_scale=1.2)
sns.set_style('whitegrid', {'font.family': 'serif', 'font.serif': 'Times New Roman'})

for col in ['load_time', 'groupby_time', 'sort_time']:
    sns.barplot(x=results_df[col], y=results_df.lang, palette="muted"
                ).set(title=col, xlabel=col)
    plt.savefig(path + 'charts\\' + col + '_{}'.format(str(int(n / 1000))) + 'k')
    # plt.show()
    plt.close()

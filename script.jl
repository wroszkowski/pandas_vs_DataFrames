using DataFrames
using CSV

path = ARGS[1]

function f_load_csv(p)
    t = @elapsed df = readtable(p * "data.csv")
    return df, t
end

# load csv
load_csv_meta = f_load_csv(path)
df = load_csv_meta[1]

load_time = load_csv_meta[2]
groupby_time = @elapsed by(df, :key, x -> sum(x[:value]))
sort_time = @elapsed sort!(df, :key)

# print results
print("\nResults for Julia script: ")
print("\nLoad csv execution time: " * string(load_time))
print("\nGrouping execution time: " * string(groupby_time))
print("\nSort execution time: " * string(sort_time))


# save csv ith results
results = DataFrame(load_time = load_time, groupby_time = groupby_time, sort_time = sort_time)

CSV.write(path *"output_julia.csv", results)


# function f_group_by(df, group_by=[], sum_by=[]):
#     t = @elapsed
#     by(df, group_by, x -> sum(x[sum_by]))
#     return t
# end

# group_by = [:key]
# sum_by = [:value]

# by(df, group_by, x -> sum(x[sum_by]))


# function f_sort(df, by=[]):
#     t = @elapsed
#     return t
# end






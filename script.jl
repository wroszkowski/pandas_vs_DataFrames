using DataFrames
using CSV

path = ARGS[1]

function f_load_csv(p)
    t = @elapsed df = CSV.read(p * "data.csv")
    return df, t
end

# load csv
load_csv_meta = f_load_csv(path)
df = load_csv_meta[1]

disallowmissing!(df)

load_time = load_csv_meta[2]
groupby_time = @elapsed by(df, :key, value_sum = :value => sum)
sort_time = @elapsed sort!(df, :key)

# print results
print("\nResults for Julia script: ")
print("\nLoad csv execution time: " * string(load_time))
print("\nGrouping execution time: " * string(groupby_time))
print("\nSort execution time: " * string(sort_time))


# save csv ith results
results = DataFrame(load_time = load_time, groupby_time = groupby_time, sort_time = sort_time)

CSV.write(path *"output_julia.csv", results)



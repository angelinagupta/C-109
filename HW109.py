import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly
import statistics

df = pd.read_csv(r"D:\code\python\108\dataC-108.csv", "r")

height_list = df["height"].to_list()
weight_list = df["Weight"].to_list()

height_mean = statistics.mean(height_list)
height_median = statistics.median(height_list)
height_mode = statistics.mode(height_list)

height_std = statistics.stdev(height_list)
weight_mean = statistics.mean(weight_list)
weight_median = statistics.median(weight_list)
weight_mode = statistics.mode(weight_list)

print("mean, median and mode of height is {}, {} and{} respectively.", format(height_mean, height_median, height_mode))
print("mean, median and mode of weight is {}, {} and{} respectively.", format(weight_mean, weight_median, weight_mode))


height_first_std_deviation_start, height_first_std_deviation_end = height_mean-height_std, height_mean+height_std
height_second_std_deviation_start, height_second_std_deviation_end = height_mean-(2*height_std), height_mean+(2*height_std)
height_third_std_deviation_start, height_third_std_deviation_end = height_mean-(3*height_std), height_mean+(3*height_std)

height_list_of_data_within_1_std_deviation = [result for result in height_list if result > height_first_std_deviation_start and result < height_first_std_deviation_end]
height_list_of_data_within_2_std_deviation = [result for result in height_list if result > height_second_std_deviation_start and result < height_second_std_deviation_end]
height_list_of_data_within_3_std_deviation = [result for result in height_list if result > height_third_std_deviation_start and result < height_third_std_deviation_end]


print("{}% of data for height lies within 1 standard deviation ", format(len(height_list_of_data_within_1_std_deviation)*100.0/ len(height_list)))
print("{}% of data for height lies within 2 standard deviation ", format(len(height_list_of_data_within_2_std_deviation)*100.0/ len(height_list)))
print("{}% of data for height lies within 3 standard deviation ", format(len(height_list_of_data_within_3_std_deviation)*100.0/ len(height_list)))

import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], [] 
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = row[1]
        highs.append(high)

   # 根据数据绘制图形
    fig = plt.figure(dpi = 128, figsize = (10, 6))
    plt.plot(dates, highs, c = 'red')

    # 设置图形的格式
    plt.title("Daily high temperatures - 2014", fontsize = 24)
    # plt.title("Daily high temperatures, July 2014", fontsize=24)
    plt.xlabel('', fontsize = 16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize = 16) 
    plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
    plt.show()

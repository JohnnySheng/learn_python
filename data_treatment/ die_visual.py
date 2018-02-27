import pygal
from die import Die

# 创建一个D6
die1 = Die()
die2 = Die()

results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll() 
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides

for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Result of rolling one D6 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9','10','11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual2.svg')
# print(frequencies)


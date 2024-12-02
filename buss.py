a = """12 2
2
12 14 10
12 20 100"""

raw_to_pure = {}
data_list = []

for row in a.split('\n'):
    data_list.append(row)
    words = row.split(" ")

the_time = {"hour": data_list[0].split()[0], "minute": data_list[0].split()[1]}
number_of_stops = data_list[1]

for index, value in enumerate(data_list):
    if index == 0:
        the_time = {"hour": value.split()[0], "minute": value.split()[1]}
        print(the_time)
    if index == 1:
        number_of_stops = value
        print(number_of_stops)
    elif index > 1:
        print(value)

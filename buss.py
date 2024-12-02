a = """12 2
2
12 14 10
12 20 100"""

raw_to_pure = {}
data_list = []
the_time = {"hour": 0, "minute":0}
for row in a.split('\n'):
    data_list.append(row)
    words = row.split(" ")

for element in data_list:

    print(element.split())

print(data_list)

# This is a sample Python script.
import csv
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


with open("jobs_dataset_dup.csv") as file:
    reader = csv.reader(file)
    data = []
    for row in reader:
        data.append(row)

        # if count > 8:
        #     break
    # numbers_to_search = data[1:][0][1:6]
data_to_search_from = data[1:]
for i, item in enumerate(data_to_search_from):
    print(item)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

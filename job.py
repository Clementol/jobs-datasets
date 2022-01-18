import csv


def get_csv_data():
    with open("jobs_dataset_dup.csv") as file:
        reader = csv.reader(file)
        count = 0
        data = []
        for row in reader:
            count += 1
            data.append(row)

            # if count > 8:
            #     break
    numbers_to_search = data[1:][1][1:6]
    data_to_search_from = data[1:]
    #  print(data[1:])
    search_data(numbers_to_search, data_to_search_from)


def search_data(numbers_to_search, data_to_search_from):
    print(numbers_to_search)
    counts = 0
    for index, item in enumerate(data_to_search_from):
        if numbers_to_search == item[1:6]:
            counts += 1
    print(counts, numbers_to_search)
    # print(data_to_search_from[0][-2])


get_csv_data()

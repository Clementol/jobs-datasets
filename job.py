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
    # numbers_to_search = data[1:][0][1:6]
    data_to_search_from = data[1:]
    # for i in range(len(data_to_search_from)):
    numbers_to_search = data_to_search_from[0][1:6]
    counts = 0
    search_data(numbers_to_search, data_to_search_from, counts)


def search_data(numbers_to_search, data_to_search_from, counts):
    # print(numbers_to_search)
    # counts = 0
    # data_to_search_from = data_to_search_from
    md = data_to_search_from
    for index, item in enumerate(data_to_search_from):
        if numbers_to_search == item[1:6]:
            counts += 1
            md[index][-1] = 0
            # print(index, md[index])
            data_to_search_from.pop(index)
            # del data_to_search_from[index]

    print(counts, numbers_to_search, len(data_to_search_from))

    if len(data_to_search_from) > 0:
        next_row_to_search = data_to_search_from[0][1:6]
        counts = 0
        search_data(next_row_to_search, data_to_search_from, counts)


get_csv_data()

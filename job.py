import csv


def get_csv_data():
    with open("jobs_dataset_dup.csv") as file:
        reader = csv.reader(file)
        data = []
        count = 0
        for row in reader:
            count += 1
            data.append(row)

            # if count > 814:
            #     break
    # numbers_to_search = data[1:][0][1:6]
    data_to_search_from = data[1:]
    # for i in range(len(data_to_search_from)):
    numbers_to_search = data_to_search_from[1][1:6]
    counts = 0
    position = 0
    search_data(numbers_to_search, data_to_search_from, counts, position)


def search_data(numbers_to_search, data_to_search_from, counts, position):
    # print(numbers_to_search)
    modified_data = []

    data_to_search_from = data_to_search_from
    # md = data_to_search_from
    for index, item in enumerate(data_to_search_from):
        if numbers_to_search == item[1:6]:
            counts += 1
            item[-1] = position
            modified_data.append(item)
            data_to_search_from.pop(index)
            # del data_to_search_from[index]

    print(counts, numbers_to_search, len(data_to_search_from))

    if position == 0:
        return
    if len(data_to_search_from) > 0:
        position += 1
        next_row_to_search = data_to_search_from[0][1:6]
        counts = 0
        search_data(next_row_to_search, data_to_search_from, counts, position)
    # print(modified_data)


get_csv_data()

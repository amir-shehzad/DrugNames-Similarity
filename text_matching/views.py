from django.shortcuts import render
from difflib import SequenceMatcher
import csv
import os

directory = os.getcwd()

file_name = directory + '/text_matching/inputs/' + "Dummy-medical-dataset.csv"


def read_csv_file(file_name):
    """Read CSV file and return keys and values column"""
    keys = []
    values = []
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        _ = next(reader)

        for row in reader:
            if row[0]:  # key
                keys.append(row[0])
            if row[1]:  # value
                values.append(row[1])

    return keys, values


def list_keys(request):
    if request.method == "GET":
        keys, values = read_csv_file(file_name)
        context = {"keys": keys}

        return render(request, "index.html", context)


def similar(str_1, str_2):
    return SequenceMatcher(None, str_1, str_2).ratio()


def search_similar_values(request):
    query = request.GET.get("query")

    keys, values = read_csv_file(file_name)

    matched_values = []
    for value in values:
        print(f"query: {query}  ---->  value: {value}")
        matching_px = similar(query, value)
        if query.split()[0] in value and matching_px > 0.5:
            matched_values.append((value, f"{matching_px * 100 :.2f} %"))

    context = {
        "keys": keys,
        "query": query,
        "matched_values": matched_values,
    }

    return render(request, "index.html", context)


# print(len(read_csv_file(file_name)[1]))
read_csv_file(file_name)
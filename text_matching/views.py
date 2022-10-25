from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle
from difflib import SequenceMatcher
import csv
import os

directory = os.getcwd()
file_name = directory + "/text_matching/inputs/" + "Dummy-medical-dataset.csv"


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


class HomePage(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    throttle_classes = [AnonRateThrottle]

    template_name = "index.html"
    keys, values = read_csv_file(file_name)

    def get(self, request):
        """Gets Keys, Values Columns from CSV file, Shows as dropdown in template"""
        context = {"keys": self.keys}

        return Response(context)


class SearchView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    throttle_classes = [AnonRateThrottle]

    template_name = "index.html"
    keys, values = read_csv_file(file_name)

    def similar(self, str_1, str_2):
        return SequenceMatcher(None, str_1, str_2).ratio()

    def get(self, request):
        """Searches for similar values against selected Key in DropDown interface"""
        query = request.GET.get("query")

        if query:
            matched_values = []
            for value in self.values:
                matching_px = self.similar(query, value)
                # if key's first substring is not present in value string
                # it means main part of key is not present
                if query.split()[0] in value and matching_px > 0.5:
                    matched_values.append((value, f"{matching_px * 100 :.2f} %"))

            context = {
                "keys": self.keys,
                "query": query,
                "matched_values": matched_values,
            }

        else:
            context = {
                "keys": self.keys,
            }

        return Response(context)

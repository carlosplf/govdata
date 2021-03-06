import json
import csv


class CSVConverter():
    def __init__(self):
        pass

    def csv_to_dict(self, filename):
        """
        Convert a CSV to a dict.
        Args:
            filename: (str) filename.
        """
        data = {}
        with open(filename, encoding='ISO-8859-1') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=";")
            primary_key = 0
            for rows in csv_reader:
                data[str(primary_key)] = rows
                primary_key += 1
        return data
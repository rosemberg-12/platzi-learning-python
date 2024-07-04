import csv
from typing import Dict, List


def read_csv(path) -> List:
    with open(path, "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        return [row for row in reader]


if __name__ == "__main__":
    data = read_csv("src/csv/data.csv")
    print(data[0])

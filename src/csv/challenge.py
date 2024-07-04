import csv
from dataclasses import dataclass
from typing import Dict, List, Tuple, Union

from matplotlib import pyplot as plt

MAPPER: Dict[str, str] = {
    "1970": "1970 Population",
    "1980": "1980 Population",
    "1990": "1990 Population",
    "2000": "2000 Population",
    "2010": "2010 Population",
    "2015": "2015 Population",
    "2020": "2020 Population",
}

POPULATION_INDEX = "World Population Percentage"
COUNTRY_INDEX = "Country"


def generate_bar_chart_by_country(country: str, csv_path: str) -> None:
    with open(csv_path, mode="r") as csv_reader:
        csv_reader = csv.reader(csv_reader, delimiter=",")
        headers = next(csv_reader)

        country_row = next(row for row in csv_reader if row[2] == country)

        country_dict: Dict = {
            item[0]: item[1] for item in list(zip(headers, country_row))
        }

        items = {item[0]: int(country_dict[item[1]]) for item in MAPPER.items()}

        generate_bar_chart(labels=list(items.keys()), values=list(items.values()))


def generate_world_population_chart(csv_path: str) -> None:
    with open(csv_path, mode="r") as csv_reader:
        csv_reader = csv.reader(csv_reader, delimiter=",")
        headers = next(csv_reader)

        countries_dict_list = [
            {item[0]: item[1] for item in list(zip(headers, row))} for row in csv_reader
        ]

        population_dict = {
            country_dict[COUNTRY_INDEX]: float(country_dict[POPULATION_INDEX])
            for country_dict in countries_dict_list
        }
        print(population_dict)

        generate_pie_chart(
            labels=list(population_dict.keys()), values=list(population_dict.values())
        )


def generate_bar_chart(labels: List[str], values: List[Union[int, float]]) -> None:
    _, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()


def generate_pie_chart(labels: List[str], values: List[Union[int, float]]) -> None:
    _fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.show()


if __name__ == "__main__":
    path = "src/csv/data.csv"
    # generate_bar_chart_by_country(country="Bolivia", csv_path=path)
    generate_world_population_chart(csv_path=path)

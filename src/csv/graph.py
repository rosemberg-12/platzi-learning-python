from typing import List

from matplotlib import pyplot as plt


def generate_bar_chart(labels: List[str], values: List[str]) -> None:
    _, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()


def genetare_pie_chart(labels: List[str], values: List[str]) -> None:
    _fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.show()


if __name__ == "__main__":
    labels = ["Prots", "Samir", "Ross"]
    values = ["20", "50", "100"]
    genetare_pie_chart(labels=labels, values=values)

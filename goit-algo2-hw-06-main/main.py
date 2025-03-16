import requests
import matplotlib.pyplot as plt
from collections import defaultdict
import re


def map_function(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return [(word, 1) for word in words]


def shuffle_function(mapped_values):
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)
    return shuffled.items()


def reduce_function(shuffled_values):
    reduced = {}
    for key, values in shuffled_values:
        reduced[key] = sum(values)
    return reduced


def map_reduce(text):
    mapped_values = map_function(text)
    shuffled_values = shuffle_function(mapped_values)
    reduced_values = reduce_function(shuffled_values)
    return reduced_values


def visualize_top_words(word_counts):
    top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[
        :10]
    words, frequencies = zip(*top_words)

    plt.figure(figsize=(10, 5))
    plt.barh(words, frequencies, color='skyblue')
    plt.xlabel("Frequency")
    plt.ylabel("Words")
    plt.title("Top 10 Most Frequent Words")
    plt.gca().invert_yaxis()
    plt.show()


if __name__ == '__main__':

    url = "https://www.gutenberg.org/files/1342/1342-0.txt"
    response = requests.get(url)

    if response.status_code == 200:
        text = response.text
        word_counts = map_reduce(text)
        visualize_top_words(word_counts)
    else:
        print("Помилка при завантаженні тексту")

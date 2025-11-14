import requests
import matplotlib.pyplot as plt
from collections import defaultdict
import re
from concurrent.futures import ThreadPoolExecutor


def map_chunk(chunk):
    return [(word, 1) for word in chunk]


def parallel_map(text, num_threads=4):
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return []

    chunk_size = max(1, len(words) // num_threads)
    chunks = [words[i:i + chunk_size] for i in range(0, len(words), chunk_size)]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = executor.map(map_chunk, chunks)

    mapped_values = []
    for result in results:
        mapped_values.extend(result)

    return mapped_values


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
    mapped_values = parallel_map(text)
    shuffled_values = shuffle_function(mapped_values)
    reduced_values = reduce_function(shuffled_values)
    return reduced_values


def visualize_top_words(word_counts, top_n=10):
    top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    words, frequencies = zip(*top_words)

    plt.figure(figsize=(10, 5))
    plt.barh(words, frequencies, color='skyblue')
    plt.xlabel("Frequency")
    plt.ylabel("Words")
    plt.title(f"Top {top_n} Most Frequent Words")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    url = "https://www.gutenberg.org/files/1342/1342-0.txt"  # Pride and Prejudice

    try:
        response = requests.get(url)
        response.raise_for_status()
        text = response.text

        word_counts = map_reduce(text)
        visualize_top_words(word_counts)

    except requests.RequestException as e:
        print(f"Помилка при завантаженні тексту: {e}")

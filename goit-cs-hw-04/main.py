from threaded_search import threaded_search
from multiprocess_search import multiprocessing_search

if __name__ == "__main__":
    folder = "data"
    keywords = ["Python", "thread", "process"]

    print("\n🔍 Пошук за допомогою потоків (threading):")
    result_threads = threaded_search(folder, keywords)
    print(result_threads)

    print("\n🔍 Пошук за допомогою процесів (multiprocessing):")
    result_processes = multiprocessing_search(folder, keywords)
    print(result_processes)

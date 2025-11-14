import os
import threading
import time

def search_in_files_threaded(file_paths, keywords, result_dict, lock):
    for path in file_paths:
        try:
            with open(path, "r", encoding="utf-8") as file:
                text = file.read()
                for word in keywords:
                    if word in text:
                        with lock:
                            result_dict.setdefault(word, []).append(path)
        except Exception as e:
            print(f"Помилка при читанні {path}: {e}")

def threaded_search(folder_path, keywords):
    start = time.time()
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".txt")]

    num_threads = min(4, len(files))
    chunk_size = len(files) // num_threads
    threads = []
    result_dict = {}
    lock = threading.Lock()

    for i in range(num_threads):
        start_idx = i * chunk_size
        end_idx = None if i + 1 == num_threads else (i + 1) * chunk_size
        thread_files = files[start_idx:end_idx]
        thread = threading.Thread(target=search_in_files_threaded, args=(thread_files, keywords, result_dict, lock))
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()

    print(f"[THREADING] Час виконання: {time.time() - start:.2f} с")
    return result_dict

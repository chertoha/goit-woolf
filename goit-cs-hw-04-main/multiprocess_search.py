import os
import time
from multiprocessing import Process, Queue

def search_in_files_process(file_paths, keywords, queue):
    result = {}
    for path in file_paths:
        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
                for kw in keywords:
                    if kw in text:
                        result.setdefault(kw, []).append(path)
        except Exception as e:
            print(f"Помилка при читанні {path}: {e}")
    queue.put(result)

def multiprocessing_search(folder_path, keywords):
    start = time.time()
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".txt")]

    num_processes = min(4, len(files))
    chunk_size = len(files) // num_processes
    processes = []
    queue = Queue()

    for i in range(num_processes):
        start_idx = i * chunk_size
        end_idx = None if i + 1 == num_processes else (i + 1) * chunk_size
        process_files = files[start_idx:end_idx]
        p = Process(target=search_in_files_process, args=(process_files, keywords, queue))
        processes.append(p)
        p.start()

    final_result = {}
    for _ in processes:
        part = queue.get()
        for kw, paths in part.items():
            final_result.setdefault(kw, []).extend(paths)

    for p in processes:
        p.join()

    print(f"[MULTIPROCESSING] Час виконання: {time.time() - start:.2f} с")
    return final_result

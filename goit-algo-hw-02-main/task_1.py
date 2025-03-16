import queue
import random
import time

q = queue.Queue()


def generate_request():
    num = random.randint(5, 12)

    for i in range(1, num):
        request = f"Request #{i}"
        print(request)
        q.put(request)
        time.sleep(0.1)


def process_request():

    while not q.empty():
        request = q.get()
        print(f"{request} processed successfully")
        time.sleep(1)

    print("All requests have been processed")


def main():
    generate_request()
    process_request()


if __name__ == "__main__":
    main()

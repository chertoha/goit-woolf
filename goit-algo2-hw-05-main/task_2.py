import time
import hashlib
import json
import zipfile


class HyperLogLog:
    def __init__(self, b=12):
        self.b = b
        self.m = 2 ** b
        self.data = [0] * self.m

    def add(self, item):
        h = hashlib.md5(item.encode('utf8')).hexdigest()
        x = int(h, 16)
        j = x & (self.m - 1)
        self.data[j] = max(self.data[j], self._rho(x))

    def _rho(self, x):
        return (x ^ (x >> 1)).bit_length() + 1

    def count(self):
        Z = 1.0 / sum([2 ** (-reg) for reg in self.data])
        alphaMM = 0.7213 / (1 + 1.079 / self.m) * self.m * self.m
        return int(alphaMM * Z)


def extract_log_file(zip_path, log_filename):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extract(log_filename)
    return log_filename


def read_log_data(log_filename):
    ip_addresses = set()
    with open(log_filename, 'r') as f:
        for line in f:
            try:
                log_entry = json.loads(line.strip())
                ip = log_entry.get('remote_addr')
                if ip:
                    ip_addresses.add(ip)
            except json.JSONDecodeError:
                continue
    return ip_addresses


def compare_methods(log_filename):
    start_time = time.time()
    unique_ips_set = read_log_data(log_filename)
    exact_count = len(unique_ips_set)
    exact_time = time.time() - start_time

    start_time = time.time()
    hll = HyperLogLog(b=12)
    with open(log_filename, 'r') as f:
        for line in f:
            try:
                log_entry = json.loads(line.strip())
                ip = log_entry.get('remote_addr')
                if ip:
                    hll.add(ip)
            except json.JSONDecodeError:
                continue
    hll_count = hll.count()
    hll_time = time.time() - start_time

    print(f"Результати порівняння:")
    print(f"{'Метод':<20} {'Унікальні елементи':<20} {'Час виконання (сек.)':<20}")
    print(f"{'Точний підрахунок':<20} {exact_count:<20} {exact_time:<20.5f}")
    print(f"{'HyperLogLog':<20} {hll_count:<20} {hll_time:<20.5f}")

    return exact_count, hll_count, exact_time, hll_time


if __name__ == "__main__":
    zip_file_path = 'lms-stage-access.zip'
    log_filename = 'lms-stage-access.log'
    extracted_log = extract_log_file(zip_file_path, log_filename)

    exact_count, hll_count, exact_time, hll_time = compare_methods(
        extracted_log)

import mmh3
import bitarray


class BloomFilter:
    def __init__(self, size: int, num_hashes: int):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = bitarray.bitarray(size)
        self.bit_array.setall(0)

    def _hashes(self, item: str):
        for i in range(self.num_hashes):
            yield mmh3.hash(item, i) % self.size

    def add(self, item: str):
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = 1

    def contains(self, item: str) -> bool:
        return all(self.bit_array[hash_value] for hash_value in self._hashes(item))


def check_password_uniqueness(bloom: BloomFilter, passwords: list[str]) -> dict[str, str]:
    result = {}
    for password in passwords:
        if not password or not isinstance(password, str):
            result[password] = "Некоректний пароль"
        elif bloom.contains(password):
            result[password] = "вже використаний"
        else:
            result[password] = "унікальний"
            bloom.add(password)
    return result


if __name__ == "__main__":
    bloom = BloomFilter(size=1000, num_hashes=3)

    existing_passwords = ["password123", "admin123", "qwerty123"]
    for password in existing_passwords:
        bloom.add(password)

    new_passwords_to_check = ["password123",
                              "newpassword", "admin123", "guest"]
    results = check_password_uniqueness(bloom, new_passwords_to_check)

    for password, status in results.items():
        print(f"Пароль '{password}' — {status}.")

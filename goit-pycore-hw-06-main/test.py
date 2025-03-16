

arr = ["asd", "ant", "vvv"]

print(arr)

print(arr.index("ant"))

arr[arr.index("ant")] = "bbb"

print(arr)

print(next((res for res in [111, 222, 333] if res == 444), None))

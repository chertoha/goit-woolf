
import random

MIN=1
MAX=1000


def get_numbers_ticket(min:int, max:int, quantity:int):
    
    if not isinstance(min, int) or not isinstance(max,int) or not isinstance(quantity,int):
        raise TypeError("wrong argument type")
    
    if min < MIN:
        raise TypeError(f"min has to be not less than {MIN}")

    if max > MAX:
        raise TypeError(f"max has to be not more than {MAX}")
    
    if quantity >= max - min:
        raise TypeError(f"quantity has to be not more than diff of {max} and {min}, = {max-min}")


    res = set()

    while len(res) < quantity:
        rand = random.randint(min,max)
        res.add(rand)


    return sorted(res)

print(get_numbers_ticket(1,100,7))


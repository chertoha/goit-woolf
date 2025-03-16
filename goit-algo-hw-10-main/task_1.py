from pulp import PULP_CBC_CMD, LpMaximize, LpProblem, LpVariable

model = LpProblem(name="optimization-production", sense=LpMaximize)

lemonade = LpVariable(name="lemonade", lowBound=0,
                      cat='Continuous')
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat='Continuous')

model += lemonade + fruit_juice, "Total Production"

model += (2 * lemonade + 1 * fruit_juice <= 100), "Water Constraint"
model += (1 * lemonade <= 50), "Sugar Constraint"
model += (1 * lemonade <= 30), "Lemon Juice Constraint"
model += (2 * fruit_juice <= 40), "Fruit Puree Constraint"

status = model.solve(PULP_CBC_CMD(msg=False))

print(f"Optimal amount of Lemonade: {lemonade.value()} units")
print(f"Optimal amount of Fruit Juice: {fruit_juice.value()} units")

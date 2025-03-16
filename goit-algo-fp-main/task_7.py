import random
import matplotlib.pyplot as plt


def monte_carlo_dice_simulation(num_rolls=100000):
    results = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        results[roll_sum] += 1

    probabilities = {key: (value / num_rolls) *
                     100 for key, value in results.items()}
    return probabilities


def plot_probabilities(monte_carlo_probs):
    theoretical_probs = {2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
                         7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78}

    sums = list(monte_carlo_probs.keys())
    mc_values = list(monte_carlo_probs.values())
    theoretical_values = [theoretical_probs[s] for s in sums]

    plt.figure(figsize=(10, 6))
    plt.bar(sums, mc_values, color='blue', alpha=0.6, label='Монте-Карло')
    plt.plot(sums, theoretical_values, marker='o',
             color='red', label='Теоретичні значення')

    plt.xlabel("Сума на кубиках")
    plt.ylabel("Ймовірність (%)")
    plt.title("Ймовірності сум при киданні двох кубиків")
    plt.xticks(sums)
    plt.legend()
    plt.grid()
    plt.show()


mc_probs = monte_carlo_dice_simulation(100000)
print("Чим вища кількість експериментів, тим більше графік ймовірностей наближається до теоретичних даних.")
print("Якщо зменшити кількість експериментів відповідність теоретичним даним зменшується")
plot_probabilities(mc_probs)

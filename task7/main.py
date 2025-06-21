import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        sums_count[roll_sum] += 1
        
    return sums_count

def calculate_probabilities(sums_count, num_rolls):
    probabilities = {s: (count / num_rolls) * 100 for s, count in sums_count.items()}
    return probabilities

def print_results_table(monte_carlo_probs, analytical_probs):
    print("-" * 50)
    print(f"{'Сума':<10} | {'Імовірність (Монте-Карло, %)'} | {'Імовірність (Аналітична, %)'}")
    print("-" * 50)
    
    for s in sorted(monte_carlo_probs.keys()):
        mc_prob_str = f"{monte_carlo_probs[s]:.2f}%"
        an_prob_str = f"{analytical_probs[s]:.2f}%"
        print(f"{s:<10} | {mc_prob_str:<30} | {an_prob_str:<28}")
    print("-" * 50)
    
def plot_results(monte_carlo_probs, analytical_probs):
    sums = sorted(monte_carlo_probs.keys())
    mc_values = [monte_carlo_probs[s] for s in sums]
    analytical_values = [analytical_probs[s] for s in sums]

    x = range(len(sums))
    
    plt.figure(figsize=(12, 6))
    plt.bar([i - 0.2 for i in x], mc_values, width=0.4, label='Монте-Карло', color='skyblue')
    plt.bar([i + 0.2 for i in x], analytical_values, width=0.4, label='Аналітична', color='orange')
    
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Імовірність (%)')
    plt.title('Порівняння імовірностей сум при киданні двох кубиків')
    plt.xticks(x, sums)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

if __name__ == '__main__':
    analytical_probabilities = {
        2: (1/36) * 100,
        3: (2/36) * 100,
        4: (3/36) * 100,
        5: (4/36) * 100,
        6: (5/36) * 100,
        7: (6/36) * 100,
        8: (5/36) * 100,
        9: (4/36) * 100,
        10: (3/36) * 100,
        11: (2/36) * 100,
        12: (1/36) * 100,
    }
    
    num_rolls = 1000000
    
    print(f"Симуляція {num_rolls} кидків двох кубиків...")
    sum_counts = simulate_dice_rolls(num_rolls)
    
    monte_carlo_probabilities = calculate_probabilities(sum_counts, num_rolls)
    
    print_results_table(monte_carlo_probabilities, analytical_probabilities)
    
    plot_results(monte_carlo_probabilities, analytical_probabilities)

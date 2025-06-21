def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    chosen_items = []
    total_calories = 0
    remaining_budget = budget
    
    for item_name, item_data in sorted_items:
        if item_data['cost'] <= remaining_budget:
            chosen_items.append(item_name)
            total_calories += item_data['calories']
            remaining_budget -= item_data['cost']
            
    return chosen_items, total_calories, remaining_budget


def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        item_name, item_data = item_list[i-1]
        cost = item_data['cost']
        calories = item_data['calories']
        
        for w in range(1, budget + 1):
            if cost <= w:
                dp[i][w] = max(calories + dp[i-1][w - cost], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
                
    chosen_items = []
    total_calories = dp[n][budget]
    remaining_budget = budget
    
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            item_name, item_data = item_list[i-1]
            chosen_items.append(item_name)
            w -= item_data['cost']
            
    chosen_items.reverse()
    remaining_budget -= (budget - w)
    
    return chosen_items, total_calories, remaining_budget


if __name__ == '__main__':
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    
    budget = 100

    print("Дані про їжу:", items)
    print(f"Бюджет: {budget}\n")

    greedy_choice, greedy_calories, greedy_rem_budget = greedy_algorithm(items, budget)
    print("--- Жадібний алгоритм ---")
    print("Обрані страви:", greedy_choice)
    print("Сумарна калорійність:", greedy_calories)
    print(f"Витрачено: {budget - greedy_rem_budget}, Залишок бюджету: {greedy_rem_budget}\n")

    dp_choice, dp_calories, dp_rem_budget = dynamic_programming(items, budget)
    print("--- Динамічне програмування ---")
    print("Обрані страви:", dp_choice)
    print("Сумарна калорійність:", dp_calories)
    print(f"Витрачено: {budget - dp_rem_budget}, Залишок бюджету: {dp_rem_budget}\n")
    
    print("--- Порівняння ---")
    print(f"Жадібний алгоритм дав {greedy_calories} калорій.")
    print(f"Динамічне програмування дало {dp_calories} калорій (оптимальний результат).")

import matplotlib.pyplot as plt
import math


class ClassicTree:
    def __init__(self, figsize=(12, 8)):
        self.fig, self.ax = plt.subplots(figsize=figsize)
        self.ax.set_aspect('equal')
        self.ax.set_xlim(-3, 3)
        self.ax.set_ylim(0, 6)
        self.ax.set_title('Класичне фрактальне дерево', fontsize=16, fontweight='bold')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.grid(True, alpha=0.3)

        self.colors = ['#8B4513', '#A0522D', '#CD853F', '#D2691E', '#B8860B', 
                      '#DAA520', '#F4A460', '#DEB887', '#F5DEB3', '#FFE4B5']
    
    def draw_branch(self, x, y, length, angle, level, max_level):

        if level >= max_level:
            return
        
        x_end = x + length * math.cos(angle)
        y_end = y + length * math.sin(angle)
        
        color = self.colors[level % len(self.colors)]
        linewidth = max(1, 8 - level)
        
        self.ax.plot([x, x_end], [y, y_end], color=color, linewidth=linewidth, alpha=0.8)
        
        new_length = length * 0.7
        left_angle = angle + math.pi / 4
        right_angle = angle - math.pi / 4
        
        self.draw_branch(x_end, y_end, new_length, left_angle, level + 1, max_level)
        self.draw_branch(x_end, y_end, new_length, right_angle, level + 1, max_level)
    
    def create_tree(self, max_level=4, initial_length=1.5):
        self.ax.clear()
        self.ax.set_aspect('equal')
        self.ax.set_xlim(-3, 3)
        self.ax.set_ylim(0, 6)
        self.ax.set_title(f'Класичне фрактальне дерево (Рівень: {max_level})', 
                         fontsize=16, fontweight='bold')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.grid(True, alpha=0.3)
        
        start_x, start_y = 0, 0
        start_angle = math.pi / 2
        
        self.draw_branch(start_x, start_y, initial_length, start_angle, 0, max_level)
    
    def show(self):
        plt.tight_layout()
        plt.show()


def get_recursion_level():
    print("=== Фрактальне дерево ===")
    print("Введіть рівень рекурсії (1-10) або натисніть Enter для значення за замовчуванням (4):")
    
    user_input = input().strip()
    
    if not user_input:
        return 4
    
    try:
        level = int(user_input)
        if 1 <= level <= 10:
            return level
        else:
            print("Рівень повинен бути від 1 до 10. Використовується значення за замовчуванням: 4")
            return 4
    except ValueError:
        print("Невірний формат. Використовується значення за замовчуванням: 4")
        return 4


def main():
    max_level = get_recursion_level()
    
    print(f"Створюємо дерево з рівнем рекурсії {max_level}...")
    
    tree = ClassicTree()
    tree.create_tree(max_level=max_level)
    tree.show()


if __name__ == "__main__":
    main()

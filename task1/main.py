class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Порожній список")
    
    def reverse(self):
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return
        
        sorted_head = None
        current = self.head
        
        while current:
            next_node = current.next

            sorted_head = self._insert_sorted(sorted_head, current)
            
            current = next_node
        
        self.head = sorted_head
    
    def _insert_sorted(self, sorted_head, new_node):
        if sorted_head is None or new_node.data <= sorted_head.data:
            new_node.next = sorted_head
            return new_node
        
        current = sorted_head
        while current.next and current.next.data < new_node.data:
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        return sorted_head
    
    def merge_sort(self):
        self.head = self._merge_sort_recursive(self.head)
    
    def _merge_sort_recursive(self, head):
        if head is None or head.next is None:
            return head
        
        middle = self._get_middle(head)
        next_of_middle = middle.next
        middle.next = None
        
        left = self._merge_sort_recursive(head)
        right = self._merge_sort_recursive(next_of_middle)
        
        return self._merge_sorted_lists(left, right)
    
    def _get_middle(self, head):
        if head is None:
            return head
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def _merge_sorted_lists(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        
        result = None
        
        if left.data <= right.data:
            result = left
            result.next = self._merge_sorted_lists(left.next, right)
        else:
            result = right
            result.next = self._merge_sorted_lists(left, right.next)
        
        return result
    
    @staticmethod
    def merge_sorted_lists(list1, list2):
        merged_list = LinkedList()
        
        current1 = list1.head
        current2 = list2.head
        
        while current1 and current2:
            if current1.data <= current2.data:
                merged_list.append(current1.data)
                current1 = current1.next
            else:
                merged_list.append(current2.data)
                current2 = current2.next
        
        while current1:
            merged_list.append(current1.data)
            current1 = current1.next
        
        while current2:
            merged_list.append(current2.data)
            current2 = current2.next
        
        return merged_list


def demo_linked_list():
    print("=== Демонстрація роботи з однозв'язним списком ===\n")
    
    print("1. Створення списку:")
    linked_list = LinkedList()
    linked_list.append(64)
    linked_list.append(34)
    linked_list.append(25)
    linked_list.append(12)
    linked_list.append(22)
    linked_list.append(11)
    linked_list.append(90)
    print("Початковий список:")
    linked_list.print_list()
    
    # Реверсування списку
    print("\n2. Реверсування списку:")
    linked_list.reverse()
    print("Після реверсування:")
    linked_list.print_list()
    
    # Сортування вставками
    print("\n3. Сортування вставками:")
    linked_list.insertion_sort()
    print("Після сортування вставками:")
    linked_list.print_list()
    
    # Реверсуємо знову для демонстрації сортування злиттям
    print("\n4. Сортування злиттям:")
    linked_list.reverse()
    print("Після реверсування:")
    linked_list.print_list()
    linked_list.merge_sort()
    print("Після сортування злиттям:")
    linked_list.print_list()
    
    # Об'єднання двох відсортованих списків
    print("\n5. Об'єднання двох відсортованих списків:")
    
    # Створюємо перший відсортований список
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)
    list1.append(7)
    print("Перший відсортований список:")
    list1.print_list()
    
    # Створюємо другий відсортований список
    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)
    list2.append(8)
    print("Другий відсортований список:")
    list2.print_list()
    
    # Об'єднуємо списки
    merged = LinkedList.merge_sorted_lists(list1, list2)
    print("Об'єднаний відсортований список:")
    merged.print_list()


if __name__ == "__main__":
    demo_linked_list()

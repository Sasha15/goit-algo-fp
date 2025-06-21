import heapq
from typing import Dict, List, Tuple, Optional
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
    
    def add_edge(self, u: int, v: int, weight: float):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
        self.vertices.add(u)
        self.vertices.add(v)
    
    def get_neighbors(self, vertex: int) -> List[Tuple[int, float]]:
        return self.graph[vertex]


class MinHeap:
    
    def __init__(self):
        self.heap = []
        self.vertex_to_index = {}
    
    def is_empty(self) -> bool:
        return len(self.heap) == 0
    
    def insert(self, vertex: int, distance: float):
        if vertex in self.vertex_to_index:
            self.update_distance(vertex, distance)
        else:
            heapq.heappush(self.heap, (distance, vertex))
            self.vertex_to_index[vertex] = len(self.heap) - 1
    
    def extract_min(self) -> Tuple[int, float]:
        if self.is_empty():
            raise IndexError("Купа порожня")
        
        distance, vertex = heapq.heappop(self.heap)
        del self.vertex_to_index[vertex]
        
        self._update_indices()
        
        return vertex, distance
    
    def update_distance(self, vertex: int, new_distance: float):
        if vertex not in self.vertex_to_index:
            return
        
        for i, (dist, v) in enumerate(self.heap):
            if v == vertex:
                if new_distance < dist:
                    self.heap[i] = (new_distance, vertex)
                    heapq.heapify(self.heap)
                    self._update_indices()
                break
    
    def _update_indices(self):
        self.vertex_to_index.clear()
        for i, (_, vertex) in enumerate(self.heap):
            self.vertex_to_index[vertex] = i


def dijkstra_heap(graph: Graph, start_vertex: int) -> Tuple[Dict[int, float], Dict[int, Optional[int]]]:
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start_vertex] = 0
    
    predecessors = {vertex: None for vertex in graph.vertices}
    
    min_heap = MinHeap()
    min_heap.insert(start_vertex, 0)
    
    visited = set()
    
    while not min_heap.is_empty():
        current_vertex, current_distance = min_heap.extract_min()
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        for neighbor, weight in graph.get_neighbors(current_vertex):
            if neighbor in visited:
                continue
            
            new_distance = current_distance + weight
            
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_vertex
                min_heap.insert(neighbor, new_distance)
    
    return distances, predecessors


def get_shortest_path(predecessors: Dict[int, Optional[int]], start_vertex: int, end_vertex: int) -> List[int]:
    if end_vertex not in predecessors:
        return []
    
    path = []
    current_vertex = end_vertex
    
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = predecessors[current_vertex]
    
    path.reverse()
    
    if path and path[0] == start_vertex:
        return path
    else:
        return []


def print_results(distances: Dict[int, float], predecessors: Dict[int, Optional[int]], start_vertex: int):
    print(f"\nРезультати алгоритму Дейкстри (початкова вершина: {start_vertex}):")
    print("-" * 60)
    
    for vertex in sorted(distances.keys()):
        distance = distances[vertex]
        if distance == float('infinity'):
            print(f"Вершина {vertex}: недосяжна")
        else:
            path = get_shortest_path(predecessors, start_vertex, vertex)
            path_str = " -> ".join(map(str, path))
            print(f"Вершина {vertex}: відстань = {distance}, шлях: {path_str}")


def main():
    print("Алгоритм Дейкстри з використанням бінарної купи")
    print("=" * 50)
    
    graph = Graph()
    
    edges = [
        (0, 1, 4),
        (0, 2, 2),
        (1, 2, 1),
        (1, 3, 5),
        (2, 3, 8),
        (2, 4, 10),
        (3, 4, 2),
        (3, 5, 6),
        (4, 5, 3),
    ]
    
    for u, v, weight in edges:
        graph.add_edge(u, v, weight)
    
    print("Створений граф:")
    for vertex in sorted(graph.vertices):
        neighbors = graph.get_neighbors(vertex)
        neighbor_str = ", ".join([f"{v}({w})" for v, w in neighbors])
        print(f"Вершина {vertex}: сусіди [{neighbor_str}]")
    
    start_vertex = 0
    distances, predecessors = dijkstra_heap(graph, start_vertex)
    
    print_results(distances, predecessors, start_vertex)
    
    end_vertex = 5
    shortest_path = get_shortest_path(predecessors, start_vertex, end_vertex)
    print(f"\nНайкоротший шлях від {start_vertex} до {end_vertex}:")
    if shortest_path:
        path_str = " -> ".join(map(str, shortest_path))
        print(f"Шлях: {path_str}")
        print(f"Загальна відстань: {distances[end_vertex]}")
    else:
        print("Шлях не знайдено")


if __name__ == "__main__":
    main() 
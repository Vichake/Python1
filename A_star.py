import heapq

def a_star_search(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start))  # (f = g + h, g, node)

    visited = set()

    while open_list:
        f, g, current = heapq.heappop(open_list)

        if current == goal:
            print(f"Goal '{goal}' reached with total cost: {g}")
            return

        if current in visited:
            continue

        visited.add(current)
        print(f"Visiting Node: {current}, Cost so far: {g}, Heuristic: {heuristic[current]}")

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g + cost
                f_value = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_value, new_g, neighbor))

    print("Goal not reachable.")

# Graph definition
graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('D',12)],
    'B': [('C', 2)],
    'C':[('D',3)],
    'D': []
}

# Heuristic values
heuristic = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 1,
    'D': 0
}

# Run the A* search
a_star_search(graph, heuristic, 'S', 'D')

from collections import deque
import pygame

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]


def move_pacman(pacman_pos, direction):
    x, y = pacman_pos
    if direction[pygame.K_a]:
        x -= 1
    elif direction[pygame.K_d]:
        x += 1
    elif direction[pygame.K_w]:
        y -= 1
    elif direction[pygame.K_s]:
        y += 1
    return x, y


def bfs(maze, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()
        if current == goal:
            break
        neighbors = get_neighboars(current, maze)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
        path = []
        while goal:
            path.append(goal)
            goal = parent[goal]
        return path[:: -1]


def get_neighboars(pos, maze):
    x, y = pos
    neighboars = []
    if x > 0 and maze[x-1][y] == 0:
        neighboars.append((x-1, y))
    if x < len(maze)-1 and maze[x+1][y] == 0:
        neighboars.append((x+1, y))
    if y > 0 and maze[x][y-1] == 0:
        neighboars.append((x, y-1))
    if y < len(maze[0])-1 and maze[x][y+1] == 0:
        neighboars.append((x, y+1))
    return neighboars


pygame.init()


def user_input():
    keys = pygame.key.get_pressed()
    return keys


screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pacman_pos = move_pacman(pacman_pos, user_input())
    ghost_pos = bfs(maze, ghost_pos, pacman_pos)[1]
    if pacman_pos == ghost_pos:
        print("Game over!")
        running = False

    

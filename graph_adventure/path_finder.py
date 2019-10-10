# Go through all directions for each node
# Handle the fact that the player needs to move BACK to the intersection
# Keep a list of intersections, remove them if I hit it again (i.e. a loop)
# I need a way to build "paths" and return the shortest overall. Shortest for each break intersection? How do I handle this?

# DFS with a Queue for each intersection?

# Intersections.
# Go back to the last one when I reach a dead end, go a way I HAVEN'T gone. If I go all ways go back to the intersection before it?

def path_finder(world):
    print(len(world)) # How many rooms I have to touch
    shortest_path = []



    return shortest_path
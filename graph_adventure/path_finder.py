# Go through all directions for each node
# I need a way to build "paths" and return the shortest overall. Shortest for each break intersection? How do I handle this?

# Find all dead_ends
# if len(dead_ends) > 0:
#   bfs to closest dead_end, remove it from list
# else:
#   while current_room has unexplored paths:
#       move weighted by distance from edge of grid (more weight closer you are to edge, should force a spiral)
#   bfs to next unexplored path

# Perhaps if I can go to each dead_end without traveling back through visited rooms. 
# See which one has the shortest path AND no visited rooms, else just shortest path. 
# Put those paths in to an array, check that array, clear that array.

def path_finder(world):
    # How many rooms I have to touch
    shortest_path = []

    # Keeping track of important stuff
    visited = set()
    main_queue = []
    intersections = []

    # Setup
    main_queue.append(world.startingRoom)
    current_room = world.startingRoom
    # while len(visited) < len(world.rooms):
    if True:
        current_room = main_queue.pop()
        visited.add(current_room.id)
        new_queue = []
        if current_room.n_to:
            new_queue.append(current_room.n_to)
        if current_room.s_to:
            new_queue.append(current_room.s_to)
        if current_room.e_to:
            new_queue.append(current_room.e_to)
        if current_room.w_to:
            new_queue.append(current_room.w_to)
        main_queue += new_queue
    print(visited)
    print(main_queue)

    return shortest_path
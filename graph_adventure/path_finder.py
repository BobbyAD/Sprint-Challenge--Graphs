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

    num_rooms = len(world.rooms)
    # Going to return this
    return_path = []
    # Keeping track of stuff
    visited = set()

    """
        Finding all dead ends so I can traverse to them
    """
    dead_ends = set()
    for r in world.rooms:
        count_connections = 0
        if world.rooms[r].n_to:
            count_connections += 1
        if world.rooms[r].s_to:
            count_connections += 1
        if world.rooms[r].e_to:
            count_connections += 1
        if world.rooms[r].w_to:
            count_connections += 1
        if count_connections == 1:
            dead_ends.add(world.rooms[r])
    
    print(f"Dead Ends: {dead_ends}")

    # test = bfs(world.startingRoom, 11)

    # for r in test:
    #     print(r.id)

    """
        Building path
    """
    current_room = world.startingRoom
    visited.add(current_room)

    while len(visited) < num_rooms:
        if len(dead_ends) > 0:
            # I need to find the CLOSEST room where I don't overlap visited, else just shortest room
            shortest = None
            shortest_no_visited = None
            dead_end_paths = []
            for i in dead_ends:
                dead_end_paths.append(bfs(current_room, i))
            for i in dead_end_paths:
                if shortest == None:
                    shortest = i
                elif shortest and len(i) < len(shortest):
                    shortest = i
                if shortest_no_visited == None and not visited & set(i):
                    shortest_no_visited = i
                elif shortest_no_visited and len(i) < len(shortest_no_visited) and not visited & set(i):
                    shortest_no_visited = i

            if shortest_no_visited:
                return_path += shortest_no_visited
                for i in shortest_no_visited:
                    visited.add(i)
                current_room = shortest_no_visited[-1]
                dead_ends.remove(current_room)
            else:
                return_path += shortest
                for i in shortest:
                    visited.add(i)
                current_room = shortest[-1]
                dead_ends.remove(current_room)
        else:
            connections = []
            if current_room.n_to:
                connections.append(current_room.n_to)
            if current_room.s_to:
                connections.append(current_room.s_to)
            if current_room.e_to:
                connections.append(current_room.e_to)
            if current_room.w_to:
                connections.append(current_room.w_to)
            for c in connections:
                pass

    print("**********\nReturn Path")
    for i in return_path:
        print(i.id)

    print("\n\n********")

    actual_return_path = []
    for i in range(0, len(return_path)-1):
        if return_path[i].n_to == return_path[i+1]:
            actual_return_path.append("n")
        if return_path[i].s_to == return_path[i+1]:
            actual_return_path.append("s")
        if return_path[i].e_to == return_path[i+1]:
            actual_return_path.append("e")
        if return_path[i].w_to == return_path[i+1]:
            actual_return_path.append("w")

    return actual_return_path

def bfs(source_room, destination_room):
    visited = set()
    
    q = [[source_room]]

    while q:
        path = q.pop()
        vertex = path[-1]

        print_str = ""
        for i in path:
            print_str += f" {i.id}"

        # print(print_str)

        if vertex.id not in visited:
            if vertex.id == destination_room.id:
                return path
            visited.add(vertex.id)

            #Getting connections
            connections = []
            if vertex.n_to and vertex.n_to.id not in visited:
                connections.append(vertex.n_to)
            if vertex.s_to and vertex.s_to.id not in visited:
                connections.append(vertex.s_to)
            if vertex.e_to and vertex.e_to.id not in visited:
                connections.append(vertex.e_to)
            if vertex.w_to and vertex.w_to.id not in visited:
                connections.append(vertex.w_to)
            for r in connections:
                new_path = list(path)
                new_path.append(r)
                q.insert(0, new_path)






    """
    OLD CODE
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
    """
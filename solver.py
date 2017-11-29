def pathfinder(maze, destination):
    prev = []
    queue = []
    path = []
 
    for x, line in enumerate(maze):
        for y, value in enumerate(line):
            if value != 'O':
                distance = float('+inf')
                previous = None
                prev.append({'c': (x, y), 'p': previous})
            else:
                distance = 0
            queue.append({'c': (x, y), 'v': distance})
 
    while queue:
        u = min(queue, key = lambda distance: distance['v'])
        queue.remove(u)
        x = u['c'][0]
        y = u['c'][1]
        z = u['v']
        next = [
            {'c': (x, y+1), 'v': z+1},
            {'c': (x+1, y), 'v': z+1},
        ]
        if x-1 >= 0:
            next.append({'c': (x-1, y), 'v': z+1})
        if y-1 >= 0:
            next.append({'c': (x, y-1), 'v': z+1})
         
        for vertex in next:
            try: 
                point = maze[vertex['c'][0]][vertex['c'][1]]
            except IndexError:
                continue
            else:
                if point != 'B':
                    v = vertex['c']
                    alt = vertex['v']
                    try:
                        qIndex = [q['c'] for q in queue].index(v)
                        pIndex = [p['c'] for p in prev].index(v)
                        previous = prev[pIndex]['c']
                        if alt < distance:
                            queue[qIndex]['v'] = alt
                            prev[pIndex]['p'] = u['c']
                    except ValueError:
                        distance = float('+inf')
                        previous = None
                         
                elif point == 'D':
                    # we have reached the destination!
                    break
 
    while prev:
        try:
            step = [p['c'] for p in prev].index(destination)
            previous = prev[step]['p']
            path.append(previous)
            destination = previous
        except ValueError:
            break
 
    if(path[0] != None):
        print "Yes, " + str(len(path))
    else:
        print "No"
 
    return
 
maze = []
print '=== Maze Pathfinder ==='
print 'Type in the maze you wish to have solved.'
print 'Press the ENTER key between lines.'
print 'Enter an empty line to solve.'
 
size = int(raw_input('What size of maze is it?: ')) # get the number of lines that will be entered
for i in range(size):
    line = raw_input('Line {}: '.format(i+1))
    maze.append(line)
 
for i, line in enumerate(maze):
    try:
        t = line.index('D')
        destination = (i, t)
        break
    except ValueError:
        # the destination is not on this line
        continue
 
pathfinder(maze, destination)

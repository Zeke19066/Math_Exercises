import numpy as np

maze_old = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

maze = np.zeros((10,10), dtype= int)

#target_coords = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
target_coords = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]



#NUMPY Method
def arraylook():
    for i, node in np.ndenumerate(maze):
        int_i = [int(n) for n in i] # Pesky tuples
        x,y = int_i[0], int_i[1]
        #print(int_i)
        if int_i in target_coords:
            print(f'executing put at: {int_i}')
            maze[x][y] = 1
            #np.put(maze, int_i, 1)# This is how we're changing individual elements in the array.
            
            print(f'Index: {i}         Node: {node}')



if __name__ == '__main__':
    arraylook()

print(f'{maze}')

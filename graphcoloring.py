def isItSafe(graphs, colors):
    for i in range(5):
        for j in range(i + 1, 5):
            if (graphs[i][j] and colors[j] == colors[i]):
                return False
    return True


def ColoringOfGraph(graphs, m, i, colors):
    if (i == 5):

        if (isItSafe(graphs, colors)):
            # Print the solution
            printSolution(colors)
            return True
        return False

    for j in range(1, m + 1):
        colors[i] = j

        if (ColoringOfGraph(graphs, m, i + 1, colors)):
            return True
        colors[i] = 0
    return False


def printSolution(colors):
    print("Solution does Exists for this graph:" " Following are colors assigned to the graph ")
    for i in range(5):
        print(colors[i], end=" ")


if __name__ == '__main__':

    # creating the graph as mentioned in the paper, with 5 vertices and we use 3 colors to color the graph
    graphs = [
        [0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 1, 0]
    ]
    m = 3
    colors = [0 for i in range(5)]

    if (not ColoringOfGraph(graphs, m, 0, colors)):
        print("Solution for the given graph does not exist")

# code by AnithaShivaramaiah


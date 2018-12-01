# Analysis of Algorithms
# Assignment 3: Shuffle Checker using Dynamic Programming
# Team members: Yevhen Voitiuk, Julia Maliauka, Michael Petracca

try:
    U = input("Enter U: ")
except SyntaxError:
    U = ""
try:
    V = input("Enter V: ")
except SyntaxError:
    V = ""
try:
    W = input("Enter W: ")
except SyntaxError:
    W = ""


def check_shuffle(U, V, W):
    if len(W) != (len(U) + len(V)):
        print(W, "is not an interleaving of", U, "and", V)
        return False

    graph = [[0 for x in range(0, len(U) + 1)] for y in range(0, len(V) + 1)]

    # The graph at (0,0) is true regardless of circumstance
    graph[0][0] = True

    # the edges along the 'outside' of the graph have one parent each, so set them specially
    for i in range(0, len(U)):
        for j in range(0, len(V)):
            # print("i: ", i, " j: ", j)
            if i == 0 and j == 0:
                graph[i][j] = True
            elif i == 0 and V[j - 1] == W[j - 1]:
                graph[i][j] = graph[i][j - 1]
            elif (U[i - 1] == W[i + j - 1]) and (V[j - 1] != W[i + j - 1]):
                graph[i][j] = graph[i - 1][j]
            elif (U[i - 1] != W[i + j - 1]) and (V[j - 1] == W[i + j - 1]):
                graph[i][j] = graph[i][j - 1]
            elif (U[i - 1] == W[i + j - 1]) and (V[j - 1] == W[i + j - 1]):
                graph[i][j] = graph[i - 1][j] or graph[i][j - 1]
            else:
                graph[i][j] = False

    if graph[len(U) - 1][len(V) - 1] == True:
        print("\n", W, "is an interleaving of ", U, " and ", V)
        return True
    else:
        print("\n", W, "is not an interleaving of ", U, " and ", V)
        return False


check_shuffle(U, V, W)

## Recursice approach to solve the damavis problem 1 (balls with values in bag)

# Define ball values
vA = 2
vB = 3
vC = 4

def ballsSolverRecursive(N, total=0):
    if total==N:
        return 1
    if total>N:
        return 0
    else:
        # substract each ball
        return ballsSolverRecursive(N, total+vA) + ballsSolverRecursive(N, total+vB) + ballsSolverRecursive(N, total+vC)


# parameters to test:
nPoints = 6 # number of points
solution = ballsSolverRecursive(nPoints)
print(solution)
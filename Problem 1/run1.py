## Recursice approach to solve the damavis problem 1 (balls with values in bag)

# Variation of the coin change problem taking ordering into account

# Define ball values
vA = 2
vB = 3
vC = 4

# RECURSIVE APPROACH
# time complexity O(3^n)-> O(k^n)
# space complexity O(1)
def ballsSolverRecursive(N, total=0):
    if total==N:
        return 1
    if total>N:
        return 0
    else:
        # substract each ball
        return ballsSolverRecursive(N, total+vA) + ballsSolverRecursive(N, total+vB) + ballsSolverRecursive(N, total+vC)

# DYNAMIC PROGRAMMING APPROACH
# Time complexity O(n)
# Space complexity O(n)
def ballsSolveDP(n):
  
    # We initialize a table that has a left padding as long as the largest ball value
    # Assuming vC is the highest of the three values:
    leng = n+1+vC
    table = [0 for i in range(leng)]
  
    # Base case (If given value is 0)
    table[vC] = 1

    for i in range(vC, leng):
        table[i] += table[i-vA]+table[i-vB]+table[i-vC]
  
    return table.pop()



# parameters to test:
n1 = 6 # number of points
n2 = 11
n3 = 14
print('Solutions for recursive:')
print('Number of was to reach %d: %d' %(n1, ballsSolverRecursive(n1)))
print('Number of was to reach %d: %d' %(n2, ballsSolverRecursive(n2)))
print('Number of was to reach %d: %d' %(n3, ballsSolverRecursive(n3)))

print('\nSolutions for Dynamic programming:')
print('Number of was to reach %d: %d' %(n1, ballsSolveDP(n1)))
print('Number of was to reach %d: %d' %(n2, ballsSolveDP(n2)))
print('Number of was to reach %d: %d' %(n3, ballsSolveDP(n3)))


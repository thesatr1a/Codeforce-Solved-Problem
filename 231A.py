# Input the number of problems
n = int(input())

# Initialize the count of problems for which friends will write a solution
count = 0

# Loop through each problem
for i in range(n):
    # Input the surety of each friend for the current problem
    surety = [int(x) for x in input().split()]

    # Check if at least two friends are sure about the solution
    if sum(surety) >= 2:
        count += 1

# Output the result
print(count)

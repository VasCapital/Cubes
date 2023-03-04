

# Define a class to represent a cube
class Cube:
    def __init__(self, side_length):
        self.side_length = side_length
        self.volume = side_length ** 3

# Define a function to process a test case
def process_test_case(test_case):
    
    # Extract the cubes from the test case
    cubes = [Cube(side_length) for side_length in test_case[1]]
    
    # Initialize the left and right pointers
    left = 0
    right = len(cubes) - 1
    
    # Initialize the previous cube's side length to infinity
    prev_side_length = float('inf')
    
    # Loop until the left and right pointers meet
    while left <= right:
        
        # Check if the left or right cube can be placed on top
        if cubes[left].side_length <= cubes[right].side_length <= prev_side_length:
            prev_side_length = cubes[right].side_length
            right -= 1
            
        elif cubes[right].side_length <= cubes[left].side_length <= prev_side_length:
            prev_side_length = cubes[left].side_length
            left += 1
            
        else:
            # If neither cube can be placed on top, return "No"
            print("No", sum(cube.volume for cube in cubes))
            return
    
    # If all cubes can be placed on top, return "Yes"
    print("Yes", sum(cube.volume for cube in cubes))

# Define a function to read test cases from input and store them in a queue
def read_test_cases():
    
    # Read the number of test cases
    t = int(input())
    
    # Create a queue to store the test cases
    test_cases_queue = []
    
    # Loop over the test cases
    for i in range(t):
        
        # Read the number of cubes
        n = int(input())
        
        # Read the side lengths of the cubes
        side_lengths = list(map(int, input().split()))
        
        # Store the test case in the queue
        test_cases_queue.append((n, side_lengths))
    
    return test_cases_queue

# Define a function to consume test cases from the queue and process them
def consume_test_cases(test_cases_queue):   
    # Loop over the test cases in the queue
    while len(test_cases_queue) > 0:    
        # Remove a test case from the queue
        test_case = test_cases_queue.pop(0) 
        # Process the test case
        process_test_case(test_case)

# Create a queue to store the test cases
test_cases_queue = read_test_cases()

print("\n")

# Process the test cases from the queue
consume_test_cases(test_cases_queue)
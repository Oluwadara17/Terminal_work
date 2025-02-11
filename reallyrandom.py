import sys
import numpy as np

def main(size, multiplier, index):
  np.random.seed(42)  
  data = np.random.randint(0, 10, size=size) * multiplier 

  if index < len(data):
    random_value = data[index]
    print(f"Your random value is {random_value}") 

if __name__ == "__main__":
  if len(sys.argv) != 4:
    sys.exit(1)
  
  try:
    size = int(sys.argv[1])
    multiplier = int(sys.argv[2])
    index = int(sys.argv[3])

     # Call the function
    main(size, multiplier, index)
  except ValueError:
        sys.exit(1)

    



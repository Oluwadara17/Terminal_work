import sys
import numpy as np           
import pandas as pd


row = int(sys.argv[1])
cols = int(sys.argv[2])

def main():
    np.random.seed(56)
    data = np.random.randint(0, 100, size = (row , cols))
    new_data = pd.DataFrame(data)
    print(new_data)
    
main()


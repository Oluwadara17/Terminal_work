import sys
import pandas as pd

def main(start, stop):
    data = pd.read_csv('president_heights.csv')

    if start < 1 or stop > len(data) or start > stop:
            print("Error: Start and stop values must be within the range of president numbers and start <= stop.")
            return
    slice = data['height(cm)'][start:stop]
    avg = slice.mean()
    print(f'The average height of presidents number {start} to {stop} is {round(avg, 2)}')


start = int(sys.argv[1])
stop = int(sys.argv[2])
main(start, stop)


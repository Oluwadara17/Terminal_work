import sys

lists = sys.argv[1:]

def main():
    data = [int(num) + index for index, num in enumerate(lists)]
    print(data)
     

main()


import sys

my_ints = sys.argv[1:]

def main():
    data = [int(x) for x in my_ints] 
    data = [x * 10 if x % 3 == 0 else x for x in data]
    print(data)
     

main()


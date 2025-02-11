import sys

set_a = sys.argv[1:]
set_b = ['apple','banana','mango','orange']

def main():
    latest = set(set_a) - set(set_b)
    print(latest)

main()


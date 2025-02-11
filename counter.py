import sys

data = sys.argv[1]

def main():
    word = {}
    for i in data:
        word[i] = word.get(i, 0) + 1
    print(word)

main()

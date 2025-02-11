import sys

data = sys.argv[1:]

def main():
    word = []
    for i in data:
        if i.lower() != 'goose':
            word.append(i)
        
    print(word)

main()

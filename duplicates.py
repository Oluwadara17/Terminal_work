import sys

data = sys.argv[1:]

def main():
    word = set()
    new = []
    for i in data:
            word.add(i)
    for v in word:
          new.append(v)
    new.sort(reverse=True)
    print(new)
        

main()

import sys

input = int(sys.argv[1])

def main():
   number = []
   for i in range(3000, 5001):
     if i % input == 0 and i % (input + 7) == 0 and i % (input * input) == 0:
        number.append(i)
   print(number)


main()
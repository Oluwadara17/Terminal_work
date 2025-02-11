import sys

input = sys.argv[1]
def main ():
  num = 0
  add = 0
  for i, v in enumerate(input):
    if v.isupper():
      num += 1
      add += i
  print(num)
  print(add)  


main()


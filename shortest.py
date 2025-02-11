import sys 

def main():
   input = sys.argv[1].split()
   count = min(input, key=len) 
   print(f"The shortest word is {count.upper()}")


main()
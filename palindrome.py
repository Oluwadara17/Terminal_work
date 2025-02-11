import sys 

input = sys.argv[1]

def main(input):
  tran = ''.join(c.lower() for c in input if c.isalnum()) 
  return tran == tran[::-1] 



if __name__ == "__main__":
    if main(input):
        print("It's a palindrome!")
    else:
        print("It's not a palindrome!")

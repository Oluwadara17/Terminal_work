import sys

def main():
	count = set()
	input = sys.argv[1].lower()
	vowel = 'aeiou'
	for i in input:
			if i in vowel:
				count.add(i)
	print(len(count))


main()


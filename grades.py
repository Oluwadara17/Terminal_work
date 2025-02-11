import sys

grades = {'Biology':80, 'Physics':88, 'Chemistry':98, 'Math':89, 'English':79,
          'Music': 67, 'History':68, 'Art':53, 'Economics':95, 'Psychology':88}
input = sys.argv[1]
def main():
    val = 0
    count = 0
    for i, j in grades.items():
        if i == input:
            continue
        else:
            val += j
            count += 1
    print(round(val / count, 2))

  
main()



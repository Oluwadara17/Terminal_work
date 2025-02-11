import sys

gpa_dict = {'A':4.0, 'A-':3.66, 'B+': 3.33, 'B':3.0, 'B-': 2.66, 'C+':2.33,
            'C':2.0, 'C-':1.66, 'D+':1.33, 'D':1.00, 'D-':.66, 'F':0.00}

inputs = sys.argv[1:]


def main():
    total_gpa = 0
    for input in inputs:
        total_gpa += gpa_dict.get(input.upper())
    total_gpa = total_gpa/len(inputs)
    print(f"My GPA is {total_gpa:.2f}")


main()


import os

def main():
    csv_file = open('test_scores.csv', 'r')

    lines = csv_file.readlines()

    csv_file.close()

    for line in lines:
        tokens = line.split(',')

        total = 0
        for token in tokens:
            total+=float(token)

        average = total / len(tokens)
        print(f'Average is {average}')

if __name__ == '__main__':
    main()
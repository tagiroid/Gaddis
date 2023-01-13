def main():
    arr = [234,4568,5,124,237,548,69,23,412,8,92]
    print(arr)
    print(f'the max number in array is {maxim(arr)}')
    print(sorted(arr)[-1])
    print(sorted(arr)[0::-1])
def maxim(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    else:
        max = maxim(arr[0:n-1])
        if arr[n-1] > max:
            return arr[n-1]
        else:
            return max
if __name__ == '__main__':
    main()
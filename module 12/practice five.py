def main():
    arr = [1,2,3,4,5,6,7,8,9,10]
    print(f'the sum is: {sum_arr(arr)}')
def sum_arr(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    else:
        return arr[n-1] + sum_arr(arr[0:n-1])
if __name__ == '__main__':
    main()
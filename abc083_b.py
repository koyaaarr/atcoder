import math

def main():
    num_n, num_a, num_b = list(map(int, input().split()))
    count_list = []
    for i in range(1, num_n + 1):
        #print("num", i)
        digit_list = list(str(i))
        digit_list_int = [int(j) for j in digit_list]
        num_sum = sum(digit_list_int)
        if num_a <= num_sum and num_sum <= num_b: count_list.append(i)
    #print(count_list)
    print(sum(count_list))

    


if __name__ == '__main__':
    main()

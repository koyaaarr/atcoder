def num_2n(i):
    count = 0
    while(i % 2 == 0):
        i = i / 2
        count += 1
    return count



def main():
    num_ans = int(input())
    ans_list = list(map(int, input().split()))
    num_2n_list =[]
    for i in ans_list:
        num_2n_list.append(num_2n(i))
    num_2n_list.sort()
    print(num_2n_list[0])


if __name__ == '__main__':
    main()

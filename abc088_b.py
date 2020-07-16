def main():
    num_ans = int(input())
    card_list = list(map(int, input().split()))
    card_list.sort()
    card_list.reverse()
    print(sum(card_list) - sum(card_list[1::2]) * 2)


if __name__ == '__main__':
    main()

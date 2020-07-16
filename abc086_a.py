def main():
    ans_list = list(map(int, input().split()))
    # print(ans_list)
    if (ans_list[0] % 2) != 0 and (ans_list[1] % 2) != 0:
        print("Odd")
    else:
        print("Even")

if __name__ == '__main__':
    main()

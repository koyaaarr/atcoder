

def main():
    hugou_list = list(input())
    hugou_list = [s.replace('+', '1') for s in hugou_list]
    hugou_list = [s.replace('-', '-1') for s in hugou_list]
    hugou_list = [int(n) for n in hugou_list]
    print(sum(hugou_list))


if __name__ == '__main__':
    main()

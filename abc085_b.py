def main():
    num_mochi = int(input())
    mochi_list = []
    for i in range(num_mochi):
        mochi_list.append(int(input()))
    print(len(set(mochi_list)))


if __name__ == '__main__':
    main()

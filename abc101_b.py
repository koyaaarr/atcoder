

def main():
    num_str = input()
    num_int = int(num_str)
    num_list = list(num_str)
    num_list = [int(n) for n in num_list]
    #print(num_str)
    #print(sum(num_list))
    if num_int % sum(num_list) == 0: print("Yes")
    else: print("No")


if __name__ == '__main__':
    main()

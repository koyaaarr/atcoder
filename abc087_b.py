def num_2n(i):
    count = 0
    while(i % 2 == 0):
        i = i / 2
        count += 1
    return count


def main():
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_x = int(input())
    count = 0
    for in_a in range(num_a + 1):
        for in_b in range(num_b + 1):
            for in_c in range(num_c + 1):
                if num_x == in_a * 500 + in_b * 100 + in_c * 50: count += 1 
    print(count)

    
    


if __name__ == '__main__':
    main()

def main():
    num_n = int(input())
    plan_lists = [[0, 0, 0]]
    for i in range(num_n):
        plan_lists.append(list(map(int, input().split())))
    for i in range(num_n):
        if sum(plan_lists[i+1][1:]) - sum(plan_lists[i][1:]) > (plan_lists[i+1][0] - plan_lists[i][0]):
            return print("No")
        if (plan_lists[i+1][0] - plan_lists[i][0]) % 2 == 0:
            if (sum(plan_lists[i+1][1:]) - sum(plan_lists[i][1:])) % 2 == 0:
                continue
            else:
                return print("No")
        else:
            if (sum(plan_lists[i+1][1:]) - sum(plan_lists[i][1:])) % 2 == 1:
                continue
            else:
                return print("No")
    print("Yes")





if __name__ == '__main__':
    main()

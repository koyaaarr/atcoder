def bigger_than_n(new_rule_lists):
    for n_rule, n_dist in new_rule_lists.items():
        n = 10**9 + 1
        if n_dist > n: return "sNo"
    return "Yes"

def main():
    num_n, num_m = list(map(int, input().split()))
    rule_lists = {}
    new_rule_lists = {}
    for i in range(num_m):
        num_a, num_b, num_c = list(map(int, input().split()))
        rule_lists[(num_a, num_b)] = num_c
    for i, (rule, dist) in enumerate(rule_lists.items()):
        if i == 0: 
            new_rule_lists.update({rule: dist})
            continue
        add_rule_lists = {}
        con_add_rule_lists = {}
        uniq = 0
        for n_rule, n_dist in new_rule_lists.items():
            if rule == n_rule and dist != n_dist:
                return print("No")
            elif rule[0] == n_rule[1] and rule[1] == n_rule[1] and dist == 0 and n_dist == 0:
                return print("No")
            elif rule != n_rule:
                con_add_rule_lists.update({rule: dist})
                if rule[0] == n_rule[1]: add_rule_lists[(n_rule[0], rule[1])] = dist + n_dist
                if rule[1] == n_rule[0]: add_rule_lists[(rule[0], n_rule[1])] = dist + n_dist
        while(len(add_rule_lists) > 0): 
            for a_rule, a_dist in add_rule_lists.items():
                uniq = 0
                for n_rule, n_dist in new_rule_lists.items():
                    if a_rule == n_rule and a_dist != n_dist:
                        return print("No")
                    elif a_rule[0] == n_rule[1] and a_rule[1] == n_rule[1] and a_dist == 0 and n_dist == 0:
                        return print("No")
                    elif a_rule == n_rule and a_dist == n_dist:
                        uniq = 1
                if uniq == 0:
                    con_add_rule_lists.update({a_rule: a_dist})
                for n_rule, n_dist in new_rule_lists.items():
                    if a_rule[0] == n_rule[1]:
                        add_rule_lists[(n_rule[0], a_rule[1])] = a_dist + n_dist
                    if a_rule[1] == n_rule[0]:
                        add_rule_lists[(a_rule[0], n_rule[1])] = a_dist + n_dist
        new_rule_lists.update(add_rule_lists)
        new_rule_lists.update(con_add_rule_lists)
        print(new_rule_lists)
    print(bigger_than_n(new_rule_lists))


if __name__ == '__main__':
    main()

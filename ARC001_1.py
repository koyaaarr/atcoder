
# coding: utf-8

# In[16]:

def main():
    num_ans = int(input())
    ans_list = list(map(int, list(input())))
    hit_list = []
    for i in [1,2,3,4] :
        hit = 0
        for j in ans_list:
            if i == j: hit += 1
        hit_list.append(hit)
    hit_list.sort()
    print(hit_list[3], hit_list[0])


# In[17]:

if __name__ == '__main__':
    main()


# In[ ]:




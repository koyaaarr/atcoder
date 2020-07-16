# 途中

def main():
    import math
    n, k = list(map(int, input().split()))
    #print(n, k)
    row = list(map(int, input().split()))
    #print(row.index(11))
    if row.index(1) == 0: 
        migigawa = 0
        hidarigawa = math.ceil((n - 1) / (k - 1))
    elif row.index(1) == n - 1:
        hidarigawa = math.ceil((n - 1) / (k - 1))
        hidarigawa = 0
    else: 
        migigawa = math.ceil(row.index(1) / (k-1))
        hidarigawa = math.ceil((n - migigawa * k) / (k-1))
    #print(row.index(1)+1 , k)
    #print(migigawa)
    
    #print(hidarigawa)
    print(migigawa + hidarigawa)

if __name__ == '__main__':
    main()

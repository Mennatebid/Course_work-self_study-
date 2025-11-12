def digit(n, k):
    """Return the digit that is k from the right of n for positive integers n and k.

    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """
    lst= []
    while n > 0:
        d = n%10
        lst.append(d)
        n = n//10
    if k > len(lst):
        return 0
    for i in lst:
        if i == lst[k]:
            return i


def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    entries = a ,b ,c
    lst = list(entries)
    mx = max(lst)
    mn= min(lst)
    lst.remove(mx)
    lst.remove(mn)
    num = lst[0]
    return num


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    result = 1
    while k >= 1:
        result *=n
        n-=1
        k-=1
    return result



def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    lst = []
    nums = 1
    while nums <= n:
        if nums % k ==0:
            print(nums)
            lst.append(n)
        else:
            pass
        nums+=1
    if len(lst) > 1:
        return len(lst)
    return 0



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    if y == 0:
        return y
    else :
        total = y%10
    return total + sum_digits(y//10)



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    lst = []
    search = []
    k = []
    x,y = 0,0
    while n > 0:
        lst.append(n%10)
        n=n//10
    for i , c in enumerate(lst):
        if c == 8:
            search.append((i,c))
    for i in search:
        k.append(i[0])
    for i in range(len(k)):
        if len(k) ==1:
            break
        elif abs(k[i-1]-k[i]) ==1:
            return True
    return False
        
            
print(double_eights(2882))


'''
s='abc'
s1='pqr'
a=''
j=0
for i in range(max(len(s),len(s1))):
    a+=s[i]+s1[i]
print(a)
'''
#######
'''
def add(s,s1,j=0,a=''):
    for i in range(max(len(s),len(s1))):
        if(j<len(s)):
            a+=s[j]
        if(j<len(s1)):
            a+=s1[j]
        j+=1
    print(a)
    

add('abc','pqr')#apbqcr
add('ab','pqrs')
add("abcd","pq")
'''


'''
s=["flower","flow","flight"]
#s=["dog","racecar","car"]
a=s[0]
b=s[-1]
l=""
for i in a:
    for j in b:
        if(i==j):
            l+=i
print(l)
'''

####
'''
d={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}

n=input()
if(len(n)>1):
    l=[]
    for i in range(len(n)):
        a=d[int(n[i])]
        l+=[a]
    l1=[]
    for i in range(len(l)-1):
        for j in l[i]:
            for k in l[i+1]:
                l1+=[j+k]

    print(l1)
elif(len(n)==1):
    print(list(d[int(n)]))
else:
    print('[]')
'''

'''
#s="sadbutsad"
#s1='sad'
s="leetcode"
s1='leetcd'
print(s.find(s1))
'''
#####permutations
'''
def permute(s, prefix="",l=[]):
    if len(s) == 0:
        print(prefix)
    else:
        for i in range(len(s)):
            permute(s[:i] + s[i+1:], prefix + s[i])
# Example usage
input_string = ['bar','foo','the']
permute(input_string)

'''
#nput: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

#Output: [6,9,12]
'''
def permute(s,s1,prefix="", result=[]):
    if len(s) == 0:
        result.append(prefix)  # Append the current permutation to the list
    else:
        for i in range(len(s)):
            # Recursive call with the current character added to the prefix
            permute(s[:i] + s[i+1:],s1, prefix + s[i], result)

    return result  # Return the list of permutations

# Example usage

input_string = ['bar','foo','the']
s1="barfoofoobarthefoobarman"
permutations = permute(input_string,s1)
for i in permutations:
    if(i in s1):
        print(s1.index(i))
'''





#[3, 3, 5, 5, 6, 7]

'''
n=[1,3,-1,-3,5,3,6,7]
k=int(input())
l=[]
for i in range(len(n)):
    a=n[i:i+k]
    if(len(a)==k):
        b=max(a)
        l+=[b]
print(l)   
    
output:
[3, 3, 5, 5, 6, 7]

'''

#if leet in s we print start and end index
'''
s='leetscode'
d=['leet','code','leetcode']
l = []
for i in d:
    if(i in s):
        a=s.index(i)
        print(a,a+len(i)-1)
                
'''           
#######
'''
n=int(input())
l=[]
for i in range(2,n):
    if(n%i==0):
        l+=[i]
print(l)
l1=[]
for j in l:
    f=1
    for k in range(2,j+1):
        if(j%k==0):
            f+=1
    if(f==2):
        l1+=[j]
            
print(l1)

output:
28
[2, 4, 7, 14]
[2, 7]
'''

'''
def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        output = []

        for i in range(len(path)):
            if path[i] == "" or path[i] == ".":
                continue
            elif path[i] == "..":
                if output:
                    output.pop(-1)
            else:
                output.append(path[i])
        
        path = "/".join(output)

        return "/"+path

'''
######[3, 4, 10]==120
'''
l = [1, 2, 3, 4, 10]
#l = [120, 1, 2, 3]
k = 3
found = False

for i in range(len(l) - k + 1):
    a = l[i:i + k]
    product = 1
    for j in a:
        product *= j
    if product == 120:
        #print(a)
        found = True

if found:
    print(a)
else:
    print("NO")

'''
#####maximum subse
'''
l = [1,5,7,2,9,4,10]
subsequences = [[]]  

la=[]
for element in l:
    
    new_subsequences = []
    for subseq in subsequences:
        new_subsequences.append(subseq + [element])  
    subsequences.extend(new_subsequences)  
for j in subsequences:
    la+=[len(j)]
a=max(la)
if(a==len(j)):
    print(j)
'''
###median
'''
def two_sorted(n,n1):
    a=sorted(n+n1)
    if(len(a)%2!=0):
        print(a[len(a)//2])
    else:
        print(a[len(a)//2-1:len(a)//2+1])
two_sorted([1,3],[2])
two_sorted([1,2],[3,4])

two_sorted([1,2,4,5],[3,4,9,6])
'''

######
'''
def outer(func):
    def inner(n,l=[]):
        a=func(n)
        for i in range(a):
            a=input()
            l.append(a)
        #print(l)
        for j in l:
            s=j.split()
            if(s[-1]=='M'):
                b='MR. '
                print(''.join([b]+s[:-2]))
            elif(s[-1]=='F'):
                b='MS. '
                print(''.join([b]+s[:-2]))
        
    return inner
@outer
def name(n):
    return n
        1
name(int(input()))

OUTPUT:
PAVAN KUMAR 20 M
KUMARI 34 F
EIURYRH 454 M
MR. PAVANKUMAR
MS. KUMARI
MR. EIURYRH

'''
#####[3,4,5,1,1]
'''
def display(n,l=[]):
    for i in range(n):
        a=int(input())
        l+=[a]
    a=sorted(l)
    max_=len(l)-1
    min_=0
    l1=[]
    for j in range((len(l)//2)+1):
        if(min_<len(l)//2):
            l1+=[a[max_]]
            l1+=[a[min_]]
            max_-=1
            min_+=1
        else:
            l1+=[a[max_]]
    print(l1)
    s=0
    l3=[]
    for k in l1:
        s+=k
        l3+=[s]
    print(l3)
    l4=0
    for h in range(len(l3)):
        if(h%2==0):
            l4+=l3[h]
        else:
            l4-=l3[h]
    print(l4)
    
display(5)


output:
[5, 1, 4, 1, 3]
[5, 6, 10, 11, 14]
12

'''

'''
s='BANANA'
a=0
b=2
for i in range(1,len(s)):
    print(s[a:a+i])
    print(s[b:b+i])
'''
####no.of zeroes and ones are equal
'''
l=[1,1,1,0,0,1,1]
s=0
l1=[]
for i in l:
    if(i==1):
        s+=1
        l1+=[s]
    else:
        s-=1
        l1+=[s]
print(l1)
l2=[]
for j in range(len(l1)):
    for k in range(j+1,len(l1)):
        if(l1[j]==l1[k]):
            l2+=[l[j+1:k+1]]
print(max(l2,key=len))


output:
[1, 1, 0, 0]
[1, 0]
[1, 0, 0, 1]
[0, 0, 1, 1]
[0, 1]
'''

###sumof given number
'''
l=[1,4,20,3,10,5,33]
for i in range(len(l)):
    for j in range(i+1,len(l)+1):
        a=sum(l[i:j])
        if(a==33):
            print(a,l[i:j])
'''
######max avg of sub array
'''
n=[1,12,-5,-6,50,3]
l=[]
k=int(input("ENTER THE NUMBR"))
for i in range(len(n)-k+1):
    a=sum(n[i:i+k])/k
    l+=[a]
print(max(l))
'''

#[2520, 1008, 720, 630, 560]
#2--> 5*7*8*9, 2*5-->7-->8*9, 2*5-->7-->8*9
'''
n=[2,5,7,8,9]
l=[]
for i in range(len(n)):
    b=n[:i]
    a=n[i+1:]
    f=1
    for j in b:
        f*=j
    f1=1
    for k in a:
        f1*=k
    l+=[f*f1]
print(l)
        
'''
'''
s=input()
ca='AEIOU'
sa='aeiou'
for i in range(len(s)):
    if(s[i] in ca):
        for j in range(i+1,len(s)):
            if(s[j] in ca):
                a=s.replace(s[i],'*').replace(s[j],s[i]).replace('*',s[j])
    elif(s[i] in sa):
        for j in range(i+1,len(s)):
            if(s[j] in sa):
                a=s.replace(s[i],'*').replace(s[j],s[i]).replace('*',s[j])
print(a)

'''
####
'''
def common(s,s1):
    if(s1 in s):
        a=len(s1)
        return s[a:]
    else:
        return '""'
print(common('abcabc','abc'))#abc
common('ababab','abab')       #ab
print(common('leet','code'))

'''

'''
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1+str2 != str2+str1:
            return ""

        divy = math.gcd(len(str1), len(str2))
        return str1[:divy]      
obj=Solution()
print(obj.gcdOfStrings('abcabc','abc'))##abc
'''

'''
s=["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
s1=[[], [1], [2], [], [3], []]
l=[]
l1=[]

for i in range(len(s)):
    if(s[i]=="MedianFinder"):
        l+=['null']
    elif(s[i]=="addNum"):
        l1+=[s1[i][0]]
        l+=['null' ]
    elif(s[i]=="findMedian"):
        sum_,leng=sum(l1),len(l1)
        l+=[(sum_/leng)]
print(l)
'''
#two binary sums
'''
# Two binary numbers as strings
binary1 = "1010"    # binary for 3
binary2 = "1011"     # binary for 1

# Convert binary strings to integers, add them, and convert back to binary
sum_binary = bin(int(binary1, 2) + int(binary2, 2))

# Output result (removing the '0b' prefix)
print("Binary Sum:", sum_binary[2:])  # Output: '100'
'''
###converting binary to number
# binary_string = "00000010100101000001111010011100"
# decimal_value = int(binary_string, 2)
# print(decimal_value)


# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 
# represents the unsigned integer 43261596, 
# so return 964176192 which its binary representation is 00111001011110000010100101000000.


# def converBinary(n):
#     a=n[::-1]
#     decimal_value=int(a,2)
#     print(decimal_value)
# converBinary('00000010100101000001111010011100')
# converBinary('11111111111111111111111111111101')

##convert integer to binary
# n = 128
# binary_rep = ""  # To store the binary representation

# while n > 0:
#     b = n % 2  # Get the remainder (either 0 or 1)
#     binary_rep = str(b) +binary_rep # Prepend the remainder to the binary string
#     n = n // 2  # Integer division by 2

# print(binary_rep)


#binary to integer

# def binary_number(n):
#     a=n[::-1]
#     print(a)
#     s=0
#     for i in range(len(a)):
#         b=int(a[i])*(2**i)
#         s+=b 
#     print(s)

# binary_number('1101')
# binary_number('11001101')



# Input: n = 11

# Output: 3

# Explanation:

# The input binary string 1011 has a total of three set bits.


# n = int(input())
# binary_rep = ""  # To store the binary representation

# while n > 0:
#     b = n % 2  # Get the remainder (either 0 or 1)
#     binary_rep = str(b) +binary_rep # Prepend the remainder to the binary string
#     n = n // 2  # Integer division by 2
# print(binary_rep.count('1'))

# def climbStairs(n):
#         if n == 0 or n == 1:
#             return 1
#         prev, curr = 1, 1
#         for i in range(2, n+1):
#             temp = curr
#             curr = prev + curr
#             prev = temp
#         return curr
# print(climbStairs(2))

# def climber(n):
#     l=[('1'*n)]
#     a=n//2
#     #print(a)
#     if(n%2==0):
#         l+=[('2'* a)]
#         return l
#     else:
#         for i in range(a+1):
#             l1=[]
#             for j in range(a+1):
#                 if(i==j):
#                     l1+=['1']
#                 else:
#                     l1+=['2']
#             b=''.join(l1)
#             l+=[b]
#     return l
# print(climber(7))
# print(climber(6))
# print(climber(30))
# print(climber(2))
# print(climber(3))


# def word_break(s,w):
#     c=0
#     for i in w:
#         if(i in s):
#             c+=1
#             s=s.replace(i,'')
#     if(c==len(w)):
#         print("TRUE")
#     else:
#         print("false")
# word_break("leetcode",["leet","code"])
# word_break("applepenapple",["apple","pen"])
# word_break("catsandog",["cats","dog","sand","and","cat"])



#maximum xor query

# def maximum_xor(n,m):
#     a=max(n)
#     l=[]
#     while(len(n)>=1):
#         s=0
#         for i in n:
#             s^=i
#         b=a-s
#         l+=[b]
#         n.pop()
#     print(l)
# maximum_xor([0,1,1,3],2)
# maximum_xor([2,3,4,7],3)

#kth samllest elements

# n=[[1,5,9],[10,11,13],[12,13,15]]
# k=int(input())  #8
# l=[]
# for i in n:
#     for j in i:
#         l+=[j]
# print(sorted(l)[k-1])

#     2 
#    3 4
#   6 5 7
#  4 1 8 3



# def triangle_pattern(n):
#     for i in range(len(n)):
#         print(' '*(len(n)-i),end='')
#         for j in range(len(n[i])):
#             print(n[i][j],end=' ')
#         print()


# triangle_pattern([[2],[3,4],[6,5,7],[4,1,8,3]])
# triangle_pattern([[-10]])


# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

# def longest_palindrom(s):
#     if(len(s)==1):
#             return s
#     elif(len(s)==2):
#          if(s==s[::-1]):
#               return s
#          else:
#               return s[0]
#     else:
#         s=list(s)
#         for i in range(len(s)):
#             for j in range(len(s)):
#                 a=s[i:len(s)-j]
#                 if(a==a[::-1] and len(a)>1):
#                     return ''.join(a)
# print(longest_palindrom("babad"))
# print(longest_palindrom("cbbd"))
# print(longest_palindrom("ac"))

# def interval_string(s,s1,s3):
#     if(not len(s1) and not len(s) and not len(s3)):
#         s2=True
#     else:
#         b,c=s1[:-1],s1[-1]
#         s2=False
#         for i in range(0,len(s),2):
#             a=s[i:i+2]
#             if(a in s3 and b in s3 and c in s3):
#                 s2=True
#     if(s2):
#         print("TRUE")
#     else:
#         print("FALSE")
    
        
# interval_string("aabcc","dbbca","aadbbcbcac")
# interval_string("aabcc","dbbca","aadbbbcbcac")
# interval_string("","","")


# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Explanation: One way to obtain s3 is:
# Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
# Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
# Since s3 can be obtained by interleaving s1 and s2, we return true.

# def interval_string(s1,s2,s3):
#     if(not len(s1) and not len(s2) and not len(s3)):
#             s4=True
#     else:
#         b,c=s2[:-1],s2[-1]
#         s4=False
#         for i in range(0,len(s1),2):
#             a=s1[i:i+2]
#             if(a in s3 and b in s3 and c in s3):
#                 s4=True
#     if(s4):
#         return "TRUE"
#     else:
#         return "FALSE"
    
        
# print(interval_string("aabcc","dbbca","aadbbcbcac"))
# print(interval_string("aabcc","dbbca","aadbbbcbcac"))
# print(interval_string("","",""))

'''
def remove_element(n,v,):
    l=[]
    l1=[]
    out=[]
    for i in n:
        if(i==v):
            l+=[i]
        else:
            l1+=[i]
    a=l1+l
    for i in a:
        if(i==v):
            out+=['-']
        else:
            out+=[i]
    print(out)

remove_element([3,2,2,3],3)
remove_element([0,1,2,2,3,0,4,2],2)
'''

'''
def unique(n,d={}):
    for i in n:
        if(i in d):
            d[i]+=1
        else:
            d[i]=1
    print(d)
    l=[]
    for i in d.items():
        if(i[1]>=1):
            l+=[i[0]]
    print(l)

#unique([1,1,2])
unique([0,0,1,1,1,2,2,3,3,4])
'''


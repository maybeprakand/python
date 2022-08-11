# # sum of first n primes
# # alphanumeric string test
# #smallest positive integer not in list 
# #make a pyramid of *


# # # finding the number is prime
# # def isprime(n):
# #     if n<2:
# #         return False
# #     if n==2:
# #         return True
# #     dc=0
# #     for i in range (1,n+1):

# #         if n%i==0:
# #             dc+=1
# #     if dc==2:
# #         return True
# #     return False
# # # print(isprime(7))

# # #sum of frist n prime numbers

# # def primesum_upto_n(n):
# #     if n<1:
# #         return 0
# #     sum =0
# #     for i in range(2,n+1):
# #         if isprime(i):
# #             sum+=i
# #     return sum
# # print(primesum_upto_n(10))
# def nprimesum(n):
#     if n<1:
#         return 0
#     sum =0
#     pc =0
#     x=2
#     while(pc<n):
#         if isprime(x):
#             sum +=x
#             pc+=1
#         x+=1
#     return sum

# print(nprimesum(10))

#smallest positive that is not in the list 
# num_list = [1,2,3,4,5,6,7,8]
# n=len(num_list)
# def smallestNotinthelist(num_list):
#     for i in range (1,n+2):
#         if i  not in num_list:
#             return i
# print(smallestNotinthelist(num_list))

#pyramid of *
# rows = int(input("Enter number of rows: "))

# lc = 0

# for i in range(1, rows+1):
#     for space in range(1, (rows-i)+1):
#         print(end="  ")
   
#     while lc!=(2*i-1):
#         print("* ", end="")
#         lc += 1
   
#     lc = 0
#     print()
    #sqaure of *
# for i in range (1,5):
#     for j in range (1,5):
#         print('*',end='')
#     print('')





#star of *
n=10
for i in range (n):
    for space in range (n-1-i):
        print(" ",end=" ")
    for j in range (2*i+1):
        print("*",end=' ')
    print('')
#print the pattern
# for i in range(5):
#     for j in range(i+1):
#         print('*',end=" ")
#     print()
    #pyramid of *
#
  
  
  
  
  
    #pyramid with space
# n=10
# h= True or False
# def Holloworpyramid(n,h=False):
   
#         for i in range(n):
#             for space in range (4-i):
#                 print(' ',end=" ")
#             for j in range(2*i+1): 
#                 if j==0 or i==4 or j==2*i:
#                     print('*', end=' ')
#                 else:
#                     if h:
#                         print(' ', end=' ')
#                     else:
#                         print('*',end=' ')
#             print('')
    
# Holloworpyramid(4)
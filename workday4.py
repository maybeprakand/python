n=10
h=True or False

def fullpyramid(n):
    for i in range (n):
        for space in range (n-1-i):
            print(" ",end=" ")
        for j in range (2*i+1):
            print("*",end=' ')
        print('')
    #now for hollow
def hollow(n):
    for i in range (n):
        for space in range (n-1-i):
            print(" ",end=" ")
        for j in range (2*i+1):
            if j==0 or i==n-1 or j==2*i:
                print("*", end=" ")
            else:
                print(" ",end=" ")
        print(" ")

# hollow(n)
def ishollow(n,h):
    if h==True:
        hollow(n)
    else:
        fullpyramid(n)
# ishollow(n,False)
#for invertion
def invert(n):
    for i in range (n):
        for space in range (i):
            print(" ",end=" ")
        for j in range (n-2*i-1):
            print("*",end=" ")
        print("")
invert(n)
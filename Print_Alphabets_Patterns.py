def printA(n):
    for i in range(n):
      for j in range(n):
        if j==0 or j==n-1 or i==0 or i==n//2:
          print("*",end=" ")
        else:
          print(" ",end=" ")
      print()

def printB(n):
    for i in range(n):
      for j in range(n):
        if (i==0 and j==n-1) or (i==n-1 and j==n-1) or (j==n-1 and i==n//2):
          print(" ",end=" ")
        elif j==0 or j==n-1 or i==n-1 or i==0 or i==n//2:
          print("*",end=" ")
        else:
          print(" ",end=" ")
      print()

def printC(n):
    for i in range(n):
      for j in range(n):
        if (i==0 and j==0) or (i==n-1 and j==0):
          print(" ",end="")
        elif j==0 or i==0 or i==n-1 :
          print("*",end=" ")
        else:
          print(" ",end=" ")
      print()

def printD(n):
  for i in range(n):
    for j in range(n):
      if (i==0 and j==n-1) or (i==n-1 and j==n-1):
        print(" ",end="")
      elif j==0 or i==0 or i==n-1 or j==n-1 :
        print("*",end=" ")
      else:
        print(" ",end=" ")
    print()

def printE(n):
  for i in range(n):
    for j in range(n):
      if j==0 or i==n-1 or i==0 or i==n//2:
        print("*",end=" ")
      else:
        print(" ",end=" ")
    print()

def printF(n):
    for i in range(n):
      for j in range(n):
        if j==0 or i==0 or i==n//2:
          print("*",end=" ")
        else:
          print(" ",end=" ")
      print()

def printG(n):
    for i in range(n):
      for j in range(n):
        if (i==0 and j==0)or (i==n-1 and j==0) or (i==n-1 and j==n-1):
          print(" ",end=" ")
        elif j==0 or i==0 or i==n-1 or (i==n//2 and j>=n//2) or (j==n-1 and i>=n//2):
          print("*",end=" ")
        else:
          print(" ",end=" ")
      print()

def printH(n):
   for i in range(n):
    for j in range(n):
      if j==0 or j==n-1 or i==n//2:
        print("*",end=" ")
      else:
        print(" ",end=" ")
    print()


def printI(n):
    for i in range(n):
      for j in range(n):
        if i==n-1 or i==0 or j==n//2:
          print("*",end=" ")
        else:
          print(" ",end=" ")
      print()


def printJ(n):
    for i in range(n):
      for j in range(n):
          if i==0 or j==n//2 or (i==n-1 and j<=n//2):
              print("*", end=" ")
          else:
              print(" ", end=" ")
      print()


def printK(n):
    for i in range(n):
      for j in range(n):
          if j == 0 or i + j == n//2 or i - j == n//2:
              print("*", end=" ")
          else:
              print(" ", end=" ")
      print()


def printL(n):
    for i in range(n):
      for j in range(n):
          if j == 0 or i == n-1:
              print("*", end=" ")
          else:
              print(" ", end=" ")
      print()


def printM(n):
    for i in range(n):
      for j in range(n):
          if j == 0 or j == n-1 or (i == j and i <= n//2) or (i + j == n-1 and i <= n//2):
              print("*", end=" ")
          else:
              print(" ", end=" ")
      print()

def printN(n):
    for i in range(n):
      for j in range(n):
          if j == 0 or j == n-1 or i==j:
              print("*", end=" ")
          else:
              print(" ", end=" ")
      print()

def printO(n):
    for i in range(n):
      for j in range(n):
          if (i==0 and j==0) or (i==0 and j==n-1) or (i==n-1 and j==0) or (i==n-1 and j==n-1):
              print(" ", end=" ")
          elif j == 0 or j == n-1 or i==0 or i==n-1:
              print("*", end=" ")
          else:
              print(" ", end=" ")
      print()


def printP(n):
    for i in range(n):
      for j in range(n):
          if (i==0 and j==n-1) or (j==n-1 and i==n//2):
              print(" ", end=" ")
          elif j == 0 or i==0 or i==n//2 or (j==n-1 and i<=n//2):
              print("*", end=" ")
          else:
              print(" ", end=" ")
      print()

def printQ(n):
   for i in range(n):
    for j in range(n):
        if (i==0 and j==0) or (i==0 and j==n-1) or (i==n-1 and j==0):
            print(" ", end=" ")
        elif j == 0 or j == n-1 or i==0 or i==n-1 or (i==j and i>=n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


def printR(n):
    for i in range(n):
      for j in range(n):
          if (i==0 and j==n-1) or (j==n-1 and i==n//2):
              print(" ", end=" ")
          elif j == 0 or i==0 or i==n//2 or (j==n-1 and i<=n//2) or (i==j and i>=n//2):
              print("*", end=" ")
          else:
              print(" ", end=" ")
      print()


def printS(n):
    for i in range(n):
      for j in range(n):
          if (i==0 and j==0) or (j==n-1 and i==n-1) or (j==0 and i==n//2) or (j==n-1 and i==n//2):
              print(" ", end=" ")
          elif (j == 0 and i<=n//2) or (j==n-1 and i>=n//2) or i==0 or i==n-1 or i==n//2:
              print("*", end=" ")
          else:
              print(" ", end=" ")
      print()


def printT(n):
    for i in range(n):
      for j in range(n):
          if i==0 or j==n//2:
              print("*", end=" ")
          else:
              print(" ", end=" ")
      print()

def printU(n):
    for i in range(n):
      for j in range(n):
          if (j==0 and i==n-1) or (j==n-1 and i==n-1):
              print(" ", end=" ")
          elif j==0 or j==n-1 or i==n-1:
              print("*", end=" ")
          else:
              print(" ", end=" ")
      print()


def printV(n):
    for i in range(n):
        for j in range(n):
            upIdx = i - n//2
            if upIdx==j or upIdx+j==n-1 or (j==0 and i<=n//2) or (j==n-1 and i<=n//2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def printW(n):
    for i in range(n):
        for j in range(n):
            if j==0 or j==n-1 or (i==j and i>=n//2) or (i+j==n-1 and i>=n//2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def printX(n):
    for i in range(n):
        for j in range(n):
            if i==j or i+j==n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def printY(n):
    for i in range(n):
        for j in range(n):
            if (i==j and i<=n//2) or (i+j==n-1 and i<=n//2) or (j==n//2 and i>=n//2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def printZ(n):
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or i+j==n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

l = input("Enter one Letter to display letter's pattern: ").upper()

if l=="A":
    printA(5)
elif l=="B":
    printB(5)
elif l=="C":
    printC(5)
elif l=="D":
    printD(5)
elif l=="E":
    printE(5)
elif l=="F":
    printF(5)
elif l=="G":
    printG(5)
elif l=="H":
    printH(5)
elif l=="I":
    printI(5)
elif l=="J":
    printJ(5)
elif l=="K":
    printK(5)
elif l=="L":
    printL(5)
elif l=="M":
    printM(5)
elif l=="N":
    printN(5)
elif l=="O":
    printO(5)
elif l=="P":
    printP(5)
elif l=="Q":
    printQ(5)
elif l=="R":
    printR(5)
elif l=="S":
    printS(5)
elif l=="T":
    printT(5)
elif l=="U":
    printU(5)
elif l=="V":
    printV(5)
elif l=="W":
    printW(5)
elif l=="X":
    printX(5)
elif l=="Y":
    printY(5)
elif l=="Z":
    printZ(5)
else:
    print("Invalid Letter")

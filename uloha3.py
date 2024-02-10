def ispalindrom(pal):
  if pal == []:
    return 0
  
  elif pal == pal[::-1]:
    return 1
  
  else:
    return 0

      

def nextPalindrome(From, radix):
  print("-------------------------")
  
  if radix > 36 or radix < 2:
    return 0
  
  a = 0
  while True:
    n = From
    palindrom = []
    while n != 0:
      palindrom.append(n%radix)
      n = n // radix

    if ispalindrom(palindrom) and a != 0:
      print(From)
      
      return 1
    
    else:
      From += 1
      a+=1


if __name__ == "__main__":
  
  while True:
    f = int(input("Number from: "))
    r = int(input("Radix: "))

    print(nextPalindrome(f, r))
  
  
  

def anagram_check(str1,str2):
   if sorted(str1) == sorted(str2):
      return True
   else:
      return False

str1=input("Enter the 1st string:")
str2=input("Enter the 2nd string:")
str3 = sorted(str1)
print(str3)

if anagram_check(str1,str2):
   print("Anagram string")
else:
   print("Not an Anagram string")
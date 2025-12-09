
s = input().lower() 
k = s.find('a') 
if k != -1:
    print(s[k:])    
else:
    print("No 'a' in the word")
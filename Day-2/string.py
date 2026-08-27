name=input("Enter your name: ")

l=len(name)
vowels="aeiouAEIOU"
vowel_count=0
for char in name:
    if char in vowels:
        vowel_count+=1
print("Number of vowels in your name:", vowel_count)
print("Length of your name:", l)

new_name=name[::-1]
if name==new_name:
    print("Your name is a palindrome.")
else:
    print("Your name is not a palindrome.")



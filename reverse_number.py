def get_number():
    while True:
          num=int(input("Enter a number:"))
          if num>=1000:
               return num
          else:
              print("Number should atleast 4 digits.Try again!!")
def reverse_number(num):
    rev=0
    digit=0
    while num>0:
         digit=num%10
         rev=(rev*10)+digit
         num//=10
    return rev
n=get_number()
r=reverse_number(n)
print("Original number:",n)
print("Reversed number:",r)

        

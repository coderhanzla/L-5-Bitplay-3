def swap(a , b):
    #   a = a^b
    #   b = a^b
    #   a = a^b

    a = (a&b)+(a|b)
    b = a+(~b)+1
    a = a+(~b)+1
    print("After swapping: a =",a,"and b =",b)



print("Swapping of two numbers without using the third variable")
a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
swap(a,b)


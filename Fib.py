def fibonacci():
    """This project is about checking a given input is in fibonacci series or not.
    User can give single or multiple inputs.If the user gives a single input,
    then the fibonacci series is printed equal to the given input,if the user gives
    multiple inputs then python will print the fibonacci series equal to the maximum
    number given in the input.
    The multiple inputs are converted into list by using split function and stored in a
    variable(i.e.:z).
    Then by using for loop and range funtion,we append the fibonacci series in some variable.(i.e.:f).
    after that using for loop,if and else conditions are checked wheather the given user
    inputs are present in that fibonacci series or not.If the given input is present
    then it prints the given input is valid or else it print the given input is invalid and the
    output's are separated by "and".
    For example:-if user inputs 2 numbers
    0 and 7
    then the output will be like,
    0 is valid and 7 is invalid.
"""
    z=input("").split("and ")
    z=list(int(i) for i in z)
    f=[0,1]
    a=1
    b=0
    s = max(z)
    for i in range(2,s+5):
        c = b
        b = a  
        a = c + b
        f.append(a)
    x = len(z)
    for j in range(x-1):
        if z[j] in f:
            print(z[j],"is Valid",end=" and ")
        else:
            print(z[j],"is Invalid",end = " and ")
    if z[-1] in f:
        print(z[-1],"is Valid")
    else:
        print(z[-1],"is Invalid")
fibonacci()

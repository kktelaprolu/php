def simple_intrest(p,t,r):
    SI = (p*t*r)/100
    return SI


principle = float(input("Enter the priciple amount:"))
Time = float(input("Enter the Time period:"))
Rate = float(input("Enter the rate of intrest:"))

SI = simple_intrest(principle,Time,Rate)
print(f"Simple Intrest of principle amount is {SI}")
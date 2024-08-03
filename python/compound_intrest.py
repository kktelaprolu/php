def compound_intrest(p,t,r):
    ci = p*(pow(1+(r/100),t))
    return ci

principle = float(input("Enter the principle amount:"))
time=float(input("Enter the time period:"))
rate=float(input("Enter the rate of intrest:"))

CI=compound_intrest(principle,time,rate)

print(f"Compound Intrest for {principle} is {CI}")
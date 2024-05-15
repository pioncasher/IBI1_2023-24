def bond(born_date):
    b=born_date+18
    if b>=1973 and b <=1986:
        print("Roger Moore")
    if b>=1987 and b <= 1994:
        print("Timothy Dalton")
    if b>=1995 and b <=2005:
        print("Pierce Brosnan")
    if b>=2006 and b <= 2021:
        print("Daniel Craig")
    if b<1973 or b> 2021:
        print("No 'Bond'")


born_date=int(input("Please input the year you born:"))

bond(born_date)  # An example of calling the function
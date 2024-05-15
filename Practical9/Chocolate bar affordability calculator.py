def calc(total_money,pri):
    num = total_money//pri
    left=total_money % pri

    return num,left

money=float(input('Please input the total money you have:'))
price=float(input('Please input the price of each chocolate bar:'))


return_values=calc(money,price)

print("The number of chocolate bars that can be bought is:",int(return_values[0]))
print("The money you left is :",return_values[1])


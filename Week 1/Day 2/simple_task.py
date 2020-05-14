# -273 degree celsius < invalid..

temp = float(input("Enter the temperature: "))
while temp<-273:
    temp = eval(input(("Impossible temperature. Please enter above -273 degree celsius:  ")))
print("The temperature of ",temp," Celsius in Farenheit is: ", 9/5*temp+32)


#break
#continue
#pass

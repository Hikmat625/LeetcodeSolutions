numbers = {'I' : 1,'V' : 5,'X' : 10,'L': 50,'C' : 100,'D' : 500,'M' : 1000}

ip = str(input())
output = 0
a = len(ip)
for i in range(a-1):
    if numbers[ip[i]] < numbers[ip[i+1]]:
        output -= numbers[ip[i]]
    else:
        output += numbers[ip[i]]

output += numbers[ip[-1]] 
 
print(output)
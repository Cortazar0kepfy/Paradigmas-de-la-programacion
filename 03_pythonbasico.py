#Cortazar Tinajero Luis Enrique
miprimeralista = []
print(miprimeralista)



mi primera lista = [1,"javier","1.34","bosco","angel","abagail", True]
print(miprimeralista)




nums = list(range(1,61))

for i in nums:
    print(i)

nums.append(61)
nums.append(62)
nums.append(62)
print(nums)
nums.remove(61)
print(nums)


i = 61
del nums[i]
print(nums)



del nums



L1 = [1,2,3]
L2 = [4,5,6]
print(L1+L2)


potencial = []
for i in range(0,10000):
    potencial.append(float(i))
print(potencial[100])

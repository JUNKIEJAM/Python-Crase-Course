names=['John','Bob','Mosh','Sarah']

print(names[0:6])
print(names[-2])

nums=[0,0,0,0,0]

print("Enter elements: ")

for i in range(5):
    int(input(nums[i]))

maxx=0

for i in nums:
    if i > maxx:
        maxx=i

print(maxx)
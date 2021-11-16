nums=[5,2,1,7,4]

nums.append(20)
print(nums);

print(nums.sort())
nums.insert(0,10)
print(nums)

nums.remove(5)
print(nums)

nums.pop()
print(nums)

print(nums.index(1))
print(50 in nums)
print(nums.count(4))
nums.clear()
print(nums)

nums2=[5,2,1,7,4,5,2,1,5,7]
nums3=[]

for i in nums2:
    if i not in nums3:
        nums3.append(i)

print(nums3)
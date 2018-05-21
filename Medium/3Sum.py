input: nums
output: result = [] which includes all the three pairs that their sum = 0 

as a+b+c = 0, then b+c = -a

1. we sort the array in ascending order: nums.sort()
2. we loop around the whole array, since there are two more nums( b&c ) in the 
   array, so the maxium index for a is len(nums) - 3
3. b=a.index() + 1
   c=len(nums) - 1
   while j < k:
     1) if b+c=-a:
           result.append([a,b,c])
           while b = b.right():
              b.index() += 1
           while c = c.left():
              c.index() -= 1
           b.index() += 1
           c.index() -= 1

     2) if b+c < -a:
           b.index() += 1
     3) if b+c > -a:
           c.index() -= 1

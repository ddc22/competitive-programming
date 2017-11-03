A=[-1,3,-4,5,1,-6,2,1]
eq = []
for idx, element in enumerate(A):
    if(idx == 0):
        continue
    if(sum(A[:idx]) == sum(A[idx+1:])):
        eq.append(idx)
print eq
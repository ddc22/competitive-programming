def array_left_rotation(a, n, k):
    rotations =  k % n
    container = [0]*n
    for i in range(n):
        container[i-rotations] = a[i]
    return container


n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
array_left_rotation(a, n, k);
answer = array_left_rotation(a, n, k);
print ' '.join(map(str, answer))


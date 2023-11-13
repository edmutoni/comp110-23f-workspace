def nested2(n):
    ''' Two nested loops from 0 to n-1 '''
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

print(nested2(3))
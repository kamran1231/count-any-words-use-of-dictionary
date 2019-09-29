

def count_words(n):
    count = {}
    for i in n:
        count[i] = n.count(i)
    return count

n = 'kamran'
print(count_words(n))
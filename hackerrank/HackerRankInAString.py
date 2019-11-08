import re

hackerrank = re.compile('h.*a.*c.*k.*e.*r.*r.*a.*n.*k')

q = int(input())

for _ in range(q):
    s = input()

    print('YES' if re.search(hackerrank, s) else 'NO')

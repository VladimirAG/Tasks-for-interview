from collections import defaultdict
ip_count = defaultdict(int)

with open('hits.txt', 'r', encoding='utf8') as file:
    for line in file:
        host, ip, page = line.strip().split()
        ip_count[ip] += 1
list_ip = list(ip_count.items())
list_ip.sort(key=lambda x: -x[1])
for i in range(5):
    print(list_ip[i][0])


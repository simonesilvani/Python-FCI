import statistics
import requests

time1 = []
time2 = []

name_site1 = "https://www.google.com"
name_site2 = "https://www.youtube.com"

number_requests = 5

time_medio1 = 0
time_medio2 = 0


for i in range(number_requests):
    r = requests.get(name_site1)
    t = r.elapsed.microseconds / 1000
    time1.append(t)
    print(t)

time_medio1 = statistics.median(time1)
print("median time : ", time_medio1, "\n")

print(name_site2)
for i in range(number_requests):
    r = requests.get(name_site2)
    t = r.elapsed.microseconds / 1000
    time2.append(t)
    print(t)

time_medio2 = statistics.median(time2)
print("median time : ", time_medio2, "\n")

if time_medio1 > time_medio2:
    print(name_site2)
else:
    print(name_site1)



import requests
import statistics
import matplotlib.pyplot as plt

time1 = []
time2 = []

name_site1 = "https://www.google.com"
name_site2 = "https://www.youtube.com"


numbers_request = 5

for i in range(numbers_request):
    r = requests.get(name_site1)
    t = r.elapsed.microseconds / 1000
    time1.append(t)
    print(t)

for i in range(numbers_request):
    r = requests.get(name_site2)
    t = r.elapsed.microseconds / 1000
    time2.append(t)
    print(t)


print (statistics.median(time1))
print (statistics.median(time2))


plt.figure(name_site1)
plt.plot(time1)
plt.ylim([0, max(time1)])
plt.xlabel("ID request")
plt.ylabel("Tempo di request")
plt.show()


plt.figure(name_site2)
plt.plot(time1)
plt.ylim([0, 1.5*max(time2)])
plt.xlabel("ID request")
plt.ylabel("Tempo di request")
plt.show()






import statistics
import requests

# LIBRERIA GRAFICA
import matplotlib.pyplot as plt


# LISTA DI OGGETTI (può avere tipi diversi int, string, ecc anche insieme)
time = []

name_site = "https://www.polimi.it"
n_request = 10

# (FOR) 10 REQUEST HTTP
for count in range(n_request):
    request = requests.get(name_site)
    t = request.elapsed.microseconds / 1000
    print(count+1,"° time of answer: ", t)
    time.append(t)


print("\n\nmin:" , min(time))
print("max: ", max(time))
print("mean: ", sum(time)/len(time))
print("median: ", statistics.median(time))

plt.figure()
plt.plot(time)
plt.ylim([0, 1.5*max(time)])
plt.xlabel('ID RICHIESTA')
plt.ylabel('[ms]')
plt.title("TEST www.polimi.it")
plt.grid()
plt.show()
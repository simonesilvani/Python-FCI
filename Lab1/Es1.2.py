import requests
import statistics


def get_time_medio(name_site):
    time.clear()
    print(name_site)
    for i in range(number_requests):
        r = requests.get(name_site)
        t = r.elapsed.microseconds / 1000
        time.append(t)
        print(i+1,"° request : ",t)
    return statistics.median(time)


def print_time_successione_medi():
    print("Time medi: ")
    for i in range(len(name_site)):
        print(name_site[i], time_medi[i])


def registro_print_tempi_medi ():
    for i in range(len(name_site)):
        time_medio_n = get_time_medio(name_site[i])
        print("time medio : ", time_medio_n, "\n")
        time_medi.append(time_medio_n)


time = []
time_medi = []
number_requests = 10
name_site = ["https://www.google.com", "https://www.youtube.com", "https://www.polimi.it", "https://www.wikipedia.org", "https://www.amazon.com", "https://www.twitter.com"]

registro_print_tempi_medi()

print_time_successione_medi()

time_medio_best = min(time_medi)
index_time_medio_best = time_medi.index(time_medio_best)
print("\n\n\ntime medio min : ",time_medio_best, "\nwebsite : ", name_site[index_time_medio_best], "\n\n")
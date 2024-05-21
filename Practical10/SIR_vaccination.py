import numpy as np
import matplotlib.pyplot as plt
import random

N = 10000 
beta = 0.3 
gamma = 0.05 
vaccination_rates = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90] 
susceptible_lists = [list(range(1, N - int(N * rate / 100) + 1)) for rate in vaccination_rates]
initial_infected = [N - int(N * rate / 100) for rate in vaccination_rates]
number_inf_lists = [[1] for _ in vaccination_rates]
infected_lists = [[initial] for initial in initial_infected]
recovered_lists = [[] for _ in vaccination_rates]
time = list(range(1, 1001))  

def simulate_infection(sus, inf, rec, num_inf):
    for _ in range(1, 1000):
        new_infections = np.random.choice(range(2), len(sus), p=[beta * len(inf) / N, 1 - beta * len(inf) / N])
        new_recoveries = np.random.choice(range(2), len(inf), p=[gamma, 1 - gamma])
        initial_inf_len = len(inf)
        
        for j in range(len(sus)):
            if new_infections[j] == 0:
                inf.append(sus[j])
                
        for k in range(initial_inf_len):
            if new_recoveries[k] == 0:
                rec.append(inf[k])
        
        sus[:] = [x for x in sus if x not in inf]
        inf[:] = [y for y in inf if y not in rec]
        inf[:] = [y for y in inf if y not in sus]
        num_inf.append(len(inf))


for sus, inf, rec, num_inf in zip(susceptible_lists, infected_lists, recovered_lists, number_inf_lists):
    simulate_infection(sus, inf, rec, num_inf)


data_dicts = [{i: j for i, j in zip(time, num_inf)} for num_inf in number_inf_lists]
t10 = [0] * 1000


data_dicts.append({i: j for i, j in zip(time, t10)})


plt.title("SIR model with different vaccination rates")
plt.xlabel("time")
plt.ylabel('number of people')
labels = ["0%", "10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]

for data_dict, label in zip(data_dicts, labels):
    x = list(data_dict.keys())
    y = list(data_dict.values())
    plt.plot(x, y, label=label)

plt.legend()
plt.show()

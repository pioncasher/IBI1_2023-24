import numpy as np
import matplotlib.pyplot as plt

population = np.zeros((100, 100))
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title("time=0")
plt.show()

N = 10000
beta = 0.3
gamma = 0.05

def update_population(population, beta, gamma):
    infectedIndex = np.where(population == 1)
    for i in range(len(infectedIndex[0])):
        x, y = infectedIndex[0][i], infectedIndex[1][i]
        for xNeighbour in range(x-1, x+2):
            for yNeighbour in range(y-1, y+2):
                if (xNeighbour, yNeighbour) != (x, y) and 0 <= xNeighbour < 100 and 0 <= yNeighbour < 100:
                    if population[xNeighbour, yNeighbour] == 0:
                        population[xNeighbour, yNeighbour] = np.random.choice(range(2), 1, p=[1-beta, beta])[0]
    for (i, j), value in np.ndenumerate(population):
        if value == 1:
            population[i, j] = np.random.choice([1, 2], 1, p=[1-gamma, gamma])[0]

for t in range(101):
    update_population(population, beta, gamma)
    if t in [10, 50, 100]:
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"time={t}")
        plt.show()

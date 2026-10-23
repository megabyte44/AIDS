import random
import numpy as np
import matplotlib.pyplot as plt 

N = 2000
n = 150

population_mean = 4.5
population_sd = 1.2

population = np.random.normal(population_mean,population_sd,N)

sample_indices = random.sample(range(N),n)

sample = []
for i in sample_indices:
    sample.append(population[i])

total = sum(sample)

sample_mean = total/n 

total_SD = 0
for value in population:
    d = value - population_mean 
    total_SD += d*d

cal_population_SD = (total_SD/N)**0.5
standard_error = population_sd/(n**0.5)
sampling_error = sample_mean - population_mean

# Display results
print("Population size:", N)
print("Sample size:", n)
print("Population mean:", population_mean, "hours")
print("Sample mean:", round(sample_mean, 4), "hours")
print("Given population standard deviation:", population_sd, "hours")
print("Calculated population standard deviation:", round(cal_population_SD, 4), "hours")
print("Standard error:", round(standard_error, 4), "hours")
print("Sampling error:", round(sampling_error, 4), "hours")

plt.figure(1)
plt.hist(population,bins=30)
plt.title("Population Study Times")
plt.xlabel("Study Time")
plt.ylabel("Frequency")

plt.figure(2)
plt.hist(sample,bins=15)
plt.title("Population Study Times")
plt.xlabel("Study Time")
plt.ylabel("Frequency")
plt.show()
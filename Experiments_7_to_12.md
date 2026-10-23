# CSE325: AI & DATA SCIENCE LABORATORY
## PART 2: EXPERIMENTS 7 TO 12 (DATA SCIENCE & STATISTICS)

---

# Experiment 7: Implement Random Sampling

```python
import random
import numpy as np
import matplotlib.pyplot as plt

# Given population parameters
N = 2000
n = 150

population_mean = 4.5
population_sd = 1.2

# Generate normally distributed study times
population = np.random.normal(population_mean, population_sd, N)

# Randomly select 150 unique students
sample_indices = random.sample(range(N), n)
sample = []

for i in sample_indices:
    sample.append(population[i])

# Calculate sample mean manually
total = 0
for value in sample:
    total = total + value

sample_mean = total / n

# Calculate population standard deviation manually
total_squared_deviation = 0
for value in population:
    difference = value - population_mean
    total_squared_deviation += difference * difference

calculated_population_sd = (total_squared_deviation / N) ** 0.5

# Calculate standard error
standard_error = population_sd / (n ** 0.5)

# Calculate sampling error
sampling_error = sample_mean - population_mean

# Display results
print("Population size:", N)
print("Sample size:", n)
print("Population mean:", population_mean, "hours")
print("Sample mean:", round(sample_mean, 4), "hours")
print("Given population standard deviation:", population_sd, "hours")
print("Calculated population standard deviation:", round(calculated_population_sd, 4), "hours")
print("Standard error:", round(standard_error, 4), "hours")
print("Sampling error:", round(sampling_error, 4), "hours")

# Visualize population
plt.hist(population, bins=30)
plt.title("Population Study Times")
plt.xlabel("Study Time")
plt.ylabel("Frequency")
plt.show()

print(" ")

# Visualize sample
plt.hist(sample, bins=15)
plt.title("Sample Study Times")
plt.xlabel("Study Time")
plt.ylabel("Frequency")
plt.show()
```

---

# Experiment 8: Demonstrating Z-Test

### 8(A) Two-Sample Z-Test
```python
from math import sqrt
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

# Given values
sample_mean1 = 170
sample_mean2 = 175

population_sd1 = 5
population_sd2 = 5

n1 = 50
n2 = 50
alpha = 0.05

# Step 1: Calculate standard error
standard_error = sqrt((population_sd1**2 / n1) + (population_sd2**2 / n2))

# Step 2: Calculate Z-statistic
z = (sample_mean1 - sample_mean2) / standard_error

# Step 3: Calculate critical value (two-tailed)
z_critical = norm.ppf(1 - alpha / 2)

# Step 4: Calculate p-value
p_value = 2 * (1 - norm.cdf(abs(z)))

# Step 5: Display results
print("Z-statistic:", round(z, 4))
print("Critical values: -", round(z_critical, 4), "and +", round(z_critical, 4))
print("P-value:", round(p_value, 4))

# Step 6: Make decision
if p_value < alpha:
    print("Decision: Reject the null hypothesis")
    print("Conclusion: The two population means are significantly different.")
else:
    print("Decision: Fail to reject the null hypothesis")
    print("Conclusion: No significant difference between the two population means.")

# Graph
x = np.linspace(-6, 6, 100)
y = norm.pdf(x)

plt.plot(x, y, label="Standard Normal Curve")
plt.fill_between(x, y, where=(x < -z_critical), color='red', alpha=0.5, label="Rejection Region")
plt.fill_between(x, y, where=(x > z_critical), color='red', alpha=0.5)
plt.axvline(-z_critical, color='green', linestyle='--', label="Critical Value")
plt.axvline(z_critical, color='green', linestyle='--')
plt.axvline(z, color='purple', linestyle='--', label="Z Statistic")
plt.legend()
plt.title("Two-Tailed Z-Test")
plt.xlabel("Z-score")
plt.ylabel("Probability")
plt.show()
```

---

### 8(B) One-Sample Z-Test
```python
from math import sqrt
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

# Given values
sample_mean = 32
population_mean = 30
population_sd = 8

n = 64
alpha = 0.05

# Step 1: Calculate standard error
standard_error = population_sd / sqrt(n)

# Step 2: Calculate Z-statistic
z = (sample_mean - population_mean) / standard_error

# Step 3: Calculate critical value
z_critical = norm.ppf(1 - alpha / 2)

# Step 4: Calculate two-tailed p-value
p_value = 2 * (1 - norm.cdf(abs(z)))

# Step 5: Display results
print("Z-statistic:", round(z, 4))
print("Critical values: -", round(z_critical, 4), "and +", round(z_critical, 4))
print("P-value:", round(p_value, 4))

# Step 6: Make decision
if p_value < alpha:
    print("Decision: Reject the null hypothesis")
    print("Conclusion: Average delivery time is significantly different.")
else:
    print("Decision: Fail to reject the null hypothesis")
    print("Conclusion: No significant difference in average delivery time.")

# Graph
x = np.linspace(-4, 4, 100)
y = norm.pdf(x)

plt.plot(x, y, label="Standard Normal Curve")
plt.fill_between(x, y, where=(x < -z_critical), color='red', label="Rejection Region")
plt.fill_between(x, y, where=(x > z_critical), color='red')
plt.axvline(-z_critical, color='green', linestyle='--', label="Critical Value")
plt.axvline(z_critical, color='green', linestyle='--')
plt.axvline(z, color='purple', linestyle='--', label="Z Statistic")
plt.legend()
plt.title("Two-Tailed Z-Test")
plt.xlabel("Z-score")
plt.ylabel("Probability")
plt.show()
```

---

# Experiment 9: Demonstrating T-Test

### 9(A) One-Sample Two-Tailed T-Test
```python
from math import sqrt
from scipy.stats import t
import numpy as np
import matplotlib.pyplot as plt

# Given values
xbar = 32
mu = 30
s = 8
n = 16
alpha = 0.05

# Step 1: Calculate t-statistic
df = n - 1
t_stat = (xbar - mu) / (s / sqrt(n))

# Step 2: Critical value
t_critical = t.ppf(1 - alpha/2, df)

# Step 3: Two-tailed p-value
p_value = 2 * (1 - t.cdf(abs(t_stat), df))

print("T-statistic:", round(t_stat, 4))
print("Critical values:", round(-t_critical, 4), "and", round(t_critical, 4))
print("P-value:", round(p_value, 4))

# Step 4: Decision
if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")

# Step 5: Graph
x = np.linspace(-4, 4, 100)
y = t.pdf(x, df)

plt.plot(x, y, label="T Distribution Curve")
plt.fill_between(x, y, where=(x < -t_critical), color="red", label="Rejection Region")
plt.fill_between(x, y, where=(x > t_critical), color="red")
plt.axvline(-t_critical, color="green", linestyle="--", label="Critical Value")
plt.axvline(t_critical, color="green", linestyle="--")
plt.axvline(t_stat, color="purple", linestyle="--", label="T Statistic")
plt.title("One-Sample Two-Tailed T-Test")
plt.xlabel("T-score")
plt.ylabel("Probability Density")
plt.legend()
plt.show()
```

---

### 9(B) Independent Two-Sample Right-Tailed T-Test
```python
from math import sqrt
from scipy.stats import t
import numpy as np
import matplotlib.pyplot as plt

# Given values
mean1 = 80
mean2 = 70
s1 = 10
s2 = 12
n1 = 25
n2 = 25
alpha = 0.05

# Step 1: Calculate t-statistic
se = sqrt(s1**2/n1 + s2**2/n2)
t_stat = (mean1 - mean2) / se

# Step 2: Welch degrees of freedom
df = (s1**2/n1 + s2**2/n2)**2 / ((s1**2/n1)**2/(n1-1) + (s2**2/n2)**2/(n2-1))

# Step 3: Right-tailed critical value and p-value
t_critical = t.ppf(1 - alpha, df)
p_value = 1 - t.cdf(t_stat, df)

print("T-statistic:", round(t_stat, 4))
print("Critical value:", round(t_critical, 4))
print("P-value:", round(p_value, 4))

# Step 4: Decision
if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")

# Step 5: Graph
x = np.linspace(-4, 4, 300)
y = t.pdf(x, df)

plt.plot(x, y, label="T Distribution Curve")
plt.fill_between(x, y, where=(x > t_critical), color="red", alpha=0.5, label="Rejection Region")
plt.axvline(t_critical, color="green", linestyle="--", label="Critical Value")
plt.axvline(t_stat, color="purple", linestyle="--", label="T Statistic")
plt.title("Independent Two-Sample Right-Tailed T-Test")
plt.xlabel("T-score")
plt.ylabel("Probability Density")
plt.legend()
plt.show()
```

---

### 9(C) Paired-Sample Left-Tailed T-Test
```python
from math import sqrt
from scipy.stats import t
import numpy as np
import matplotlib.pyplot as plt

# Paired measurements
before = [80, 75, 90, 85, 70, 88, 92, 78]
after  = [75, 73, 85, 80, 68, 82, 88, 74]
alpha = 0.05

# Step 1: Calculate paired differences
d = np.array(after) - np.array(before)
n = len(d)
mean_d = np.mean(d)
sd_d = np.std(d, ddof=1)
df = n - 1

# Step 2: Calculate t-statistic
t_stat = mean_d / (sd_d / sqrt(n))

# Step 3: Left-tailed critical value and p-value
t_critical = t.ppf(alpha, df)
p_value = t.cdf(t_stat, df)

print("T-statistic:", round(t_stat, 4))
print("Critical value:", round(t_critical, 4))
print("P-value:", round(p_value, 4))

# Step 4: Decision
if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")

# Step 5: Graph
x = np.linspace(-4, 4, 100)
y = t.pdf(x, df)

plt.plot(x, y, label="T Distribution Curve")
plt.fill_between(x, y, where=(x < t_critical), color="red", alpha=0.5, label="Rejection Region")
plt.axvline(t_critical, color="green", linestyle="--", label="Critical Value")
plt.axvline(t_stat, color="purple", linestyle="--", label="T Statistic")
plt.title("Paired Left-Tailed T-Test")
plt.xlabel("T-score")
plt.ylabel("Probability Density")
plt.legend()
plt.show()
```

---

### 9(D) Independent Two-Sample Pooled Variance T-Test
```python
from math import sqrt
from scipy.stats import t
import numpy as np
import matplotlib.pyplot as plt

# Given values
mean1 = 78
mean2 = 73
s1 = 6
s2 = 7
n1 = 25
n2 = 22
alpha = 0.05

# Step 1: Calculate pooled variance and standard deviation
df = n1 + n2 - 2
pooled_variance = ((n1-1)*s1**2 + (n2-1)*s2**2) / df
sp = sqrt(pooled_variance)

# Step 2: Calculate T-statistic
se = sp * sqrt(1/n1 + 1/n2)
t_stat = (mean1 - mean2) / se

# Step 3: Calculate critical value
t_critical = t.ppf(1 - alpha/2, df)

# Step 4: Calculate two-tailed p-value
p_value = 2 * (1 - t.cdf(abs(t_stat), df))

# Step 5: Display results
print("Pooled variance:", round(pooled_variance, 4))
print("Pooled standard deviation:", round(sp, 4))
print("T-statistic:", round(t_stat, 4))
print("Degrees of freedom:", df)
print("Critical values:", round(-t_critical, 4), "and", round(t_critical, 4))
print("P-value:", round(p_value, 4))

# Step 6: Decision
if p_value < alpha:
    print("Decision: Reject H0")
    print("Conclusion: Significant difference between the groups.")
else:
    print("Decision: Fail to reject H0")
    print("Conclusion: No significant difference between the groups.")

# Step 7: Graph
x = np.linspace(-4, 4, 300)
y = t.pdf(x, df)

plt.plot(x, y, label="T Distribution Curve")
plt.fill_between(x, y, where=(x < -t_critical), color="red", alpha=0.5, label="Rejection Region")
plt.fill_between(x, y, where=(x > t_critical), color="red", alpha=0.5)
plt.axvline(-t_critical, color="green", linestyle="--", label="Critical Value")
plt.axvline(t_critical, color="green", linestyle="--")
plt.axvline(t_stat, color="purple", linestyle="--", label="T Statistic")
plt.title("Independent Two-Sample T-Test")
plt.xlabel("T-score")
plt.ylabel("Probability Density")
plt.legend()
plt.show()
```

---

# Experiment 10: Demonstrating ANOVA

### 10(A) One-Way ANOVA
```python
from scipy import stats

# Exam scores of students taught by 3 different methods (10 students each)
method_a = [85, 86, 88, 75, 78, 94, 98, 79, 71, 80]
method_b = [91, 92, 93, 85, 87, 84, 82, 88, 95, 96]
method_c = [79, 78, 88, 94, 92, 85, 83, 85, 82, 81]

groups = [method_a, method_b, method_c]
alpha = 0.05   # significance level

def one_way_anova(groups):
    k = len(groups)                              # number of groups
    N = sum(len(g) for g in groups)              # total observations
    grand_mean = sum(sum(g) for g in groups) / N

    ssb = 0   # sum of squares between groups
    ssw = 0   # sum of squares within groups
    for g in groups:
        group_mean = sum(g) / len(g)
        ssb += len(g) * (group_mean - grand_mean) ** 2
        ssw += sum((x - group_mean) ** 2 for x in g)

    df_between = k - 1
    df_within = N - k
    msb = ssb / df_between
    msw = ssw / df_within
    F = msb / msw
    p_value = stats.f.sf(F, df_between, df_within)   # right-tailed
    return grand_mean, ssb, ssw, df_between, df_within, msb, msw, F, p_value

(grand_mean, ssb, ssw, df_b, df_w,
 msb, msw, F, p_value) = one_way_anova(groups)

print("Grand mean            :", round(grand_mean, 2))
print("SSB (between)         :", round(ssb, 2))
print("SSW (within)          :", round(ssw, 2))
print("df (between, within)  :", (df_b, df_w))
print("MSB                   :", round(msb, 4))
print("MSW                   :", round(msw, 4))
print("F statistic           :", round(F, 4))
print("P-value               :", round(p_value, 4))

if p_value < alpha:
    print("Result: Reject H0 (at least one mean differs)")
else:
    print("Result: Fail to reject H0 (no significant difference in means)")

# Cross-check with SciPy's built-in function
print("SciPy check:", stats.f_oneway(method_a, method_b, method_c))
```

---

### 10(B) Two-Way ANOVA
```python
from scipy import stats

# Plant growth (cm) for 3 fertilizers (Factor A) x 2 sunlight levels (Factor B),
# with 5 plants in every cell.
data = {
    ("Fert 1", "Low sun"):  [6, 7, 6, 8, 7],
    ("Fert 1", "High sun"): [9, 10, 8, 9, 10],
    ("Fert 2", "Low sun"):  [8, 9, 8, 10, 9],
    ("Fert 2", "High sun"): [14, 13, 15, 14, 12],
    ("Fert 3", "Low sun"):  [7, 6, 8, 7, 6],
    ("Fert 3", "High sun"): [10, 11, 9, 10, 12],
}
alpha = 0.05   # significance level

def mean(x):
    return sum(x) / len(x)

def two_way_anova(data):
    A_levels = sorted({key[0] for key in data})
    B_levels = sorted({key[1] for key in data})
    a, b = len(A_levels), len(B_levels)
    n = len(next(iter(data.values())))           # replicates per cell

    grand_mean = mean([x for v in data.values() for x in v])
    mean_A = {i: mean([x for j in B_levels for x in data[(i, j)]]) for i in A_levels}
    mean_B = {j: mean([x for i in A_levels for x in data[(i, j)]]) for j in B_levels}
    cell   = {key: mean(v) for key, v in data.items()}

    ssa  = b * n * sum((mean_A[i] - grand_mean) ** 2 for i in A_levels)
    ssb  = a * n * sum((mean_B[j] - grand_mean) ** 2 for j in B_levels)
    ssab = n * sum((cell[(i, j)] - mean_A[i] - mean_B[j] + grand_mean) ** 2
                   for i in A_levels for j in B_levels)
    sse  = sum((x - cell[key]) ** 2 for key, v in data.items() for x in v)

    df_e = a * b * (n - 1)
    mse = sse / df_e

    results = {}
    for name, ss, df in [("Factor A (fertilizer)", ssa, a - 1),
                         ("Factor B (sunlight)",   ssb, b - 1),
                         ("Interaction A x B",     ssab, (a - 1) * (b - 1))]:
        ms = ss / df
        F = ms / mse
        p_value = stats.f.sf(F, df, df_e)         # right-tailed
        results[name] = (ss, df, ms, F, p_value)
    return results, sse, df_e, mse

results, sse, df_e, mse = two_way_anova(data)

print(f"{'Source':<24}{'SS':>9}{'df':>5}{'MS':>9}{'F':>10}{'P-value':>12}")
for name, (ss, df, ms, F, p) in results.items():
    print(f"{name:<24}{ss:>9.3f}{df:>5}{ms:>9.3f}{F:>10.4f}{p:>12.6f}")
print(f"{'Error (within)':<24}{sse:>9.3f}{df_e:>5}{mse:>9.3f}")

print()
for name, (ss, df, ms, F, p) in results.items():
    verdict = "Reject H0 (significant)" if p < alpha else "Fail to reject H0 (not significant)"
    print(f"{name}: {verdict}")
```

---

### 10(C) Demonstrating F-Test (Variance Ratio Test)
```python
import numpy as np
from scipy import stats

# Two machines fill bottles. Is one machine less consistent than the other?
machine_a = [85, 88, 90, 86, 87, 89, 91, 84]
machine_b = [78, 95, 70, 99, 82, 92, 75, 97]

alpha = 0.05   # significance level

def f_test(sample1, sample2):
    var1 = np.var(sample1, ddof=1)   # sample variance (n - 1)
    var2 = np.var(sample2, ddof=1)
    F = var1 / var2
    df1 = len(sample1) - 1
    df2 = len(sample2) - 1
    # two-tailed p-value
    p_value = 2 * min(stats.f.cdf(F, df1, df2), stats.f.sf(F, df1, df2))
    return var1, var2, F, df1, df2, p_value

var1, var2, F, df1, df2, p_value = f_test(machine_a, machine_b)

print("Variance (A)       :", round(var1, 4))
print("Variance (B)       :", round(var2, 4))
print("F statistic        :", round(F, 4))
print("Degrees of freedom :", (df1, df2))
print("P-value            :", round(p_value, 4))

if p_value < alpha:
    print("Result: Reject H0 (variances differ)")
else:
    print("Result: Fail to reject H0 (variances are equal)")
```

---

# Experiment 11: Demonstrating Linear Regression

```python
import matplotlib.pyplot as plt

x = [5, 8, 10, 12, 15, 18, 20, 22]
y = [25, 30, 38, 40, 48, 54, 60, 63]
n = len(x)

x_bar = sum(x) / n
y_bar = sum(y) / n

num = sum((x[i] - x_bar) * (y[i] - y_bar) for i in range(n))
den = sum((x[i] - x_bar) ** 2 for i in range(n))
m = num / den
c = y_bar - m * x_bar

print("equation y =", round(m, 2), "x +", round(c, 2))

yp = [m * xi + c for xi in x]
sse = sum((y[i] - yp[i]) ** 2 for i in range(n))
sst = sum((y[i] - y_bar) ** 2 for i in range(n))
r2 = 1 - sse / sst
print("R^2 score:", round(r2, 4))

target = 25
pred = m * target + c
print("prediction sales:", round(pred, 2))

plt.scatter(x, y, label="actual data")
plt.plot(x, yp, color="red", label="regression line")
plt.xlabel("advertising expenditure")
plt.ylabel("sales revenue")
plt.legend()
plt.grid()
plt.show()

print(f"1. The fitted regression equation is y = {m:.2f}x + {c:.2f}, so sales revenue increases by about {m:.2f} for each additional unit of advertising expenditure.\n"
      f"2. The R^2 score is {r2:.4f}, meaning the model explains about {r2*100:.2f}% of the variation in sales revenue.\n"
      f"3. For an advertising expenditure of {target}, the predicted sales revenue is {pred:.2f}.")
```

---

# Experiment 12: Demonstrating Logistic Regression

```python
import numpy as np
import matplotlib.pyplot as plt
import math

# Step 1: Input data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
n = len(x)

# Step 2: Initialize parameters
m = 0
c = 0
lr = 0.1

# Step 3: Train the model
for _ in range(10000):
    dm = 0
    dc = 0

    for i in range(n):
        p = 1 / (1 + math.exp(-(m*x[i] + c)))
        dm += (p - y[i]) * x[i]
        dc += p - y[i]

    m -= lr * dm / n
    c -= lr * dc / n

# Step 4: Predict classes
yp = []
for xi in x:
    p = 1 / (1 + math.exp(-(m*xi + c)))
    yp.append(1 if p >= 0.5 else 0)

# Step 5: Calculate accuracy
correct = sum(yp[i] == y[i] for i in range(n))
print("Accuracy:", correct/n * 100, "%")

# Step 6: Predict for new input
target = 5.5
new_p = 1 / (1 + math.exp(-(m*target + c)))
print("Pass probability:", round(new_p*100, 2), "%")
print("Prediction:", "Pass" if new_p >= 0.5 else "Fail")

# Step 7: Plot graph
p = [1/(1 + math.exp(-(m*xi + c))) for xi in x]

plt.scatter(x, y, label="Actual data")
plt.plot(x, p, color="red", label="Logistic curve")
plt.axhline(0.5, linestyle="--", color="green", label="Threshold = 0.5")

# Show the new point
plt.scatter(target, new_p, color="purple", s=100, label="New point (5.5)")

plt.xlabel("Study hours")
plt.ylabel("Pass probability")
plt.legend()
plt.grid()
plt.show()
```

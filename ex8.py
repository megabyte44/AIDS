import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from scipy.stats import norm


def TwoSampleTest():
    population_sd2 = population_sd1= 5
    sample_mean1 = 170
    sample_mean2 = 175
    
    n1 = n2 = 50
    alpha = 0.05

    standard_error= sqrt(population_sd1**2/n1 + population_sd2**2/n2)

    z = (sample_mean1 - sample_mean2)/standard_error

    z_critical = norm.ppf(1-alpha/2)

    p_value = 2*(1-norm.cdf(abs(z)))

    print("Z-statistic:", round(z, 4))
    print("Critical values: -", round(z_critical, 4), "and +", round(z_critical, 4))
    print("P-value:", round(p_value, 4))

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

TwoSampleTest()

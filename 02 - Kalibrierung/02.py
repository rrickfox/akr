import math
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches


s1 = [3465, 3465, 3465, 3465, 3465, 3419]
s2 = [0, 827, 1604, 2409, 3215, 4000]
s3 = [4000, 3440, 2698, 1881, 1000, 0][::-1]

s1_avg = list(map(lambda x: x[0] + (x[1]-x[0])/2, zip(s2, s3)))

power_start = [0.32, 0.32, 0.30, 0.29, 0.30, 1.17]
power_end = [0.92, 1.42, 1.69, 1.57, 1.17]
wb1_impulse = [3769, 5388, 6335, 5725, 4313]
wb2_impulse = [4004, 5725, 6723, 5882, 4284]
lb_watt = [0.45, 0.67, 0.82, 0.74, 0.55]
wb1_t2 = [198.87, 100.0, 71.78, 76.84, 113.59]
wb2_t2 = [198.8, 101.0, 72.17, 75.57, 112.34]
lb_t2 = [193.03, 97.84, 70.81, 73.66, 107.5]

average_t2 = [(wb1_t2[i] + wb2_t2[i] + lb_t2[i]) / 3 for i in range(5)]
average_ts = [t2 / math.log(2) for t2 in average_t2]

lambdas = [0.0124, 0.0305, 0.111, 0.301, 1.14, 3.01]
alphas = [0.033, 0.219, 0.196, 0.395, 0.115, 0.042]

l_star_per_beta = 0.0051
beta = 0.00641
rho_differential = [l_star_per_beta / ts + sum([alphas[i] / (1 + lambdas[i] * ts) for i in range(6)]) for ts in average_ts]
rho_integral_s2 = [sum(rho_differential[:i]) for i in range(6)]
rho_integral_s3 = [sum(rho_differential[i:]) for i in range(6)[::-1]]
rho_integral_s1 = list(map(lambda x: x[0] + (x[1]-x[0])/2, zip(rho_integral_s2, rho_integral_s3)))

z_s2 = [0] + [s2[i] - (s2[i] - s2[i - 1]) / 2 for i in range(1, 6)] + [4000]
drho_per_dz_s2 = [0] + [rho_differential[i - 1] / (s2[i] - s2[i - 1]) * 1000 for i in range(1, 6)] + [0]

z_s3 = [0 + s1[-1] - s1[-2]] + [s3[i] - (s3[i] - s3[i - 1]) / 2 for i in range(1, 6)] + [4000]
drho_per_dz_s3 = [0] + [rho_differential[i - 1] / (s3[i] - s3[i - 1]) * 1000 for i in range(1, 6)] + [0]

z_s1 = list(map(lambda x: x[0] + (x[1]-x[0])/2, zip(z_s2, z_s3)))
drho_per_dz_s1 = list(map(lambda x: x[0] + (x[1]-x[0])/2, zip(drho_per_dz_s2, drho_per_dz_s3)))

rho_integral_max = (max(rho_integral_s1), max(rho_integral_s2), max(rho_integral_s3))
rho_integral_max_sum = sum(rho_integral_max)
excess_reactivity_s2 = [rho_integral_max[1] - x for x in rho_integral_s3]
excess_reactivity_s3 = [rho_integral_max[2] - x for x in rho_integral_s3[::-1]]
excess_reactivity_s1 = [rho_integral_max[0] - (rho_integral_s1[4] + (s1[i] - s1_avg[4]) / (s1_avg[5] - s1_avg[4]) * (rho_integral_s1[5] - rho_integral_s1[4])) for i in range(6)]
excess_reactivity = [excess_reactivity_s1[i] + excess_reactivity_s2[i] + excess_reactivity_s3[i] for i in range(6)]
excess_reactivity_avg = sum(excess_reactivity) / len(excess_reactivity)

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)
print("s1_avg:", s1_avg)
print("power_start:", power_start)
print("power_end:", power_end)
print("wb1_impulse:", wb1_impulse)
print("wb2_impulse:", wb2_impulse)
print("lb_watt:", lb_watt)
print("wb1_t2:", wb1_t2)
print("wb2_t2:", wb2_t2)
print("lb_t2:", lb_t2)
print("average_t2:", average_t2)
print("average_ts:", average_ts)
print("lambdas:", lambdas)
print("alphas:", alphas)
print("rho_differential:", rho_differential)
print("rho_integral_s2:", rho_integral_s2)
print("rho_integral_s3:", rho_integral_s3)
print("rho_integral_s1:", rho_integral_s1)
print("z_s2:", z_s2)
print("drho_per_dz_s2:", drho_per_dz_s2)
print("excess_reactivity_s2:", excess_reactivity_s2)
print("z_s3:", z_s3)
print("drho_per_dz_s3:", drho_per_dz_s3)
print("excess_reactivity_s3:", excess_reactivity_s3)
print("z_s1:", z_s1)
print("drho_per_dz_s1:", drho_per_dz_s1)
print("excess_reactivity_s1:", excess_reactivity_s1)
print("excess_reactivity:", excess_reactivity)
print("excess_reactivity_avg:", excess_reactivity_avg)
print("rho_integral_max:", rho_integral_max)
print("rho_integral_max_sum:", rho_integral_max_sum)






print("===== Tabelle Messwerte =====")
for i in range(5):
    print(f"${power_start[i]:5.2f}\, W$ & ${s1[i]:6}$ & ${s2[i]:6}$ & ${s3[i]:6}$ & $  \infty  $ & $  \infty  $ & $  \infty  $ & $  \infty  $ & $  \infty  $ \\\\")
    print(f"${power_end[i]:5.2f}\, W$ & ${s1[i]:6}$ & ${s2[i + 1]:6}$ & ${s3[i]:6}$ & ${wb1_t2[i]:6.2f}\, s$ & ${wb2_t2[i]:6.2f}\, s$ & ${lb_t2[i]:6.2f}\, s$ & ${average_t2[i]:6.2f}\, s$ & ${average_ts[i]:6.2f}\, s$ \\\\")

print(f"${power_start[5]:5.2f}\, W$ & ${s1[5]:6}$ & ${s2[5]:6}$ & ${s3[5]:6}$ & $  \infty  $ & $  \infty  $ & $  \infty  $ & $  \infty  $ & $  \infty  $ \\\\")
print("\n\n")

print("===== Tabelle S2 berechnet =====")
for i in range(5):
    print(f"${s2[1:][i]:6}$ & ${average_ts[i]:6.2f}\, s$ & ${rho_differential[i]:.4f}$ & ${drho_per_dz_s2[1:][i]:.4f}$ & ${rho_integral_s2[1:][i]:.4f}\, \$$ \\\\")
print("\n\n")

print("===== Tabelle S3 berechnet =====")
for i in range(5):
    print(f"${s3[1:][i]:6}$ & ${drho_per_dz_s3[1:][i]:.4f}$ & ${rho_integral_s3[1:][i]:.4f}\, \$$ \\\\")
print("\n\n")

print("===== Tabelle S1 berechnet =====")
for i in range(5):
    print(f"${s1_avg[1:][i]:6}$ & ${drho_per_dz_s2[1:][i]:.4f}$ & ${rho_integral_s1[1:][i]:.4f}\, \$$ \\\\")
print("\n\n")

print("===== Tabelle Überschussreaktivität =====")
for i in range(6):
    print(f"${s1[i]:6}$ & ${s2[i]:6}$ & ${s3[::-1][i]:6}$ & ${excess_reactivity_s1[i]:6.4f}$ & ${excess_reactivity_s2[i]:6.4f}$ & ${excess_reactivity_s3[i]:6.4f}$ & ${excess_reactivity[i]:6.4f} $ \\\\")






fig, ax = plt.subplots()
green_patch = mpatches.Patch(color='tab:green', label='S1')
blue_patch = mpatches.Patch(color='tab:blue', label='S2')
yellow_patch = mpatches.Patch(color='tab:orange', label='S3')
ax.legend(handles=[green_patch, blue_patch, yellow_patch], prop={'size': 20})


# plot
plt.plot(z_s2, drho_per_dz_s2)
plt.plot(z_s3, drho_per_dz_s3)
plt.plot(z_s1, drho_per_dz_s1)

# points
plt.scatter(z_s2, drho_per_dz_s2)
plt.scatter(z_s3, drho_per_dz_s3)
plt.scatter(z_s1, drho_per_dz_s1)


# green lines
plt.plot([s2[x] for x in (0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5)], [drho_per_dz_s2[x] for x in (0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6)], c = "gray", linewidth=1)
plt.plot([s1[-1] - s1[-2]] * 2 + [s3[x] for x in (1, 1, 2, 2, 3, 3, 4, 4, 5, 5)], [drho_per_dz_s3[x] for x in (0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6)], c = "gray", linewidth=1)
plt.plot([(s1[-1] - s1[-2])/2] * 2 + [s1_avg[x] for x in (1, 1, 2, 2, 3, 3, 4, 4, 5, 5)], [drho_per_dz_s1[x] for x in (0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6)], c = "gray", linewidth=1)


plt.show()


fig, ax = plt.subplots()
green_patch = mpatches.Patch(color='tab:green', label='S1')
blue_patch = mpatches.Patch(color='tab:blue', label='S2')
yellow_patch = mpatches.Patch(color='tab:orange', label='S3')
ax.legend(handles=[green_patch, blue_patch, yellow_patch], prop={'size': 20})


plt.plot(s2, rho_integral_s2)
plt.plot(s3, rho_integral_s3)
plt.plot(s1_avg, rho_integral_s1)


# points
plt.scatter(s2, rho_integral_s2)
plt.scatter(s3, rho_integral_s3)
plt.scatter(s1_avg, rho_integral_s1)


# green lines
plt.plot([s2[x] for x in (0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5)], [rho_integral_s2[x] for x in (0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5)], c = "gray", linewidth=1)
plt.plot([s3[x] for x in (0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5)], [rho_integral_s3[x] for x in (0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5)], c = "gray", linewidth=1)
plt.plot([s1_avg[x] for x in (0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5)], [rho_integral_s1[x] for x in (0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5)], c = "gray", linewidth=1)


plt.show()
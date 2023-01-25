wb1_0_ein = (7.4, 7.3, 7.6)
wb1_0_aus = (9.4, 9.3, 9.6)
wb1_n0_ein = round(sum(wb1_0_ein) / 3, 4)
wb1_n0_aus = round(sum(wb1_0_aus) / 3, 4)
wb2_0_ein = (6.9, 6.6, 6.7)
wb2_0_aus = (10.4, 10.3, 10.1)
wb2_n0_ein = round(sum(wb2_0_ein) / 3, 4)
wb2_n0_aus = round(sum(wb2_0_aus) / 3, 4)
print("wb1_n0_ein", wb1_n0_ein)
print("wb1_n0_aus", wb1_n0_aus)
print("wb2_n0_ein", wb2_n0_ein)
print("wb2_n0_aus", wb2_n0_aus)
print()

hubhoehe_ein = [0] + [100, 200, 300, 400, 450, 500]
wb1_n1_ein = [8.5, 9.8, 12.5, 19.2, 31.1, 52.3]
wb1_n2_ein = [8.6, 9.9, 12.7, 18.8, 30.1, 52]
wb2_n1_ein = [8.2, 9.1, 11.9, 17.8, 28.5, 49.6]
wb2_n2_ein = [7.8, 9.2, 11.6, 18.4, 29.1, 49.2]

hubhoehe_aus = [0] + [100, 200, 300, 400, 450]
wb1_n1_aus = [10.8, 13.7, 18.5, 36.8, 87.4]
wb1_n2_aus = [10.7, 13.9, 18.3, 36.4, 88.6]
wb2_n1_aus = [11.9, 14.8, 21.5, 40.8, 96.7]
wb2_n2_aus = [11.5, 15.2, 20.8, 41.3, 99.3]

wb1_avg_ein = [wb1_n0_ein] + [round(sum(x) / 2, 3) for x in zip(wb1_n1_ein, wb1_n2_ein)]
wb1_avg_aus = [wb1_n0_aus] + [round(sum(x) / 2, 3) for x in zip(wb1_n1_aus, wb1_n2_aus)]
wb2_avg_ein = [wb2_n0_ein] + [round(sum(x) / 2, 3) for x in zip(wb2_n1_ein, wb2_n2_ein)]
wb2_avg_aus = [wb2_n0_aus] + [round(sum(x) / 2, 3) for x in zip(wb2_n1_aus, wb2_n2_aus)]
print("wb1_avg_ein", wb1_avg_ein)
print("wb1_avg_aus", wb1_avg_aus)
print("wb2_avg_ein", wb2_avg_ein)
print("wb2_avg_aus", wb2_avg_aus)
print()

wb1_ratio_ein = [round(wb1_n0_ein / x, 3) for x in wb1_avg_ein]
wb1_ratio_aus = [round(wb1_n0_aus / x, 3) for x in wb1_avg_aus]
wb2_ratio_ein = [round(wb2_n0_ein / x, 3) for x in wb2_avg_ein]
wb2_ratio_aus = [round(wb2_n0_aus / x, 3) for x in wb2_avg_aus]
print("wb1_ratio_ein", wb1_ratio_ein)
print("wb1_ratio_aus", wb1_ratio_aus)
print("wb2_ratio_ein", wb2_ratio_ein)
print("wb2_ratio_aus", wb2_ratio_aus)
print()

wb1_k_ein = [0.945]
for ni_1, ni in zip(wb1_avg_ein, wb1_avg_ein[1:]):
    wb1_k_ein.append(round(1 + (ni_1 / ni) * (wb1_k_ein[-1] - 1), 4))
wb1_k_aus = [0.945]
for ni_1, ni in zip(wb1_avg_aus, wb1_avg_aus[1:]):
    wb1_k_aus.append(round(1 + (ni_1 / ni) * (wb1_k_aus[-1] - 1), 4))

wb2_k_ein = [0.945]
for ni_1, ni in zip(wb2_avg_ein, wb2_avg_ein[1:]):
    wb2_k_ein.append(round(1 + (ni_1 / ni) * (wb2_k_ein[-1] - 1), 4))
wb2_k_aus = [0.945]
for ni_1, ni in zip(wb2_avg_aus, wb2_avg_aus[1:]):
    wb2_k_aus.append(round(1 + (ni_1 / ni) * (wb2_k_aus[-1] - 1), 4))

print("wb1_k_ein", wb1_k_ein)
print("wb1_k_aus", wb1_k_aus)
print("wb2_k_ein", wb2_k_ein)
print("wb2_k_aus", wb2_k_aus)
print()

wb1_M_ein = [round(1 / (1 - k), 4) for k in wb1_k_ein]
wb1_M_aus = [round(1 / (1 - k), 4) for k in wb1_k_aus]
wb2_M_ein = [round(1 / (1 - k), 4) for k in wb2_k_ein]
wb2_M_aus = [round(1 / (1 - k), 4) for k in wb2_k_aus]
print("wb1_M_ein", wb1_M_ein)
print("wb1_M_aus", wb1_M_aus)
print("wb2_M_ein", wb2_M_ein)
print("wb2_M_aus", wb2_M_aus)
print()

wb1_rho_ein = [round((k - 1) / k, 5) for k in wb1_k_ein]
wb1_rho_aus = [round((k - 1) / k, 5) for k in wb1_k_aus]
wb2_rho_ein = [round((k - 1) / k, 5) for k in wb2_k_ein]
wb2_rho_aus = [round((k - 1) / k, 5) for k in wb2_k_aus]
print("wb1_rho_ein", wb1_rho_ein)
print("wb1_rho_aus", wb1_rho_aus)
print("wb2_rho_ein", wb2_rho_ein)
print("wb2_rho_aus", wb2_rho_aus)
print()

# kritische Hubhoehe approximieren
calc_zero = lambda x1, x2, y1, y2: x2 + (-y2 / ((y2 - y1) / (x2 - x1)))
wb1_krit_ein = [calc_zero(*args) for args in zip(hubhoehe_ein, hubhoehe_ein[1:], wb1_ratio_ein, wb1_ratio_ein[1:])]
wb1_krit_aus = [calc_zero(*args) for args in zip(hubhoehe_aus, hubhoehe_aus[1:], wb1_ratio_aus, wb1_ratio_aus[1:])]
wb2_krit_ein = [calc_zero(*args) for args in zip(hubhoehe_ein, hubhoehe_ein[1:], wb2_ratio_ein, wb2_ratio_ein[1:])]
wb2_krit_aus = [calc_zero(*args) for args in zip(hubhoehe_aus, hubhoehe_aus[1:], wb2_ratio_aus, wb2_ratio_aus[1:])]
print("wb1_krit_ein", wb1_krit_ein)
print("wb1_krit_aus", wb1_krit_aus)
print("wb2_krit_ein", wb2_krit_ein)
print("wb2_krit_aus", wb2_krit_aus)

# Tabelle ausgeben
print("Tabelle WB1")
print("\\multirow{2}{*}{  0} & ein & \\multicolumn{3}{r|}{" + f"{round(wb1_avg_ein[0], 2):5.2f}" + "} & " + f"{wb1_ratio_ein[0]:5.3f} & {wb1_k_ein[0]:5.3f} & {wb1_M_ein[0]:6.2f} & {wb1_rho_ein[0]:7.4f} \\\\")
print("                     & aus & \\multicolumn{3}{r|}{" + f"{round(wb1_avg_aus[0], 2):5.2f}" + "} & " + f"{wb1_ratio_aus[0]:5.3f} & {wb1_k_aus[0]:5.3f} & {wb1_M_aus[0]:6.2f} & {wb1_rho_aus[0]:7.4f} \\\\")
for i in range(1, len(hubhoehe_aus)):
    print("\\midrule")
    print("\\multirow{2}{*}{" + f"{hubhoehe_ein[i]}" + "}" + f" & ein & {wb1_n1_ein[i-1]:6.1f} & {wb1_n2_ein[i-1]:6.1f} & {wb1_avg_ein[i]:8.2f} & {wb1_ratio_ein[i]:5.3f} & {wb1_k_ein[i]:5.3f} & {wb1_M_ein[i]:6.2f} & {wb1_rho_ein[i]:7.4f} \\\\")
    print(f"                     & ein & {wb1_n1_aus[i-1]:6.1f} & {wb1_n2_aus[i-1]:6.1f} & {wb1_avg_aus[i]:8.2f} & {wb1_ratio_aus[i]:5.3f} & {wb1_k_aus[i]:5.3f} & {wb1_M_aus[i]:6.2f} & {wb1_rho_aus[i]:7.4f} \\\\")
print("\\midrule")
print(f"                 {hubhoehe_ein[-1]} & ein & {wb1_n1_ein[-1]:6.1f} & {wb1_n2_ein[-1]:6.1f} & {wb1_avg_ein[-1]:8.2f} & {wb1_ratio_ein[-1]:5.3f} & {wb1_k_ein[-1]:5.3f} & {wb1_M_ein[-1]:6.2f} & {wb1_rho_ein[-1]:7.4f} \\\\")


print("\n\nTabelle WB2")
print("\\multirow{2}{*}{  0} & ein & \\multicolumn{3}{r|}{" + f"{round(wb2_avg_ein[0], 2):5.2f}" + "} & " + f"{wb2_ratio_ein[0]:5.3f} & {wb2_k_ein[0]:5.3f} & {wb2_M_ein[0]:6.2f} & {wb2_rho_ein[0]:7.4f} \\\\")
print("                     & aus & \\multicolumn{3}{r|}{" + f"{round(wb2_avg_aus[0], 2):5.2f}" + "} & " + f"{wb2_ratio_aus[0]:5.3f} & {wb2_k_aus[0]:5.3f} & {wb2_M_aus[0]:6.2f} & {wb2_rho_aus[0]:7.4f} \\\\")
for i in range(1, len(hubhoehe_aus)):
    print("\\midrule")
    print("\\multirow{2}{*}{" + f"{hubhoehe_ein[i]}" + "}" + f" & ein & {wb2_n1_ein[i-1]:6.1f} & {wb2_n2_ein[i-1]:6.1f} & {wb2_avg_ein[i]:8.2f} & {wb2_ratio_ein[i]:5.3f} & {wb2_k_ein[i]:5.3f} & {wb2_M_ein[i]:6.2f} & {wb2_rho_ein[i]:7.4f} \\\\")
    print(f"                     & ein & {wb2_n1_aus[i-1]:6.1f} & {wb2_n2_aus[i-1]:6.1f} & {wb2_avg_aus[i]:8.2f} & {wb2_ratio_aus[i]:5.3f} & {wb2_k_aus[i]:5.3f} & {wb2_M_aus[i]:6.2f} & {wb2_rho_aus[i]:7.4f} \\\\")
print("\\midrule")
print(f"                 {hubhoehe_ein[-1]} & ein & {wb2_n1_ein[-1]:6.1f} & {wb2_n2_ein[-1]:6.1f} & {wb2_avg_ein[-1]:8.2f} & {wb2_ratio_ein[-1]:5.3f} & {wb2_k_ein[-1]:5.3f} & {wb2_M_ein[-1]:6.2f} & {wb2_rho_ein[-1]:7.4f} \\\\")

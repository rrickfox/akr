import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import math
offset_quelle = 0.02

abstände = list(map(lambda x: x + offset_quelle, [0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1, 1.2, 1.5, 2, 2.5, 3]))
rgd = [1580, 840, 445, 182, 100, 65, 40, 32, 19, 11, 8.8, 6.5, 3.05, 2, 1.4]
lb133 = [4500, 1600, 750, 250, 140, 80, 50, 45, 30, 17, 10, 7.5, 4.5, 3.5, 2.25]
fh40 = [4600, 1150, 535, 185, 101, 63.3, 41.3, 29.6, 19.2, 12, 8.42, 6.9, 3.58, 2.75, 1.8]


leichtbeton_abstände = [round(x * 100) / 100 for x in map(lambda x: x + offset_quelle, [0.3, 0.4, 0.5, 0.6, 1.0, 1.5])]
leichtbeton_rgd = [60, 36, 24, 17.5, 6.4, 3.5]
leichtbeton_fh40 = [65.8, 37.7, 26, 18.8, 7.38, 3.7] 
leichtbeton_lb133 = [80, 45, 35, 20, 8, 3.5]

schwerbeton_abstände = [round(x * 100) / 100 for x in map(lambda x: x + offset_quelle, [0.3, 0.4, 0.5, 0.6, 1.0, 1.5])]
schwerbeton_fh40 = [4.84, 3.4, 2.74, 1.85, 1, 0.35]
schwerbeton_rgd = [4.35, 3, 2.5, 1, 0.5, 0.3]
schwerbeton_lb133 = [7.5, 3.5, 2.5, 1.8, 1, 0.55]

blei_abstände = [round(x * 100) / 100 for x in map(lambda x: x + offset_quelle, [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 1.0])]
blei_rgd = [2.4, 1.2, 0.3, 0.2, 10000, 10000, 10000]
blei_fh40 = [6, 3.39, 0.75, 0.69, 0.59, 0.43, 0.36]
blei_lb133 = [8, 3.5, 1.4, 0.7, 0.55, 0.3, 0.2]


(fig, ax) = plt.subplots()

plt.plot(abstände, rgd)
plt.plot(abstände, lb133)
plt.plot(abstände, fh40)

plt.scatter(abstände, rgd)
plt.scatter(abstände, lb133)
plt.scatter(abstände, fh40)

plt.xlabel(r"Abstand $r$")
plt.ylabel(r"Dosisleistung $P_x$")

plt.legend(["STEP RDG 27091", "Berthold LB 133-1", "Thermo FH40G"])

plt.yscale('log')
plt.xscale('log')

ax.set_xticks([], minor=True)
plt.xticks(abstände)

plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=None, hspace=None)

ax.xaxis.set_major_formatter(mticker.ScalarFormatter())
ax.ticklabel_format(style='plain', axis='x')

plt.show()





k = 92.5
a0 = 0.26
a = a0 * math.pow(math.e, ((-math.log(2)) * 29.75 / 30))

dosis_berechnet = [k * a / math.pow((x), 2) for x in abstände]

# print("*dosis_berechnet*")
# for i in range(len(abstände)):
#     print(f"$ {abstände[i]:6.2f} $ & $ {dosis_berechnet[i]:6.2f} $ \\\\")
# print()



dosis_rgd_prozent_fehler_abs = [abs((d / db)-1) for d, db in zip(rgd, dosis_berechnet)]

abstände_abschirmung = [round(x * 100) / 100 for x in sorted(set(leichtbeton_abstände).union(schwerbeton_abstände).union(blei_abstände))]

# print("*dosis_abschirmung*")
# for abstand in abstände_abschirmung:
#     leichtbeton = leichtbeton_abstände.index(abstand) if abstand in leichtbeton_abstände else -1
#     schwerbeton = schwerbeton_abstände.index(abstand) if abstand in schwerbeton_abstände else -1
#     blei = blei_abstände.index(abstand) if abstand in blei_abstände else -1

#     nothing = "    - "

#     leichtbeton_rgd_absch = f"{leichtbeton_rgd[leichtbeton]:6.2f}" if leichtbeton >= 0 else nothing
#     leichtbeton_fh40_absch = f"{leichtbeton_fh40[leichtbeton]:6.2f}" if leichtbeton >= 0 else nothing
#     leichtbeton_lb133_absch = f"{leichtbeton_lb133[leichtbeton]:6.2f}" if leichtbeton >= 0 else nothing

#     schwerbeton_rgd_absch = f"{schwerbeton_rgd[schwerbeton]:6.2f}" if schwerbeton >= 0 else nothing
#     schwerbeton_fh40_absch = f"{schwerbeton_fh40[schwerbeton]:6.2f}" if schwerbeton >= 0 else nothing
#     schwerbeton_lb133_absch = f"{schwerbeton_lb133[schwerbeton]:6.2f}" if schwerbeton >= 0 else nothing

#     blei_rgd_absch = f"{blei_rgd[blei]:6.2f}" if blei >= 0 else nothing
#     blei_fh40_absch = f"{blei_fh40[blei]:6.2f}" if blei >= 0 else nothing
#     blei_lb133_absch = f"{blei_lb133[blei]:6.2f}" if blei >= 0 else nothing

#     print(f"$ {abstand:6.2f} $ & $ {leichtbeton_rgd_absch} $ & $ {leichtbeton_fh40_absch} $ & $ {leichtbeton_lb133_absch} $ & $ {schwerbeton_rgd_absch} $ & $ {schwerbeton_fh40_absch} $ & $ {schwerbeton_lb133_absch} $ & $ {blei_rgd_absch} $ & $ {blei_fh40_absch} $ & $ {blei_lb133_absch} $ \\\\")
# print()

def calc_coeff(x, Px, Px0):
    return [-(math.log(Px / Px0) / x) for (Px, Px0) in zip(Px, Px0)]

leichtbeton_rgd_koeff = calc_coeff(0.2, leichtbeton_rgd, rgd[4:8] + [rgd[9], rgd[11]])
leichtbeton_fh40_koeff = calc_coeff(0.2, leichtbeton_fh40, fh40[4:8] + [fh40[9], fh40[11]])
leichtbeton_lb133_koeff = calc_coeff(0.2, leichtbeton_lb133, lb133[4:8] + [lb133[9], lb133[11]])
leichtbeton_koeff = [(x + y + z) / 3 for (x, y, z) in zip(leichtbeton_rgd_koeff, leichtbeton_fh40_koeff, leichtbeton_lb133_koeff)]

schwerbeton_rgd_koeff = calc_coeff(0.2, schwerbeton_rgd, rgd[4:8] + [rgd[9], rgd[11]])
schwerbeton_fh40_koeff = calc_coeff(0.2, schwerbeton_fh40, fh40[4:8] + [fh40[9], fh40[11]])
schwerbeton_lb133_koeff = calc_coeff(0.2, schwerbeton_lb133, lb133[4:8] + [lb133[9], lb133[11]])
schwerbeton_koeff = [(x + y + z) / 3 for (x, y, z) in zip(schwerbeton_rgd_koeff, schwerbeton_fh40_koeff, schwerbeton_lb133_koeff)]

blei_rgd_koeff = calc_coeff(0.05, blei_rgd, rgd[1:7] + [rgd[9]])
blei_fh40_koeff = calc_coeff(0.05, blei_fh40, fh40[1:7] + [fh40[9]])
blei_lb133_koeff = calc_coeff(0.05, blei_lb133, lb133[1:7] + [lb133[9]])
blei_koeff = [(x + y + z) / 3 for (x, y, z) in zip(blei_rgd_koeff, blei_fh40_koeff, blei_lb133_koeff)]

# print("*leichtbeton_coeff: *")
# print(f"$ Abstände $ & $ rgd_coeff $ & $ fh40_coeff $ & $ lb133_coeff $ & $ average_coeff $ \\\\")
# for i in range(len(leichtbeton_koeff)):
#     print(f"$ {leichtbeton_abstände[i]:6.2f} $ & $ {leichtbeton_rgd_koeff[i]:6.2f} $ & $ {leichtbeton_fh40_koeff[i]:6.2f} $ & $ {leichtbeton_lb133_koeff[i]:6.2f} $ & $ {leichtbeton_koeff[i]:6.2f} $ \\\\")

# print(f"$ averag $ & $ {sum(leichtbeton_rgd_koeff) / len(leichtbeton_rgd_koeff):6.2f} $ & $ {sum(leichtbeton_fh40_koeff) / len(leichtbeton_fh40_koeff):6.2f} $ & $ {sum(leichtbeton_lb133_koeff) / len(leichtbeton_lb133_koeff):6.2f} $ & $ {sum(leichtbeton_koeff) / len(leichtbeton_koeff):6.2f} $ \\\\")
# print()


# print("*schwerbeton_coeff: *")
# print(f"$ Abstände $ & $ rgd_coeff $ & $ fh40_coeff $ & $ lb133_coeff $ & $ average_coeff $ \\\\")
# for i in range(len(schwerbeton_koeff)):
#     print(f"$ {schwerbeton_abstände[i]:6.2f} $ & $ {schwerbeton_rgd_koeff[i]:6.2f} $ & $ {schwerbeton_fh40_koeff[i]:6.2f} $ & $ {schwerbeton_lb133_koeff[i]:6.2f} $ & $ {schwerbeton_koeff[i]:6.2f} $ \\\\")

# print(f"$ averag $ & $ {sum(schwerbeton_rgd_koeff) / len(schwerbeton_rgd_koeff):6.2f} $ & $ {sum(schwerbeton_fh40_koeff) / len(schwerbeton_fh40_koeff):6.2f} $ & $ {sum(schwerbeton_lb133_koeff) / len(schwerbeton_lb133_koeff):6.2f} $ & $ {sum(schwerbeton_koeff) / len(schwerbeton_koeff):6.2f} $ \\\\")
# print()


# print("*blei_coeff: *")
# print(f"$ Abstände $ & $ rgd_coeff $ & $ fh40_coeff $ & $ lb133_coeff $ & $ average_coeff $ \\\\")
# for i in range(len(blei_koeff)):
#     print(f"$ {blei_abstände[i]:6.2f} $ & $ {blei_rgd_koeff[i]:6.2f} $ & $ {blei_fh40_koeff[i]:6.2f} $ & $ {blei_lb133_koeff[i]:6.2f} $ & $ {blei_koeff[i]:6.2f} $ \\\\")

# print(f"$ averag $ & $ {sum(blei_rgd_koeff) / len(blei_rgd_koeff):6.2f} $ & $ {sum(blei_fh40_koeff) / len(blei_fh40_koeff):6.2f} $ & $ {sum(blei_lb133_koeff) / len(blei_lb133_koeff):6.2f} $ & $ {sum(blei_koeff) / len(blei_koeff):6.2f} $ \\\\")
# print()



print("A:", a)
print("dosis_berechnet", dosis_berechnet)
print("dosis_rgd_prozent_fehler_abs", dosis_rgd_prozent_fehler_abs)
print("dosis_rgd_prozent_fehler_abs average", sum(dosis_rgd_prozent_fehler_abs[4:])/len(dosis_rgd_prozent_fehler_abs[4:]))
print("leichtbeton_fh40_koeff", leichtbeton_fh40_koeff)
print("leichtbeton_rgd_koeff", leichtbeton_rgd_koeff)
print("leichtbeton_lb133_koeff", leichtbeton_lb133_koeff)
print("schwerbeton_rgd_koeff", schwerbeton_rgd_koeff)
print("schwerbeton_fh40_koeff", schwerbeton_fh40_koeff)
print("schwerbeton_lb133_koeff", schwerbeton_lb133_koeff)
print("blei_rgd_koeff", blei_rgd_koeff)
print("blei_fh40_koeff", blei_fh40_koeff)
print("blei_lb133_koeff", blei_lb133_koeff)

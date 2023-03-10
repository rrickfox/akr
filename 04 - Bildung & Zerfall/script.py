_ = [24505, 23967, 24063, 23525, 11971, 11433]
_ = [21163, 20625, 22350, 21812, 11134, 10596]
_ = [18339, 17801, 20668, 20130, 10651, 10113]
_ = [15840, 15302, 19868, 19330, 10252, 10113]
_ = [13718, 13180, 18376, 17838, 9285, 8747]
_ = [11656, 11118, 17582, 17044, 8809, 8271]
_ = [10279, 9741, 16477, 15939, 8314, 7776]
_ = [8744, 8206, 15461, 14923, 8117, 7579]
_ = [7612, 7074, 14629, 14097, 7423, 6885]
_ = [6536, 5998, 13838, 13300, 7081, 6543]
_ = [5961, 5423, 12893, 12355, 6791, 6253]
_ = [5102, 4564, 12004, 11466, 6380, 5842]
_ = [4426, 3888, 11673, 11135, 6026, 5488]
_ = [3948, 3410, 11196, 10658, 5638, 5100]
_ = [3381, 2843, 10355, 9817, 5410, 4872]
_ = [3060, 2522, 10077, 9539, 5180, 4642]
_ = [2691, 2153, 9477, 8939, 4852, 4314]
_ = [2300, 1762, 9009, 8471, 4645, 4107]
_ = [1930, 1392, 8152, 7614, 4096, 3558]

import math

n0 = 538
ta = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 10.0]

ni_al = [24505, 21163, 18339, 15840, 13718, 11656, 10279, 8744, 7612, 6536, 5961, 5102, 4426, 3948, 3381, 3060, 2691, 2300, 1930]
ni_cu = [24063, 22350, 20668, 19868, 18376, 17582, 16477, 15461, 14629, 13838, 12893, 12004, 11673, 11196, 10355, 10077, 9477, 9009, 8152]
ni_x = [11971, 11134, 10651, 10252, 9285, 8809, 8314, 8117, 7423, 7081, 6791, 6380, 6026, 5638, 5410, 5180, 4852, 4645, 4096]


ni0_al = [n - n0 for n in ni_al]
ni0_cu = [n - n0 for n in ni_cu]
ni0_x = [n - n0 for n in ni_x]


func_al = lambda x: math.exp(10.2344 - 0.3021 * x)
func_al_inv = lambda y: (math.log(y) - 10.2344) / (- 0.3021)

func_cu = lambda x: math.exp(10.0940 - 0.1182 * x)
func_cu_inv = lambda y: (math.log(y) - 10.0940) / (- 0.1182)

func_x = lambda x: math.exp(9.3969 - 0.1210 * x)
func_x_inv = lambda y: (math.log(y) - 9.3969) / (- 0.1210)

halb_al = func_al_inv(func_al(100) / 2) - 100
halb_cu = func_cu_inv(func_cu(100) / 2) - 100
halb_x = func_x_inv(func_x(100) / 2) - 100

Ztb_al = func_al(0) / 6
Ztb_cu = func_cu(0) / 6
Ztb_x = func_x(0) / 6
n0 /= 6

Nl = 6.025 * 1e23
V = math.pi * pow(3 / 2, 2) * 0.1
tb = 10
C = 0.01

AG_cu = 65
AG_al = 27
AG_x = None

wirk_cu = 2.1 * 1e-24
wirk_al = 0.215 * 1e-24
wirk_x = None # * 1e-24

rho_cu = 8.92
rho_al = 2.2


phi_cu = (Ztb_cu - n0) * AG_cu / (C * V * rho_cu * 0.309 * Nl * wirk_cu * (1 - math.exp(- math.log(2) / halb_cu * tb)))
phi_al = (Ztb_al - n0) * AG_al / (C * V * rho_al * Nl * wirk_al * (1 - math.exp(- math.log(2) / halb_al * tb)))

# g cm?? mol / s mol cm?? g cm??


print("ta:", ' '.join(map(str, ta)))
print("ni0_al:", ' '.join(map(str, ni0_al)))
print("ni0_cu:", ' '.join(map(str, ni0_cu)))
print("ni0_x:", ' '.join(map(str, ni0_x)))
print("n0 (1sec):", n0)
print("halb_al:", halb_al)
print("halb_cu:", halb_cu)
print("halb_x:", halb_x)
print("Ztb_al:", Ztb_al)
print("Ztb_cu:", Ztb_cu)
print("Ztb_x:", Ztb_x)
print("phi_cu:", phi_cu)
print("phi_al:", phi_al)
print("phi_avg:", (phi_al + phi_cu) / 2)
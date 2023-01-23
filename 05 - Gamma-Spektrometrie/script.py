'''
- Kalibrierung Szintillator
keV  | Kanal
-----+------
662  | 1500
1173 | 2575
1332 | 2920

- Kalibrierung Halbleiter
keV  | Kanal
-----+------
662  | 1530
1173 | 2704
1332 | 3072


Probengewicht: 6.08 g

Cu-66: Kanal 2395 / 1039 keV (Datenbank: Iod-135)
Cu-64: Kanal 1177 / 507 keV (Datenbank: Caesium-136)

Abklingzeit		| LiveT	| Cu-66 Gross / Net	| Cu-64 Gross / Net	| Verhältnis
----------------+-------+-------------------+-------------------+------------
~10 s			| 200 s	| 2519 / 2303 ± 68 	| 2894 / 1640 ± 121	| 0.71211
200 s + 10 min	| 200 s	| 470 / 398 ± 34	| 2078 / 1664 ± 77	| 4.1809


- Fotopeaks unbekannte Probe 1 (Indium-116m)
128, 441, 817, 1097, 1292, 1505

- Fotopeaks unbekannte Probe 2 (Radium-Leuchtfarbe)
186, 243, 285, 352, 610, 769, 934, 1121, 1238

- Kalibrierung unbekannte Probe 2
keV	| Kanal
----+-------
186	| 428 
243	| 559 
295	| 679 
352	| 810 
610	| 1406 


'''

import matplotlib.pyplot as plt
import os, math
from typing import Tuple, List, Literal

def get_data(filename: str) -> Tuple[List[int], List[Tuple[int, int]] | Literal[False]]:
    with open(filename) as file:
        data = file.read()

    data = data.split("0 4095\n")[1]
    data, roi = data.split("\n$ROI:\n")
    roi = roi.split("\n$PRESETS:")[0]

    data = [int(x.strip()) for x in data.split("\n")]
    roi = [tuple(map(int, x.split(" "))) if x.count(" ") > 0 else (int(x), int(x)) for x in roi.split("\n")] if roi.count("\n") > 1 else False

    return data, roi

def get_peaks(data: List[int], min_height: int, resolution: int = 10, mult: float = 5) -> List[int]:
    gradient = [y2 - y1 for y1, y2 in zip(data, data[1:])]

    peak_indices = [i+1 for i, (y1, y2) in enumerate(zip(gradient, gradient[1:])) if (y1 > y2 and y1 > 0 > y2)]

    true_peaks = [i for i in peak_indices if (data[i] > min_height and i - resolution >= 0 and data[i] >= mult * data[i - resolution] and i + resolution < len(data) and data[i] >= mult * data[i + resolution])]

    p = set()
    for peak in true_peaks:
        m = max((data[i], i) for i in range(peak - resolution, peak + resolution + 1) if i in true_peaks)
        p.add(m[1])

    return list(sorted(p))

def get_area(data: List[int], left: int, right: int) -> Tuple[int, int]:
    gross = sum(data[left:right+1])

    dx = (right - left)
    diff = ((data[left] + data[right]) / 2) * dx

    return gross, gross - diff

# settings
all_files = False
render = True
render_peaks = False

# file
f = "gruppe_3.Spe"

# params
best_height = {"gruppe_3.Spe": 60, "Co_60.Spe": 40, "Ba_133.Spe": 50, "Cu_1.Spe": 100}
best_res = {}
best_mult = {"gruppe_3.Spe": 2, "Ba_133.Spe": 6}

if all_files:
    for filename in os.listdir():
        if not filename.endswith(".Spe"):
            continue

        data, _ = get_data(filename)

        peaks = get_peaks(data, best_height.get(f, max(data) // 2), best_res.get(f, 10), best_mult.get(f, 5))
        print(filename, peaks)
        data = [1 if i in peaks else 0 for i in range(0, len(data))] if render_peaks else data

        if render:
            plt.title(filename)
            plt.plot(data)
            plt.subplots_adjust(left=0.05, bottom=0.05, right=0.98, top=0.95, wspace=None, hspace=None)
            plt.show()
else:
    data, _ = get_data(f)

    peaks = get_peaks(data, best_height.get(f, max(data) // 2), best_res.get(f, 10), best_mult.get(f, 5))
    print(f, peaks)
    
    if f == "gruppe_3.Spe":
        kalib = lambda x: 0.43345 * x + 0.66809
        
        for i in range(len(peaks)):
            print(f"{peaks[i]} & {kalib(peaks[i]):6.2f} \\\\")


    data = [1 if i in peaks else 0 for i in range(0, len(data))] if render_peaks else data

    if render:
        plt.title(f)
        plt.plot(data)
        plt.subplots_adjust(left=0.05, bottom=0.05, right=0.98, top=0.95, wspace=None, hspace=None)
        plt.show()

# plot energiekalibrierung
peaks_co_60 = get_peaks(get_data("Co_60.Spe")[0], best_height["Co_60.Spe"])
data_cs_137 = get_data("Cs_137.Spe")[0]
peaks_cs_137 = get_peaks(data_cs_137, max(data_cs_137) // 2)

# plt.title("Energiekalibrierung")
# plt.plot(peaks_co_60+peaks_cs_137, [1173, 1332, 662])
# plt.subplots_adjust(left=0.05, bottom=0.05, right=0.98, top=0.95, wspace=None, hspace=None)
# plt.show()

# calculate area of peaks in copper:
print()
a = get_area(get_data("Cu_1.Spe")[0], 2655, 2667)[1]
b = get_area(get_data("Cu_2.Spe")[0], 2655, 2667)[1]

wait_time = 10 * 60
measure_time = 200
total_time = wait_time + 1/2 * measure_time
half_life = 5.12 * 60
print("actual half life:", half_life)

print("theoretical time:", - math.log(b / a) * half_life / math.log(2))
print("calculated half life:", (- math.log(2) * total_time) / math.log(b / a))
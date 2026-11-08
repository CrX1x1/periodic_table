from ti_draw import *
from ti_system import *
from ti_graphics import *
from math import *
selected_color=(2,107,249)#so i don't forget what color the Evo uses for selected stuff in text
E = [ # Couldn't be bothered with inputting all this manually, i just used AI lol
    (),
    ("Hydrogen", 1, "H", 1.008, 0, 1, "1s¹", 32, 1312, 2.2, "0.000082", -259.16, -252.879, "Gas", "+-1", 1766),
    ("Helium", 2, "He", 4.0026, 2, 2, "1s²", 37, 2372, "N/A", 0.000164, -272.2, -268.928, "Gas", "0", 1868),
    ("Lithium", 3, "Li", 6.94, 4, 3, "1s² 2s¹", 130, 520, "0.98", 0.534, 180.5, 1342, "Solid", "+1", 1817),
    ("Beryllium", 4, "Be", 9.0122, 5, 4, "1s² 2s²", 99, 899, 1.57, 1.85, 1287, 2468, "Solid", "+2", 1798),
    ("Boron", 5, "B", 10.81, 6, 5, "1s² 2s² 2p¹", 84, 801, 2.04, 2.34, 2077, 4000, "Solid", "+3", 1808),
    ("Carbon", 6, "C", 12.011, 6, 6, "1s² 2s² 2p²", 75, 1086, 2.55, 2.26, 3550, 4027, "Solid", "+-4, +2", "ANCIENT"),
    ("Nitrogen", 7, "N", 14.007, 7, 7, "1s² 2s² 2p³", 71, 1402, 3.04, 0.001145, -210.0, -195.795, "Gas", "+-3, +5, +4", 1772),
    ("Oxygen", 8, "O", 15.999, 8, 8, "1s² 2s² 2p⁴", 66, 1314, 3.44, 0.001308, -218.79, -182.96, "Gas", "-2", 1774),
    ("Fluorine", 9, "F", 18.998, 10, 9, "1s² 2s² 2p⁵", 57, 1681, 3.98, 0.001553, -219.67, -188.11, "Gas", "-1", 1886),
    ("Neon", 10, "Ne", 20.180, 10, 10, "[He] 2s² 2p⁶", 58, 2081, "N/A", 0.000825, -248.59, -246.046, "Gas", "0", 1898),
    ("Sodium", 11, "Na", 22.990, 12, 11, "[Ne] 3s¹", 166, 496, "0.93", 0.968, "97.794", "882.94", "Solid", "+1", 1807),
    ("Magnesium", 12, "Mg", 24.305, 12, 12, "[Ne] 3s²", 141, 738, 1.31, 1.738, 650, 1090, "Solid", "+2", 1755),
    ("Aluminum", 13, "Al", 26.982, 14, 13, "[Ne] 3s² 3p¹", 121, 578, 1.61, 2.70, "660.32", 2470, "Solid", "+3", 1825),
    ("Silicon", 14, "Si", 28.085, 14, 14, "[Ne] 3s² 3p²", 111, 787, 1.9, 2.329, 1414, 3265, "Solid", "+4, -4", 1824),
    ("Phosphorus", 15, "P", 30.974, 16, 15, "[Ne] 3s² 3p³", 107, 1012, 2.19, 1.823, 44.15, 280.5, "Solid", "+5, +3, -3", 1669),
    ("Sulfur", 16, "S", 32.06, 16, 16, "[Ne] 3s² 3p⁴", 105, 1000, 2.58, 2.07, 115.21, "444.6", "Solid", "+6, +4, -2", "ANCIENT"),
    ("Chlorine", 17, "Cl", 35.45, 18, 17, "[Ne] 3s² 3p⁵", 102, 1251, 3.16, 0.002898, -101.5, -34.04, "Gas", "-1, +1, +3, +5, +7", 1774),
    ("Argon", 18, "Ar", 39.948, 22, 18, "[Ne] 3s² 3p⁶", 106, 1521, "N/A", 0.001633, -189.34, -185.85, "Gas", "0", 1894),
    ("Potassium", 19, "K", 39.098, 20, 19, "[Ar] 4s¹", 203, 419, "0.82", 0.856, "63.5", 759, "Solid", "+1", 1807),
    ("Calcium", 20, "Ca", 40.078, 20, 20, "[Ar] 4s²", 176, 590, 1.0, 1.55, 842, 1484, "Solid", "+2", 1808),
    ("Scandium", 21, "Sc", 44.956, 24, 21, "[Ar] 3d¹ 4s²", 170, 633, 1.36, 2.985, 1541, 2836, "Solid", "+3", 1879),
    ("Titanium", 22, "Ti", 47.867, 26, 22, "[Ar] 3d² 4s²", 160, 659, 1.54, 4.506, 1668, 3287, "Solid", "+4, +3", 1791),
    ("Vanadium", 23, "V", "50.942", 28, 23, "[Ar] 3d³ 4s²", 153, 651, 1.63, 6.11, 1910, 3407, "Solid", "+5, +4, +3, +2", 1801),
    ("Chromium", 24, "Cr", 51.996, 28, 24, "[Ar] 3d⁵ 4s¹", 139, 653, 1.66, 7.19, 1907, 2671, "Solid", "+3, +6, +2", 1797),
    ("Manganese", 25, "Mn", 54.938, 30, 25, "[Ar] 3d⁵ 4s²", 139, 717, 1.55, 7.21, 1246, 2061, "Solid", "+2, +4, +7", 1774),
    ("Iron", 26, "Fe", 55.845, 30, 26, "[Ar] 3d⁶ 4s²", 132, 763, 1.83, 7.874, 1538, 2862, "Solid", "+3, +2", "ANCIENT"),
    ("Cobalt", 27, "Co", 58.933, 32, 27, "[Ar] 3d⁷ 4s²", 126, 760, 1.88, 8.90, 1495, 2927, "Solid", "+2, +3", 1735),
    ("Nickel", 28, "Ni", 58.693, 31, 28, "[Ar] 3d⁸ 4s²", 124, 737, 1.91, "8.908", 1455, 2730, "Solid", "+2, +3", 1751),
    ("Copper", 29, "Cu", 63.546, 35, 29, "[Ar] 3d¹⁰ 4s¹", 132, 746, 1.9, "8.96", 1084.62, 2562, "Solid", "+2, +1", "ANCIENT"),
    ("Zinc", 30, "Zn", 65.38, 35, 30, "[Ar] 3d¹⁰ 4s²", 122, 906, 1.65, 7.14, 419.53, 907, "Solid", "+2", 1746),
    ("Gallium", 31, "Ga", "69.723", 39, 31, "[Ar] 3d¹⁰ 4s² 4p¹", 122, 579, 1.81, 5.91, "29.76", 2204, "Solid", "+3", 1875),
    ("Germanium", 32, "Ge", 72.630, 41, 32, "[Ar] 3d¹⁰ 4s² 4p²", 120, 762, 2.01, 5.323, 938.25, 2833, "Solid", "+4, +2", 1886),
    ("Arsenic", 33, "As", 74.922, 42, 33, "[Ar] 3d¹⁰ 4s² 4p³", 119, 947, 2.18, 5.727, 817, 614, "Solid", "+3, +5, -3", 1250),
    ("Selenium", 34, "Se", "78.971", 45, 34, "[Ar] 3d¹⁰ 4s² 4p⁴", 120, 941, 2.55, 4.81, 221, 685, "Solid", "+4, +6, -2", 1817),
    ("Bromine", 35, "Br", 79.904, 45, 35, "[Ar] 3d¹⁰ 4s² 4p⁵", 120, 1140, 2.96, 3.1028, -7.2, 58.8, "Liquid", "-1, +1, +5", 1826),
    ("Krypton", 36, "Kr", "83.798", 48, 36, "[Ar] 3d¹⁰ 4s² 4p⁶", 116, 1351, 3.0, 0.00375, -157.36, -153.22, "Gas", "0", 1898),
    ("Rubidium", 37, "Rb", "85.468", 48, 37, "[Kr] 5s¹", 235, 403, "0.82", 1.532, 39.3, 688, "Solid", "+1", 1861),
    ("Strontium", 38, "Sr", 87.62, 50, 38, "[Kr] 5s²", 200, 549, 0.95, 2.64, 777, 1382, "Solid", "+2", 1790),
    ("Yttrium", 39, "Y", "88.906", 50, 39, "[Kr] 4d¹ 5s²", 180, 600, 1.22, 4.472, 1526, 3336, "Solid", "+3", 1794),
    ("Zirconium", 40, "Zr", "91.224", 51, 40, "[Kr] 4d² 5s²", 160, 640, 1.33, 6.52, 1855, 4409, "Solid", "+4", 1789),
    ("Niobium", 41, "Nb", "92.906", 52, 41, "[Kr] 4d⁴ 5s¹", 146, 652, 1.6, 8.57, 2477, 4744, "Solid", "+5, +3", 1801),
    ("Molybdenum", 42, "Mo", "95.95", 54, 42, "[Kr] 4d⁵ 5s¹", 139, 684, 2.16, 10.28, 2623, 4639, "Solid", "+6", 1778),
    ("Technetium", 43, "Tc", "98.0", 55, 43, "[Kr] 4d⁵ 5s²", 136, 702, 1.9, 11.5, 2157, 4265, "Solid", "+7, +4", 1937),
    ("Ruthenium", 44, "Ru", 101.07, 57, 44, "[Kr] 4d⁷ 5s¹", 134, 710, 2.2, 12.45, 2334, 4150, "Solid", "+3, +4, +8", 1844),
    ("Rhodium", 45, "Rh", 102.91, 58, 45, "[Kr] 4d⁸ 5s¹", 134, 720, 2.28, 12.41, 1964, 3695, "Solid", "+3", 1803),
    ("Palladium", 46, "Pd", 106.42, 60, 46, "[Kr] 4d¹⁰", 137, 804, 2.2, 12.023, 1554.9, 2963, "Solid", "+2, +4", 1803),
    ("Silver", 47, "Ag", 107.87, 61, 47, "[Kr] 4d¹⁰ 5s¹", 144, 731, 1.93, 10.49, "961.78", 2162, "Solid", "+1", "ANCIENT"),
    ("Cadmium", 48, "Cd", 112.41, 64, 48, "[Kr] 4d¹⁰ 5s²", 151, 868, 1.69, 8.65, 321.07, 767, "Solid", "+2", 1817),
    ("Indium", 49, "In", 114.82, 66, 49, "[Kr] 4d¹⁰ 5s² 5p¹", 167, 558, 1.78, 7.31, 156.6, 2072, "Solid", "+3", 1863),
    ("Tin", 50, "Sn", 118.71, 69, 50, "[Kr] 4d¹⁰ 5s² 5p²", 140, 709, 1.96, 7.287, 231.93, 2602, "Solid", "+4, +2", "ANCIENT"),
    ("Antimony", 51, "Sb", 121.76, 71, 51, "[Kr] 4d¹⁰ 5s² 5p³", 140, 834, 2.05, 6.697, 630.63, 1587, "Solid", "+3, +5, -3", 1540),
    ("Tellurium", 52, "Te", 127.60, 76, 52, "[Kr] 4d¹⁰ 5s² 5p⁴", 142, 869, 2.1, 6.24, 449.51, 988, "Solid", "+4, +6, -2", 1782),
    ("Iodine", 53, "I", 126.90, 74, 53, "[Kr] 4d¹⁰ 5s² 5p⁵", 133, 1008, 2.66, 4.933, 113.7, 184.3, "Solid", "-1, +1, +5, +7", 1811),
    ("Xenon", 54, "Xe", 131.29, 78, 54, "[Kr] 4d¹⁰ 5s² 5p⁶", 131, 1170, 2.6, 0.005894, -111.75, -108.09, "Gas", "0", 1898),
    ("Cesium", 55, "Cs", 132.91, 78, 55, "[Xe] 6s¹", 267, 376, 0.79, 1.93, 28.5, 671, "Solid", "+1", 1860),
    ("Barium", 56, "Ba", 137.33, 81, 56, "[Xe] 6s²", 222, 503, 0.89, 3.51, 727, 1897, "Solid", "+2", 1808),
    ("Lanthanum", 57, "La", 138.91, 82, 57, "[Xe] 5d¹ 6s²", 187, 538, 1.1, 6.162, 920, 3464, "Solid", "+3", 1839),
    ("Cerium", 58, "Ce", 140.12, 82, 58, "[Xe] 4f¹ 5d¹ 6s²", 181, 534, 1.12, 6.77, 798, 3443, "Solid", "+3, +4", 1803),
    ("Praseodymium", 59, "Pr", 140.91, 82, 59, "[Xe] 4f³ 6s²", 182, 527, 1.13, 6.77, 931, 3520, "Solid", "+3", 1885),
    ("Neodymium", 60, "Nd", 144.24, 84, 60, "[Xe] 4f⁴ 6s²", 181, 533, 1.14, 7.01, 1024, 3074, "Solid", "+3", 1885),
    ("Promethium", 61, "Pm", 145.0, 84, 61, "[Xe] 4f⁵ 6s²", 183, 540, 1.13, 7.26, 1042, 3000, "Solid", "+3", 1945),
    ("Samarium", 62, "Sm", 150.36, 88, 62, "[Xe] 4f⁶ 6s²", 180, 545, 1.17, 7.52, 1072, 1794, "Solid", "+3, +2", 1879),
    ("Europium", 63, "Eu", 151.96, 89, 63, "[Xe] 4f⁷ 6s²", 180, 547, 1.2, 5.244, 822, 1529, "Solid", "+3, +2", 1901),
    ("Gadolinium", 64, "Gd", 157.25, 93, 64, "[Xe] 4f⁷ 5d¹ 6s²", 180, 593, 1.2, 7.90, 1313, 3273, "Solid", "+3", 1880),
    ("Terbium", 65, "Tb", 158.93, 94, 65, "[Xe] 4f⁹ 6s²", 177, 566, 1.2, 8.23, 1356, 3230, "Solid", "+3, +4", 1843),
    ("Dysprosium", 66, "Dy", 162.50, 96, 66, "[Xe] 4f¹⁰ 6s²", 178, 573, 1.22, "8.55", 1407, 2567, "Solid", "+3", 1886),
    ("Holmium", 67, "Ho", 164.93, 98, 67, "[Xe] 4f¹¹ 6s²", 176, 581, 1.23, "8.80", 1474, 2700, "Solid", "+3", 1878),
    ("Erbium", 68, "Er", 167.26, 99, 68, "[Xe] 4f¹² 6s²", 176, 589, 1.24, "9.066", 1529, 2868, "Solid", "+3", 1843),
    ("Thulium", 69, "Tm", 168.93, 100, 69, "[Xe] 4f¹³ 6s²", 176, 597, 1.25, 9.32, 1545, 1950, "Solid", "+3, +2", 1879),
    ("Ytterbium", 70, "Yb", 173.05, 103, 70, "[Xe] 4f¹⁴ 6s²", 176, 603, 1.1, 6.90, 824, 1196, "Solid", "+3, +2", 1878),
    ("Lutetium", 71, "Lu", 174.97, 104, 71, "[Xe] 4f¹⁴ 5d¹ 6s²", 174, 524, 1.27, "9.841", 1663, 3402, "Solid", "+3", 1907),
    ("Hafnium", 72, "Hf", 178.49, 106, 72, "[Xe] 4f¹⁴ 5d² 6s²", 159, 659, 1.3, 13.31, 2233, 4603, "Solid", "+4", 1923),
    ("Tantalum", 73, "Ta", 180.95, 108, 73, "[Xe] 4f¹⁴ 5d³ 6s²", 146, 761, 1.5, 16.69, 3017, 5458, "Solid", "+5", 1802),
    ("Tungsten", 74, "W", 183.84, 110, 74, "[Xe] 4f¹⁴ 5d⁴ 6s²", 139, 770, 2.36, 19.25, 3422, 5555, "Solid", "+6", 1783),
    ("Rhenium", 75, "Re", 186.21, 111, 75, "[Xe] 4f¹⁴ 5d⁵ 6s²", 137, 760, 1.9, 21.02, 3186, 5596, "Solid", "+7, +4", 1925),
    ("Osmium", 76, "Os", 190.23, 114, 76, "[Xe] 4f¹⁴ 5d⁶ 6s²", 135, 840, 2.2, 22.59, 3033, 5012, "Solid", "+4, +3, +8", 1803),
    ("Iridium", 77, "Ir", 192.22, 115, 77, "[Xe] 4f¹⁴ 5d⁷ 6s²", 136, 880, 2.2, 22.56, 2446, 4428, "Solid", "+4, +3", 1803),
    ("Platinum", 78, "Pt", 195.08, 117, 78, "[Xe] 4f¹⁴ 5d⁹ 6s¹", 139, 870, 2.28, 21.45, 1768.3, 3825, "Solid", "+4, +2", 1735),
    ("Gold", 79, "Au", 196.97, 118, 79, "[Xe] 4f¹⁴ 5d¹⁰ 6s¹", 144, 890, 2.54, 19.3, 1064.18, 2856, "Solid", "+3, +1", "ANCIENT"),
    ("Mercury", 80, "Hg", 200.59, 121, 80, "[Xe] 4f¹⁴ 5d¹⁰ 6s²", 151, 1007, 2.0, 13.534, -38.83, 356.73, "Liquid", "+2, +1", "ANCIENT"),
    ("Thallium", 81, "Tl", 204.38, 123, 81, "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p¹", 170, 589, 1.62, 11.85, 304, 1473, "Solid", "+1, +3", 1861),
    ("Lead", 82, "Pb", 207.2, 125, 82, "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p²", 146, 716, 1.87, 11.34, 327.46, 1749, "Solid", "+2, +4", "ANCIENT"),
    ("Bismuth", 83, "Bi", 208.98, 126, 83, "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p³", 148, 703, 2.02, "9.78", 271.5, 1564, "Solid", "+3, +5", 1753),
    ("Polonium", 84, "Po", 209.0, 125, 84, "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁴", 140, 812, 2.0, 9.196, 254, 962, "Solid", "+2, +4", 1898),
    ("Astatine", 85, "At", 210.0, 125, 85, "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁵", 150, 890, 2.2, 7.0, 302, 337, "Solid", "-1, +1", 1940),
    ("Radon", 86, "Rn", 222.0, 136, 86, "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁶", 150, 1037, "N/A", 0.00973, -71, "-61.7", "Gas", "0", 1900),
    ("Francium", 87, "Fr", 223.0, 136, 87, "[Rn] 7s¹", 260, 380, 0.7, 1.87, 27, 677, "Solid", "+1", 1939),
    ("Radium", 88, "Ra", 226.0, 138, 88, "[Rn] 7s²", 221, 509, 0.9, 5.5, 700, 1737, "Solid", "+2", 1898),
    ("Actinium", 89, "Ac", 227.0, 138, 89, "[Rn] 6d¹ 7s²", 195, 499, 1.1, 10.07, 1050, 3200, "Solid", "+3", 1899),
    ("Thorium", 90, "Th", 232.04, 142, 90, "[Rn] 6d² 7s²", 179, 587, 1.3, 11.72, 1750, 4788, "Solid", "+4", 1829),
    ("Protactinium", 91, "Pa", 231.04, 140, 91, "[Rn] 5f² 6d¹ 7s²", 163, 568, 1.5, 15.37, 1568, 4027, "Solid", "+5", 1913),
    ("Uranium", 92, "U", 238.03, 146, 92, "[Rn] 5f³ 6d¹ 7s²", 156, 598, 1.38, 19.1, 1132.2, 4131, "Solid", "+6, +4", 1789),
    ("Neptunium", 93, "Np", 237.0, 144, 93, "[Rn] 5f⁴ 6d¹ 7s²", 156, 605, 1.36, 20.45, 639, 4174, "Solid", "+5, +6", 1940),
    ("Plutonium", 94, "Pu", 244.0, 150, 94, "[Rn] 5f⁶ 7s²", 159, 585, 1.28, 19.816, 639.4, 3228, "Solid", "+4, +6", 1940),
    ("Americium", 95, "Am", 243.0, 148, 95, "[Rn] 5f⁷ 7s²", 173, 578, 1.13, 12.0, 1176, 2607, "Solid", "+3, +4", 1944),
    ("Curium", 96, "Cm", 247.0, 151, 96, "[Rn] 5f⁷ 6d¹ 7s²", 174, 581, 1.28, 13.51, 1345, 3110, "Solid", "+3", 1944),
    ("Berkelium", 97, "Bk", 247.0, 150, 97, "[Rn] 5f⁹ 7s²", 170, 601, 1.3, 14.78, 986, 2627, "Solid", "+3, +4", 1949),
    ("Californium", 98, "Cf", 251.0, 153, 98, "[Rn] 5f¹⁰ 7s²", 186, 608, 1.3, 15.1, 900, 1470, "Solid", "+3", 1950),
    ("Einsteinium", 99, "Es", 252.0, 153, 99, "[Rn] 5f¹¹ 7s²", 186, 619, 1.3, 8.84, 860, "N/A", "Solid", "+3", 1952),
    ("Fermium", 100, "Fm", 257.0, 157, 100, "[Rn] 5f¹² 7s²", 198, 627, 1.3, "N/A", 1527, "N/A", "Solid", "+3", 1952),
    ("Mendelevium", 101, "Md", 258.0, 157, 101, "[Rn] 5f¹³ 7s²", 194, 635, 1.3, "N/A", 827, "N/A", "Solid", "+3, +2", 1955),
    ("Nobelium", 102, "No", 259.0, 157, 102, "[Rn] 5f¹⁴ 7s²", 197, 642, 1.3, "N/A", 827, "N/A", "Solid", "+2, +3", 1966),
    ("Lawrencium", 103, "Lr", 266.0, 163, 103, "[Rn] 5f¹⁴ 7s² 7p¹", 161, 470, 1.3, "N/A", 1627, "N/A", "Solid", "+3", 1961),
    ("Rutherfordium", 104, "Rf", 267.0, 163, 104, "[Rn] 5f¹⁴ 6d² 7s²", 150, 580, "N/A", 23.2, 2100, 5500, "Synthetic", "+4", 1969),
    ("Dubnium", 105, "Db", 268.0, 163, 105, "[Rn] 5f¹⁴ 6d³ 7s²", 139, 665, "N/A", 29.3, "N/A", "N/A", "Synthetic", "+5", 1967),
    ("Seaborgium", 106, "Sg", 269.0, 163, 106, "[Rn] 5f¹⁴ 6d⁴ 7s²", 132, 757, "N/A", 35.0, "N/A", "N/A", "Synthetic", "+6", 1974),
    ("Bohrium", 107, "Bh", 270.0, 163, 107, "[Rn] 5f¹⁴ 6d⁵ 7s²", 128, 740, "N/A", 37.1, "N/A", "N/A", "Synthetic", "+7", 1981),
    ("Hassium", 108, "Hs", 277.0, 169, 108, "[Rn] 5f¹⁴ 6d⁶ 7s²", 126, 730, "N/A", 40.7, "N/A", "N/A", "Synthetic", "+8", 1984),
    ("Meitnerium", 109, "Mt", 278.0, 169, 109, "[Rn] 5f¹⁴ 6d⁷ 7s²", 128, 800, "N/A", 37.4, "N/A", "N/A", "Synthetic", "+9, +8", 1982),
    ("Darmstadtium", 110, "Ds", 281.0, 171, 110, "[Rn] 5f¹⁴ 6d⁸ 7s²", 128, 955, "N/A", 34.8, "N/A", "N/A", "Synthetic", "+8, +6", 1994),
    ("Roentgenium", 111, "Rg", 282.0, 171, 111, "[Rn] 5f¹⁴ 6d⁹ 7s²", 121, 1020, "N/A", 28.7, "N/A", "N/A", "Synthetic", "+5, +3", 1994),
    ("Copernicium", 112, "Cn", 285.0, 173, 112, "[Rn] 5f¹⁴ 6d¹⁰ 7s²", 122, 1155, "N/A", 14.0, "N/A", 357, "Synthetic", "+2", 1996),
    ("Nihonium", 113, "Nh", 286.0, 173, 113, "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p¹", 136, 704, "N/A", 16.0, 430, 1130, "Synthetic", "+1, +3", 2004),
    ("Flerovium", 114, "Fl", 289.0, 175, 114, "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p²", 143, 823, "N/A", "9.928", 200, 380, "Synthetic", "+2, +4", 1998),
    ("Moscovium", 115, "Mc", 290.0, 175, 115, "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p³", 162, 538, "N/A", 13.5, 400, 1100, "Synthetic", "+1, +3", 2003),
    ("Livermorium", 116, "Lv", 293.0, 177, 116, "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁴", 175, 663, "N/A", 12.9, 435, 870, "Synthetic", "+2, +4", 2000),
    ("Tennessine", 117, "Ts", 294.0, 177, 117, "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁵", 165, 742, "N/A", 7.2, 450, 610, "Synthetic", "-1, +1, +3, +5", 2010),
    ("Oganesson", 118, "Og", 294.0, 176, 118, "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁶", 157, 860, "N/A", 5.0, 50, 177, "Synthetic", "0", 2002)
]
#types of elements
nm = (1, 6, 7, 8, 15, 16, 34) # reactive nonmetals
ng = (2, 10, 18, 36, 54, 86, 118) # noble gases
am = (3, 11, 19, 37, 55, 87) # alkali metals
aem = (4, 12, 20, 38, 56, 88) # alkaline earth metals
met = (5, 14, 32, 33, 51, 52, 84) # metalloids
hg = (9, 17, 35, 53, 85, 117) # halogens
post = (13, 31, 49, 50, 81, 82, 83, 113, 114, 115, 116) # post-transition metals
tm = (
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
    72, 73, 74, 75, 76, 77, 78, 79, 80,
    104, 105, 106, 107, 108, 109, 110, 111, 112
) # transition metals
lan = tuple(range(57, 72)) # lanthanides (57-71)
act = tuple(range(89, 104)) # actinides (89-103)
class state:
    table = 0
    info = 1
    list = 2
    graph = 3
    splash = 4
    select = 5
class type:
    name = 0
    atomic_number = 1
    symbol = 2
    atomic_mass = 3
    electronegativity = 4
    ionization_energy = 5
    atomic_radius = 6
    melting_point = 7
    boiling_point = 8
    density = 9
    phase_at_room_temp = 10
    year_discovered = 11
class sort_by:
    atomic_number = 0
    name = 1
    symbol = 2
    atomic_mass = 3
numbers = { #keypad keycode to number
    72: 7,
    73: 8,
    74: 9,
    82: 4,
    83: 5,
    84: 6,
    92: 1,
    93: 2,
    94: 3,
    102: 0
}
size=17
sx=6
sy=7

def boxpos(a): # why did this take so long
    if a == 1:
        return (sx, sy)
    if a == 2:
        return (sx + 17 * size, sy)

    if 3 <= a <= 4:
        return (sx + (a - 3) * size, sy + size)
    if 5 <= a <= 10:
        return (sx + (a + 7) * size, sy + size)

    if 11 <= a <= 12:
        return (sx + (a - 11) * size, sy + 2 * size)
    if 13 <= a <= 18:
        return (sx + (a - 1) * size, sy + 2 * size)

    if 19 <= a <= 36:
        return (sx + (a - 19) * size, sy + 3 * size)

    if 37 <= a <= 54:
        return (sx + (a - 37) * size, sy + 4 * size)

    if 55 <= a <= 56:
        return (sx + (a - 55) * size, sy + 5 * size)
    if 72 <= a <= 86:
        return (sx + (a - 69) * size, sy + 5 * size)
        
    if 87 <= a <= 88:
        return (sx + (a - 87) * size, sy + 6 * size)
    if 104 <= a <= 118:
        return (sx + (a - 101) * size, sy + 6 * size)
        

    gap = size // 2
    if 57 <= a <= 71 :
        return (sx + (a - 54) * size, sy + 7 * size + gap)
    if 89 <= a <= 103:
        return (sx + (a - 86) * size, sy + 8 * size + gap)
        
    

    return (sx, sy)

def draw_box(a, selected=False): #finally putting abstraction to use lol
    pos = boxpos(a)
    x, y = pos[0], pos[1]

    get_color(a)
    fill_rect(x, y, size, size)

    if selected:
        set_color(0, 0, 0)
        draw_rect(x, y, size, size)
        draw_rect(x + 1, y + 1, size - 2, size - 2)
    else:
        set_color(85, 85, 85)
        draw_rect(x, y, size, size)

def get_color(a): #had to use some dumb screenshot from the calculator as ref
    if a in nm:
        set_color(0, 240, 0)
    elif a in hg:
        set_color(0, 222, 191)
    elif a in ng:
        set_color(143, 170, 255)
    elif a in am:
        set_color(255,171,0)
    elif a in aem:
        set_color(255,255,0)
    elif a in met:
        set_color(83, 207, 144)
    elif a in post:
        set_color(161, 188, 175)
    elif a in tm:
        set_color(224, 156, 160)
    elif a in lan:
        set_color(255, 171, 144)
    elif a in act:
        set_color(224, 171, 207)
    else:
        set_color(240, 240, 240)
    
def replace_selection(prev, new):
    global selectable #screw you, python
    draw_box(prev, selected=False)
    clear_rect(40, 0, 160, 55)
    clear_rect(40, 0, 250, 24)
    draw_box(new, selected=True)
    try:
        draw_text(75, 25, str(E[new][0]))
        draw_text(160, 50, str(E[new][1]))
        draw_text(75, 50, str(E[new][2]))
        selectable = True
    except IndexError:
        draw_text(75, 25, "N/A")
        draw_text(75, 50, "N/A")
        draw_text(160, 50, "N/A")
        selectable = False
def drawSoftkey(size, pos, text):
    width = size * 62 + (size - 1)
    x = (pos - 1) * 62 + 5 #crunch them numbers
    set_pen("medium","solid")
    draw_rect(x, 210-20, width, 40)
    draw_text(x+5, 212, str(text))
    set_pen("thin","solid")
def draw_table():
    for i in range(1, 119): # i forgor how many elements there are, thanks google
        draw_box(i, selected=(i == selected))
    #fork looking thing from the CE
    draw_rect(48,100, 1, 60)
    draw_rect(48, 160, 8, 1)
    draw_rect(48, 143, 8, 1)
def draw_splash():
    set_color(0, 0, 0)
    draw_text(100, 100, "Periodic Table")
    setFont(4)
    draw_text(160, 120, "V7.0.0.3996")
    draw_text(110, 200, "PRESS ANY KEY")
    draw_text(114, 213, "©2026 CrX1x1")
    setFont(2)
def draw_text_row(y, align, text, is_selected=None, height=18): 
    align = str(align)
    if align=="middle":
        text_x=160-(6*len(text))
    elif align.isdigit():
        text_x = int(align)
    else:
        text_x=160-(str(text).index(align)+1)*12
    if is_selected:
        set_color(0,0,0)
    else:
        set_color(255,255,255)
    if is_selected is not None:
        fill_rect(text_x-2,y-(height+1),len(text)*12+3,height+1)
    if is_selected:
        set_color(255,255,255)
    else:
        set_color(0,0,0)
    draw_text(text_x,y,text)
    set_color(0,0,0)
#a useless function was here
def draw_list(start, end, selected): # more AI polishing lol
    if start > end or selected < start or selected > end or start < 1 or end > 118:
        raise ValueError("Invalid range or selected index, selected=%d, start=%d, end=%d" % (selected, start, end))
    
    
    for i in range(start, end + 1):
        y_pos = 22 + (i - start) * 20
        
        if i == selected:
            set_color(0, 0, 0)
            if alpha:
                #set color to green for alpha lol
                set_color(0, 158, 0)
            fill_rect(10, y_pos -18, 300, 22)
            set_color(255, 255, 255)
        else:
            set_color(255, 255, 255)
            fill_rect(10, y_pos -18, 300, 22)
            set_color(0, 0, 0)

        if current_sort == sort_by.atomic_number:
            draw_text(25, y_pos, str(E[i][1])) # atomic number
            draw_text(65, y_pos, E[i][0])       # element name
            draw_text(280, y_pos, E[i][2])      # element symbol
        elif current_sort == sort_by.name:
            draw_text(20, y_pos, E[i][0])       # element name
            draw_text(225, y_pos, str(E[i][1])) # atomic number
            draw_text(280, y_pos, E[i][2])      # element symbol
        elif current_sort == sort_by.symbol:
            draw_text(20, y_pos, E[i][2])      # element symbol
            draw_text(65, y_pos, E[i][0])       # element name
            draw_text(280, y_pos, str(E[i][1])) # atomic number
def sort_elements(sort_by):
    global E, current_sort
    current_sort = sort_by

    # right, i forgot about the empty tuple i put, thanks AI
    if sort_by == 0:  # Sort by atomic number
        E = [E[0]] + sorted(E[1:], key=lambda x: int(x[1]))
    elif sort_by == 1:  # Sort by name
        E = [E[0]] + sorted(E[1:], key=lambda x: x[0])
    elif sort_by == 2:  # Sort by symbol
        E = [E[0]] + sorted(E[1:], key=lambda x: x[2])
        


prev_selected = 0
selected = 1
current_state = state.splash
setFont(2)
stuff_drawn = False
prev_list_pos = 0
list_pos = 0
selectable = True
current_sort = sort_by.atomic_number
jmp_str = ""
items = 9
title = ""
options = []
menu_selected = 0
return_to = state.table
callback = None # eh, just in case
alpha = False
while True:
    key = getKey(0)
    if key == 31:
        alpha = not alpha
        stuff_drawn = False
    if current_state == state.splash:
        if not stuff_drawn:
            #draw static text, of course
            draw_splash()
            stuff_drawn = True
        # animation that i made on-calculator when i got bored
        cx = 40
        cy = 90
        orbit_rad = 30
        electron_rad = 3

        set_color(255, 0, 0)
        fill_circle(cx, cy, 5)  # draw the singular proton in the center

        # plus sign
        set_color(255, 255, 255)
        draw_line(cx-2, cy, cx+2, cy)
        draw_line(cx, cy-2, cx, cy+2)

        # draw the electron orbit
        set_color(100, 100, 100)
        draw_circle(cx, cy, orbit_rad)

        #previous pos
        prev_ex = cx + orbit_rad
        prev_ey = cy

        while True:
            for deg in range(0, 360, 5):
                key = getKey(0)
                if key != 0:
                    break
                angle = radians(deg)
                ex = cx + orbit_rad * cos(angle)
                ey = cy + orbit_rad * sin(angle)
                clear_rect(prev_ex - electron_rad, prev_ey - electron_rad - 1, (electron_rad * 2) + 2, (electron_rad * 2) + 2)
                set_color(100, 100, 100)
                draw_circle(cx, cy, orbit_rad)
                set_color(0, 0, 255)
                fill_circle(ex, ey, electron_rad)
                prev_ex, prev_ey = ex, ey
            if key != 0:
                stuff_drawn = False
                break
        clear()
        key = 0
        current_state = state.table
    if current_state == state.table:
        if not stuff_drawn:
            draw_table()
            replace_selection(prev_selected, selected)
            drawSoftkey(2, 1, "OPTIONS")
            drawSoftkey(1, 3, "LIST")
            drawSoftkey(1, 4, "INFO")
            drawSoftkey(1, 5, "QUIT")
            stuff_drawn = True
        if key == 0:
            continue
        if key == 24: #left
            if selected == 1:
                continue
            prev_selected = selected
            selected -= 1
            replace_selection(prev_selected, selected)
        if key == 26: #right
            if selected == 118:
                continue
            prev_selected = selected
            selected += 1
            replace_selection(prev_selected, selected)
        if key == 25: #up, save my sanity
            if selected in (1, 2, 4, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 5, 6, 7, 8, 9):
                continue
            prev_selected = selected
            if selected == 3:
                selected = 1
            elif selected == 10:
                selected = 2
            elif 11 <= selected <= 20:
                selected -= 8
            elif 31 <= selected <= 56:
                selected -= 18
            elif 57 <= selected <= 71:
                selected += 47
            elif 72 <= selected <= 118:
                selected -= 32    
            replace_selection(prev_selected, selected)
            continue
        if key == 34: #down
            if 87 <= selected <= 103 or selected == 39:
                continue
            prev_selected = selected
            if selected == 1:
                selected = 3
            elif selected == 2:
                selected = 10
            elif 3 <= selected <= 12:
                selected += 8
            elif 13 <= selected <= 38:
                selected += 18
            elif 40 <= selected <= 86:
                selected += 32
            elif 104 <= selected <= 118:  
                selected -= 47
            replace_selection(prev_selected, selected)
            continue
        if key in (11, 12): # y= and window
            #todo
            pass
        if key == 13: # zoom
            # go to the list
            clear()
            current_state = state.list
            if selected > len(E) - items:
                list_start = len(E) - items
            else:
                list_start = selected
            current_sort = sort_by.atomic_number
            stuff_drawn = False
            key = 0
        if key == 14: # trace
            #splash screen
            clear()
            current_state = state.splash
            stuff_drawn = False
        if key == 15: # graph
            #quit
            break
        if key == 105:
            #enter
            if selectable:
                clear()
                current_state = state.info
                stuff_drawn = False
            else:
                #todo, make a "not selectable" message
                pass
    if current_state == state.info:
        charsize = 12 #measurement of how many pixels a character takes up horizontally, will do later, placeholder
        if not stuff_drawn:
            drawSoftkey(1, 1, "SET")
            drawSoftkey(1, 2, "HELP")
            drawSoftkey(1, 3, "LIST")
            drawSoftkey(1, 4, "TBL")
            drawSoftkey(1, 5, "QUIT")
            set_pen("thin","solid")
            
            get_color(selected)
            fill_rect(6, 4, 308, 30)
            set_color(0, 0, 0)
            draw_rect(6, 38, 308, 145)
            draw_rect(6, 4, 308, 30)
            draw_text(160 - (len(str(E[selected][0])) * charsize // 2), 26, str(E[selected][0]))
            stuff_drawn = True
            text_drawn = False
        if not text_drawn:
            if list_pos in range(0, 6):
                draw_text_row(60, ":", "ATOMIC #: "+str(E[selected][1]), list_pos == 0)
                draw_text_row(80, ":", "SYMBOL: "+str(E[selected][2]), list_pos == 1)
                draw_text_row(100, ":", "WEIGHT: "+str(E[selected][3]), list_pos == 2)
                draw_text_row(120, ":", "NEUTRONS: "+str(E[selected][4]), list_pos == 3)
                draw_text_row(140, ":", "PROTONS: "+str(E[selected][5]), list_pos == 4)
                draw_text_row(170, "middle", str(E[selected][6]), list_pos == 5, 20)
            if list_pos in range(6,12):
                draw_text_row(60, ":", "RADIUS: "+str(E[selected][7]), list_pos == 6)
                draw_text_row(80, ":", "1ST IONIZE: "+str(E[selected][8]), list_pos == 7)
                draw_text_row(100, ":", "ELECTRONEG: "+str(E[selected][9]), list_pos == 8)
                draw_text_row(120, ":", "DENSITY: "+str(E[selected][10]), list_pos == 9)
                draw_text_row(140, ":", "MELTING PT: "+str(E[selected][11]), list_pos == 10)
                draw_text_row(160, ":", "BOILING PT: "+str(E[selected][12]), list_pos == 11)
            if list_pos in range(12,15):
                draw_text_row(60, ":", "STATE: "+str(E[selected][13]), list_pos == 12)
                draw_text_row(80, ":", "OX STATES: "+str(E[selected][14]), list_pos == 13)
                draw_text_row(100, ":", "DISCOVERED: "+str(E[selected][15]), list_pos == 14)
            text_drawn = True
        if key == 25:# up
            if list_pos == 0:
                continue
            if list_pos in (6,12):
                 clear_rect(6, 38, 308, 145)
            prev_list_pos = list_pos
            list_pos -= 1
            text_drawn = False
        if key == 34:# down
            if list_pos == 14:
                continue
            if list_pos in (5,11):
                clear_rect(6, 38, 308, 145)
            
            prev_list_pos = list_pos
            list_pos += 1
            text_drawn = False
        if key == 24: #left
            if selected == 1:
                continue
            prev_selected = selected
            selected -= 1
            stuff_drawn = False
            text_drawn = False
            clear_rect(6, 38, 308, 145)
        if key == 26:
            if selected == (len(E)-1):
                continue
            prev_selected = selected
            selected += 1
            stuff_drawn = False
            text_drawn = False
            clear_rect(6, 38, 308, 145)
        if key == 15:
             break
        if key == 14:
            text_drawn = False
            stuff_drawn = False
            clear()
            current_state = state.table
        if key == 13:
            text_drawn = False
            stuff_drawn = False
            clear()
            if selected > len(E) - items:
                list_start = len(E) - items
            else:
                list_start = selected
            current_sort = sort_by.atomic_number
            current_state = state.list
            key = 0
    if current_state == state.list:# ai polished, it failed, and then i ended up doing debugging and patching myself lol
        
        if 'list_start' not in globals():
            list_start = 1
            
        if not stuff_drawn:
            if menu_selected is not None:
                if menu_selected == 0:
                    sort_elements(sort_by.atomic_number)
                elif menu_selected == 1:
                    sort_elements(sort_by.name)
                elif menu_selected == 2:
                    sort_elements(sort_by.symbol)
                menu_selected = -1
            draw_list(list_start, min(list_start + items - 1, len(E) - 1), selected)
            set_color(0, 0, 0)
            if current_sort == sort_by.atomic_number:
                drawSoftkey(2, 1, "RESET") 
            drawSoftkey(1, 3, "SORT")
            drawSoftkey(1, 4, "TBL")
            drawSoftkey(1, 5, "QUIT")
            set_pen("thin","solid")
            set_color(0, 0, 0)
            draw_rect(5, 3, 310, 184)
            stuff_drawn = True
        
        if key == 25: # up
            if selected > 1:
                if alpha:
                    alpha = False
                    selected -= 10
                    selected = max(selected, 1)
                else:
                    selected -= 1
                if selected < list_start:
                    list_start = selected
                stuff_drawn = False
                
        elif key == 34: # down
            if selected < len(E) - 1:
                if alpha:
                    alpha = False
                    selected += 10
                    selected = min(selected, len(E) - 1)
                else:
                    selected += 1
                if selected >= list_start + items:
                    list_start = selected - items + 1
                stuff_drawn = False
                
        elif key in (11, 12) and current_sort == sort_by.atomic_number:
            selected = 1
            list_start = 1
            jmp_str = ""
            prev_jmp_str = ""
            stuff_drawn = False
            clear()
            
        elif key == 14:
            stuff_drawn = False
            clear()
            current_state = state.table
            
        elif key == 15:
            break
        elif key == 13:
            # select sort
            return_to = current_state
            current_state = state.select
            options = ["ATOMIC NUMBER", "NAME", "SYMBOL"]
            title = "SORT ELEMENTS BY:"
            stuff_drawn = False
            clear()
        elif key == 105: #enter, go to info panel
            clear()
            current_state = state.info
            stuff_drawn = False
        elif key in numbers:
            if current_sort == sort_by.atomic_number:
                prev_jmp_str = jmp_str
                jmp_str += str(numbers[key])
                if jmp_str == "0":
                    jmp_str = prev_jmp_str
                elif 1 <= int(jmp_str) <= len(E) - 1:
                    selected = int(jmp_str)
                    list_start = min(selected, len(E) - items)
                    stuff_drawn = False
                else:
                    jmp_str = prev_jmp_str
    if current_state == state.select:
        if menu_selected == -1:
            menu_selected = 0
        if not stuff_drawn:
            set_color(0, 0, 0)
            draw_rect(5, 3, 310, 30)
            set_color(200,200,255) # blue color instead
            fill_rect(5, 3, 310, 30)
            draw_text_row(30, "middle", title)
            # draw the options list below the title
            for i, option in enumerate(options):
                draw_text_row(60 + i * 22, 30, "%s:%s"%(i+1, option), is_selected=(i == menu_selected))
            drawSoftkey(1,1,"OK")
            drawSoftkey(1,5,"ESC")
            stuff_drawn = True
            
        if key == 25: # up
            if menu_selected > 0:
                menu_selected -= 1
                stuff_drawn = False
        elif key == 34: # down
            if menu_selected < len(options) - 1:
                menu_selected += 1
                stuff_drawn = False
        elif key in (105, 11): # enter
            # handle the selection of the current option
            selected_option = options[menu_selected]
            stuff_drawn = False
            current_state = return_to
            clear()
        elif key == 15:
            current_state = return_to
            stuff_drawn = False
            clear()

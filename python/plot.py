import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize


def autolabel(rects, yerr=[0, 0, 0]):
    """
    Attach a text label above each bar in *rects*, displaying its height.
    Source:
    https://matplotlib.org/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
    """
    for i, rect in enumerate(rects):
        height = rect.get_height()
        plt.annotate(r'${} \pm {} \mu s$'.format(height, yerr[i]),
                     xy=(rect.get_x() + rect.get_width() / 2,
                         height + yerr[i]),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom')


def jan_31_benchmarking():
    ''' Old-style benchmarking '''
    # Addition
    labels = ['numpy', 'tensors', 'math.matrices']
    data = [70, 245, 1750]
    rects = plt.bar(x=range(len(data)), height=data, tick_label=labels)
    autolabel(rects)

    plt.title('Add Two 100k Element Arrays')
    plt.xlabel('Library / Vocabulary')
    plt.ylabel('Time (us)')
    plt.ylim(top=max(data) * 1.1)
    plt.show()

    # Matrix multiplication
    data = [520, 2712,  12940]
    rects = plt.bar(x=range(len(data)), height=data, tick_label=labels)
    autolabel(rects)

    plt.title('Multiply Two 100x100 Element Arrays')
    plt.xlabel('Library / Vocabulary')
    plt.ylabel('Time (us)')
    plt.ylim(top=max(data) * 1.1)
    plt.show()

    # Matrix transposition
    data = [1, 711, 17]
    rects = plt.bar(x=range(len(data)), height=data, tick_label=labels)
    autolabel(rects)

    plt.title('Transpose a 100x100 Element Array')
    plt.xlabel('Library / Vocabulary')
    plt.ylabel('Time (us)')
    plt.ylim(top=max(data) * 1.1)
    plt.show()


def sin_func(x, a, b, c):
    return a * np.sin(b * x) + c


def feb_6_benchmarking():
    ''' Test out impact on garbage collection '''
    x_data = np.arange(30) + 1
    no_gc = [3051476, 3012790, 3221173, 2956580, 2596003, 2594998, 2663338,
             2825727, 3076740, 3045100, 2598003, 2592870, 2655172, 2628627,
             3096976, 2923263, 2596609, 2595064, 2592968, 2663469, 3107040,
             2911755, 2611512, 2600538, 2596673, 2623847, 3037184, 2970033,
             2597872, 2834640]

    with_gc_1 = [2617837, 2611595, 2606830, 2608464, 2605527, 2609590, 2610261,
                 2604330, 2603769, 2613516, 2609546, 2607349, 2639476, 2688193,
                 2608280, 2607027, 2606865, 2605624, 2606139, 2606522, 2613550,
                 2702453, 2777699, 2621044, 2780597, 3222790, 2624013, 2751122,
                 2735148, 2608397]

    with_gc_2 = [2621413, 2981441, 2608684, 2610563, 2610649, 2778801, 2606172,
                 2982184, 2690104, 3157840, 2747703, 3402213, 2653121, 2626381,
                 2818332, 2608261, 2608932, 2666946, 2650281, 2665784, 2644083,
                 2606865, 3470364, 2746330, 3150380, 2967961, 3233225, 2645445,
                 2762184, 2607818]

    with_gc_3 = [2639847, 2604862, 2606640, 2620360, 2614161, 2610362, 2603735,
                 2606903, 2606014, 2602061, 2601360, 2604599, 2605980, 2626606,
                 2606829, 2608719, 2608126, 2606388, 2606995, 2609233, 2605232,
                 3966425, 2603957, 4205922, 2607591, 2608634, 2608074, 2640602,
                 2605698, 2604836]

    no_gc = np.array(no_gc) / 1000000
    with_gc_1 = np.array(with_gc_1) / 1000000
    with_gc_2 = np.array(with_gc_2) / 1000000
    with_gc_3 = np.array(with_gc_3) / 1000000

    params, params_covariance = optimize.curve_fit(sin_func, x_data, no_gc,
                                                   p0=[2.5, 1,
                                                       3])

    # 100 linearly spaced numbers
    x = np.linspace(1, 30, 1000)

    # the function, which is y = sin(x) here
    y = params[0] * np.sin(params[1] * x) + params[2]

    plt.plot(x_data, no_gc, 'o')
    plt.plot(x, y, 'r')
    plt.ylim(bottom=0, top=max(with_gc_3) * 1.1)
    plt.title('Multiply 100x100 Element Arrays - No Manual Garbage Collection')
    plt.xlabel('Trial')
    plt.ylabel('Time (ms)')
    plt.show()

    plt.plot(x_data, with_gc_1, 'bo')
    plt.plot(x_data, with_gc_2, 'ro')
    plt.plot(x_data, with_gc_3, 'yo')
    plt.ylim(bottom=0, top=max(with_gc_3) * 1.1)
    plt.title('Multiply 100x100 Element Arrays - ' +
              'Garbage Collection Before Each Call')
    plt.xlabel('Trial')
    plt.ylabel('Time (ms)')
    plt.show()


def feb_7_benchmarking():
    ''' Get new data with error bars! '''
    # Data
    labels = ['numpy', 'tensors', 'math.matrices']

    t_add = [232775, 233971, 238884, 234146, 232840, 233810, 233405, 233327,
             233906, 234152, 233346, 234006, 233543, 233427, 233350, 465950,
             333094, 233014, 233235, 233890, 233731, 233844, 438358, 233524,
             233155, 233736, 242376, 407495, 233487, 233839]

    t_matmul = [2617837, 2611595, 2606830, 2608464, 2605527, 2609590, 2610261,
                2604330, 2603769, 2613516, 2609546, 2607349, 2639476, 2688193,
                2608280, 2607027, 2606865, 2605624, 2606139, 2606522, 2613550,
                2702453, 2777699, 2621044, 2780597, 3222790, 2624013, 2751122,
                2735148, 2608397]

    t_transpose = [716122, 674089, 674374, 815392, 676803, 674842, 674986,
                   1024099, 676151, 675658, 676115, 675929, 675221, 683359,
                   674791, 676264, 674884, 676456, 677638, 676185, 676306,
                   725239, 676136, 675901, 675267, 675439, 667354, 675536,
                   678058, 675983]

    m_add = [1691864, 1599821, 1598871, 1942485, 1600183, 1599695, 1600104,
             1600225, 1602987, 1602682, 1748842, 1602618, 1600055, 1598157,
             1599273, 1599229, 1598888, 1599548, 1599433, 1599919, 1599078,
             1643490, 1615201, 1599872, 1602648, 1602997, 1600216, 1605647,
             1600218, 1605608]

    m_matmul = [12793339, 12916947, 12708402, 12020015, 17699378, 13158661,
                12458662, 12572522, 12642106, 12227820, 12351928, 12691935,
                11983044, 12264951, 13126555, 12012390, 11989681, 11981440,
                12264752, 12181297, 11988687, 12151452, 11984948, 11983809,
                12014014, 12000078, 11983570, 11984604, 12008697, 12058735]

    m_transpose = [45027, 40395, 40903, 40261, 41078, 32493, 33292, 32839,
                   32961, 44587, 35342, 43048, 33310, 32899, 31907, 31587,
                   37562, 53351, 49319, 34559, 58005, 60013, 35701, 34562,
                   54455, 33620, 33274, 54990, 33365, 33481]

    n_add = [217752, 32303, 28000, 27305, 27191, 26829, 27059, 26998, 26963,
             26826, 26743, 26908, 27007, 27013, 26909, 26701, 26825, 26877,
             26814, 45463, 28317, 26886, 26967, 27006, 27272, 27080, 26938,
             26895, 26993, 26817]

    n_matmul = [92264, 78767, 78090, 77407, 77673, 77711, 77273, 77419, 77476,
                77040, 77709, 77264, 77439, 77093, 77527, 77067, 102330,
                105591, 78485, 77942, 77753, 77594, 77834, 110632, 127869,
                122631, 111515, 97618, 96761, 134954]

    n_transpose = [29544, 8322, 8643, 7123, 5621, 10100, 7538, 2405, 8511,
                   6325, 5595, 5763, 5949, 5052, 3751, 7484, 6278, 8053, 6425,
                   5583, 4306, 6670, 15612, 12063, 13421, 4860, 2481, 2354,
                   8874, 6577]

    # Cast to numpy array
    t_add = np.array(t_add) / 1000
    t_matmul = np.array(t_matmul) / 1000
    t_transpose = np.array(t_transpose) / 1000
    m_add = np.array(m_add) / 1000
    m_matmul = np.array(m_matmul) / 1000
    m_transpose = np.array(m_transpose) / 1000
    n_add = np.array(n_add) / 1000
    n_matmul = np.array(n_matmul) / 1000
    n_transpose = np.array(n_transpose) / 1000

    # Addition
    add_means = np.array([np.mean(n_add), np.mean(t_add), np.mean(m_add)])
    add_stds = np.array([np.std(n_add), np.std(t_add), np.std(m_add)])
    add_means = add_means.astype(int)
    add_stds = add_stds.astype(int)

    rects = plt.bar(x=range(len(add_means)),
                    height=add_means, tick_label=labels, yerr=add_stds)
    autolabel(rects, add_stds)

    plt.title('Add Two 100k Element Arrays')
    plt.xlabel('Library / Vocabulary')
    plt.ylabel(r'Time ($\mu s$)')
    plt.ylim(top=max(add_means) * 1.2)
    plt.show()

    # Multiplication
    matmul_means = np.array(
        [np.mean(n_matmul), np.mean(t_matmul), np.mean(m_matmul)])
    matmul_stds = np.array(
        [np.std(n_matmul), np.std(t_matmul), np.std(m_matmul)])
    matmul_means = matmul_means.astype(int)
    matmul_stds = matmul_stds.astype(int)

    rects = plt.bar(x=range(len(matmul_means)),
                    height=matmul_means, tick_label=labels, yerr=matmul_stds)
    autolabel(rects, matmul_stds)

    plt.title('Multiply Two 100x100 Element Arrays')
    plt.xlabel('Library / Vocabulary')
    plt.ylabel(r'Time ($\mu s$)')
    plt.ylim(top=max(matmul_means) * 1.2)
    plt.show()

    # Transpose
    transpose_means = np.array([np.mean(n_transpose), np.mean(t_transpose),
                                np.mean(m_transpose)])
    transpose_stds = np.array([np.std(n_transpose), np.std(t_transpose),
                               np.std(m_transpose)])
    transpose_means = transpose_means.astype(int)
    transpose_stds = transpose_stds.astype(int)

    rects = plt.bar(x=range(len(transpose_means)), height=transpose_means,
                    tick_label=labels, yerr=transpose_stds)
    autolabel(rects, transpose_stds)

    plt.title('Transpose a 100x100 Element Array')
    plt.xlabel('Library / Vocabulary')
    plt.ylabel(r'Time ($\mu s$)')
    plt.ylim(top=max(transpose_means) * 1.2)
    plt.show()


def main():
    feb_7_benchmarking()


if __name__ == '__main__':
    main()

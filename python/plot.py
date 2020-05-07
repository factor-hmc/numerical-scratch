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
        plt.annotate(r'${} \pm {} ms$'.format(height, yerr[i]),
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


def feb_9_benchmarking():
    labels = ['Vanilla', 'SIMD']

    # This is the original style (pre Feb 9)
    style1 = [232775, 233971, 238884, 234146, 232840, 233810, 233405, 233327,
              233906, 234152, 233346, 234006, 233543, 233427, 233350, 465950,
              333094, 233014, 233235, 233890, 233731, 233844, 438358, 233524,
              233155, 233736, 242376, 407495, 233487, 233839]

    # This uses direct c-arrays to remove the need for the start index
    style2 = [66483780, 66683132, 69067172, 66682335, 66594571, 74668551,
              68403923, 72544333, 77259163, 72649789, 80057730, 77465377,
              71717455, 70713860, 66458389, 76328519, 67034759, 66583162,
              74852873, 67369030, 67669800, 71062850, 72701049, 74014725,
              72806532, 72125823, 68055052, 66601896, 66368918, 70324875]

    style1 = np.array(style1) / 1000
    style2 = np.array(style2) / 1000

    means = np.array([np.mean(style1), np.mean(style2)]).astype(int)
    stds = np.array([np.std(style1), np.std(style2)]).astype(int)

    rects = plt.bar(x=range(len(means)),
                    height=means, tick_label=labels, yerr=stds)
    autolabel(rects, stds)

    plt.title('Add Two 100k Element Arrays')
    plt.xlabel('Implementation')
    plt.ylabel(r'Time ($\mu s$)')
    plt.ylim(top=max(means) * 1.2)
    plt.show()


def feb_16_benchmarking():
    ''' Get new data with error bars! '''
    # Data
    labels = ['numpy', 'tensors', 'math.matrices']

    t_add = [63681, 63288, 63156, 62894, 63409, 62826, 62371, 63361, 63256,
             62534, 62782, 62226, 62588, 62596, 61998, 63207, 62774, 62699,
             62766, 62048, 62263, 61411, 62197, 63065, 62508, 62525, 62696,
             65891, 63027, 63380]

    t_matmul_100 = [3002769, 2984803, 2950593, 3011281, 2953131, 2944961,
                    2944361, 2943872, 3001597, 2946397, 2945814, 2942405,
                    3003859, 2948559, 2948898, 2954622, 2943404, 3001759,
                    2945933, 2944373, 2953515, 2946785, 2965791, 2952813,
                    2948738, 2952322, 3024136, 3007285, 2951595, 2952803]

    t_matmul_1000 = [828471191, 828542608, 828215059, 828350049, 828402132,
                     828444191, 828874698, 828257704, 828175629, 828508119,
                     828716529, 828558659, 828681679, 828611721, 828314668,
                     830106572, 828340455, 829212792, 828619871, 828368351,
                     828284582, 828251697, 828450318, 828555590, 828497724,
                     828416184, 828292992, 828299557, 827493214, 826025658]

    t_transpose = [365223, 391824, 364729, 365248, 364908, 364684, 365874,
                   365293, 364960, 399805, 363790, 364685, 365010, 364643,
                   364159, 363822, 364310, 363979, 364366, 364232, 364455,
                   365596, 365228, 391863, 364143, 364504, 364809, 364425,
                   364873, 364772]

    m_add = [1691864, 1599821, 1598871, 1942485, 1600183, 1599695, 1600104,
             1600225, 1602987, 1602682, 1748842, 1602618, 1600055, 1598157,
             1599273, 1599229, 1598888, 1599548, 1599433, 1599919, 1599078,
             1643490, 1615201, 1599872, 1602648, 1602997, 1600216, 1605647,
             1600218, 1605608]

    m_matmul_100 = [12793339, 12916947, 12708402, 12020015, 17699378, 13158661,
                    12458662, 12572522, 12642106, 12227820, 12351928, 12691935,
                    11983044, 12264951, 13126555, 12012390, 11989681, 11981440,
                    12264752, 12181297, 11988687, 12151452, 11984948, 11983809,
                    12014014, 12000078, 11983570, 11984604, 12008697, 12058735]

    m_matmul_1000 = [12009185570, 12005449930, 11995872204, 12003169018,
                     12007385020, 12006812793, 12000051183, 12000365153,
                     12003577782, 12002088065, 12008996042, 12003862467,
                     12004734996, 12001978593, 12009429195, 11998935872,
                     12006691997, 11998822899, 11999439487, 12003708258,
                     12000928868, 11999506197, 12001008652, 12004392101,
                     12011651314, 12008158167, 12005144807, 12006991958,
                     12053428100, 12040745924]

    m_transpose = [45027, 40395, 40903, 40261, 41078, 32493, 33292, 32839,
                   32961, 44587, 35342, 43048, 33310, 32899, 31907, 31587,
                   37562, 53351, 49319, 34559, 58005, 60013, 35701, 34562,
                   54455, 33620, 33274, 54990, 33365, 33481]

    n_add = [217752, 32303, 28000, 27305, 27191, 26829, 27059, 26998, 26963,
             26826, 26743, 26908, 27007, 27013, 26909, 26701, 26825, 26877,
             26814, 45463, 28317, 26886, 26967, 27006, 27272, 27080, 26938,
             26895, 26993, 26817]

    n_matmul_100 = [92264, 78767, 78090, 77407, 77673, 77711, 77273, 77419,
                    77476, 77040, 77709, 77264, 77439, 77093, 77527, 77067,
                    102330, 105591, 78485, 77942, 77753, 77594, 77834, 110632,
                    127869, 122631, 111515, 97618, 96761, 134954]

    n_matmul_1000 = [21238433, 16619649, 15162618, 13439006, 13294785,
                     11686406, 12516240, 11604115, 12330164, 11733975,
                     11786885, 15973550, 12076515, 12173215, 12575362,
                     11628379, 11469076, 11504058, 12205348, 11596335,
                     11644163, 11846563, 11546053, 11729519, 11519261,
                     11833941, 11790333, 11542091, 15344395, 15420503]

    n_transpose = [29544, 8322, 8643, 7123, 5621, 10100, 7538, 2405, 8511,
                   6325, 5595, 5763, 5949, 5052, 3751, 7484, 6278, 8053, 6425,
                   5583, 4306, 6670, 15612, 12063, 13421, 4860, 2481, 2354,
                   8874, 6577]

    # Cast to numpy array
    t_add = np.array(t_add) / 1000
    t_matmul_100 = np.array(t_matmul_100) / 1000
    t_matmul_1000 = np.array(t_matmul_1000) / 1000
    t_transpose = np.array(t_transpose) / 1000
    m_add = np.array(m_add) / 1000
    m_matmul_100 = np.array(m_matmul_100) / 1000
    m_matmul_1000 = np.array(m_matmul_1000) / 1000
    m_transpose = np.array(m_transpose) / 1000
    n_add = np.array(n_add) / 1000
    n_matmul_100 = np.array(n_matmul_100) / 1000
    n_matmul_1000 = np.array(n_matmul_1000) / 1000
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
    matmul_100_means = np.array(
        [np.mean(n_matmul_100), np.mean(t_matmul_100), np.mean(m_matmul_100)])
    matmul_100_stds = np.array(
        [np.std(n_matmul_100), np.std(t_matmul_100), np.std(m_matmul_100)])
    matmul_100_means = matmul_100_means.astype(int)
    matmul_100_stds = matmul_100_stds.astype(int)

    rects = plt.bar(x=range(len(matmul_100_means)),
                    height=matmul_100_means, tick_label=labels,
                    yerr=matmul_100_stds)
    autolabel(rects, matmul_100_stds)

    plt.title('Multiply Two 100x100 Element Arrays')
    plt.xlabel('Library / Vocabulary')
    plt.ylabel(r'Time ($\mu s$)')
    plt.ylim(top=max(matmul_100_means) * 1.2)
    plt.show()

    matmul_1000_means = np.array(
        [np.mean(n_matmul_1000), np.mean(t_matmul_1000),
         np.mean(m_matmul_1000)])
    matmul_1000_stds = np.array(
        [np.std(n_matmul_1000), np.std(t_matmul_1000), np.std(m_matmul_1000)])
    matmul_1000_means = matmul_1000_means.astype(int)
    matmul_1000_stds = matmul_1000_stds.astype(int)

    rects = plt.bar(x=range(len(matmul_1000_means)),
                    height=matmul_1000_means, tick_label=labels,
                    yerr=matmul_1000_stds)
    autolabel(rects, matmul_1000_stds)

    plt.title('Multiply Two 1000x1000 Element Arrays')
    plt.xlabel('Library / Vocabulary')
    plt.ylabel(r'Time ($\mu s$)')
    plt.ylim(top=max(matmul_1000_means) * 1.2)
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

    # Transpose
    plt.title('Transpose a 100x100 Element Array')
    plt.xlabel('Library / Vocabulary')
    plt.ylabel(r'Time ($\mu s$)')
    plt.ylim(top=max(transpose_means) * 1.2)
    plt.show()


def mar_1_benchmarking():
    ''' Get new data with error bars! '''
    # Data
    labels = ['numpy', 'tensors', 'math.matrices']

    t_add = [63970, 62085, 62258, 61726, 61483, 62798, 62497, 62761, 62237,
             62517, 62943, 61776, 61881, 62771, 63717, 61765, 61322, 62594,
             62534, 62289, 62119, 61652, 61976, 62089, 61728, 76393, 62586,
             62955, 62568, 62476]

    t_matmul_100 = [1397581, 1394946, 1394267, 1401410, 1396694, 1401705,
                    1396754, 1396920, 1395966, 1396826, 1403299, 1396574,
                    1430449, 1456683, 1456869, 1422450, 1394665, 1395173,
                    1396041, 1395650, 1431402, 1395295, 1395692, 1394470,
                    1395751, 1396224, 1394189, 1395574, 1395748, 1396061]

    t_transpose = [366146, 364938, 364946, 363461, 364459, 363904, 365564,
                   364866, 365190, 365475, 364822, 365273, 364625, 364899,
                   365005, 364627, 368948, 366356, 395654, 365746, 364985,
                   365164, 365103, 364774, 365750, 365331, 364557, 365670,
                   368016, 369469]

    m_add = [1691864, 1599821, 1598871, 1942485, 1600183, 1599695, 1600104,
             1600225, 1602987, 1602682, 1748842, 1602618, 1600055, 1598157,
             1599273, 1599229, 1598888, 1599548, 1599433, 1599919, 1599078,
             1643490, 1615201, 1599872, 1602648, 1602997, 1600216, 1605647,
             1600218, 1605608]

    m_matmul_100 = [12793339, 12916947, 12708402, 12020015, 17699378, 13158661,
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

    n_matmul_100 = [92264, 78767, 78090, 77407, 77673, 77711, 77273, 77419,
                    77476, 77040, 77709, 77264, 77439, 77093, 77527, 77067,
                    102330, 105591, 78485, 77942, 77753, 77594, 77834, 110632,
                    127869, 122631, 111515, 97618, 96761, 134954]

    n_transpose = [29544, 8322, 8643, 7123, 5621, 10100, 7538, 2405, 8511,
                   6325, 5595, 5763, 5949, 5052, 3751, 7484, 6278, 8053, 6425,
                   5583, 4306, 6670, 15612, 12063, 13421, 4860, 2481, 2354,
                   8874, 6577]

    # Cast to numpy array
    t_add = np.array(t_add) / 1000
    t_matmul_100 = np.array(t_matmul_100) / 1000
    t_transpose = np.array(t_transpose) / 1000
    m_add = np.array(m_add) / 1000
    m_matmul_100 = np.array(m_matmul_100) / 1000
    m_transpose = np.array(m_transpose) / 1000
    n_add = np.array(n_add) / 1000
    n_matmul_100 = np.array(n_matmul_100) / 1000
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
    matmul_100_means = np.array(
        [np.mean(n_matmul_100), np.mean(t_matmul_100), np.mean(m_matmul_100)])
    matmul_100_stds = np.array(
        [np.std(n_matmul_100), np.std(t_matmul_100), np.std(m_matmul_100)])
    matmul_100_means = matmul_100_means.astype(int)
    matmul_100_stds = matmul_100_stds.astype(int)

    rects = plt.bar(x=range(len(matmul_100_means)),
                    height=matmul_100_means, tick_label=labels,
                    yerr=matmul_100_stds)
    autolabel(rects, matmul_100_stds)

    plt.title('Multiply Two 100x100 Element Arrays')
    plt.xlabel('Library / Vocabulary')
    plt.ylabel(r'Time ($\mu s$)')
    plt.ylim(top=max(matmul_100_means) * 1.2)
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

    # Transpose
    plt.title('Transpose a 100x100 Element Array')
    plt.xlabel('Library / Vocabulary')
    plt.ylabel(r'Time ($\mu s$)')
    plt.ylim(top=max(transpose_means) * 1.2)
    plt.show()


def linreg_benchmarking():
    labels = ['numpy', 'tensors', 'math.matrices']
    n_linreg = [56304216.384887695, 56652784.34753418, 61619997.02453613,
                91920137.40539551, 64600944.51904297, 53758144.37866211,
                49791812.896728516, 55835962.29553223, 53603172.302246094,
                54345846.17614746, 51870107.650756836, 56970834.732055664,
                58438062.66784668, 54279088.97399902, 51270961.76147461,
                56035041.80908203, 71886777.87780762, 161808252.33459473,
                123386859.89379883, 66714048.38562012, 65269947.05200195,
                66086053.8482666, 61708927.154541016, 64868211.74621582,
                56583881.37817383, 56859970.09277344, 54980039.59655762,
                55878877.63977051, 59067010.8795166, 61305999.755859375]

    t_linreg = [440903926, 450840980, 432761229, 411992620, 393458549,
                376823043, 387481884, 370435810, 454540747, 418382785,
                398029555, 443056542, 376570064, 381812345, 369848682,
                388916866, 376924448, 398357209, 406981266, 400735144,
                420804783, 399305186, 394554817, 406719578, 410475176,
                444186372, 472822702, 459279855, 4316531,   441150126]

    m_linreg = [1051107758, 1042712524, 1625986045, 2270926810, 1159551160,
                1251307886, 1178664170, 1183390364, 1306561253, 1227795418,
                1131305500, 1122022560, 1345095419, 1215394382, 1535152233,
                1811392629, 1460416420, 1305313674, 1393448097, 1219977020,
                1115528823, 1388364178, 1207547755, 1134284592, 1096196563,
                1378454943, 1188107075, 1113949479, 1301903432, 1280083293]

    # Cast to numpy array
    t_linreg = np.array(t_linreg) / 1000000
    m_linreg = np.array(m_linreg) / 1000000
    n_linreg = np.array(n_linreg) / 1000000

    linreg_means = np.array(
        [np.mean(n_linreg), np.mean(t_linreg), np.mean(m_linreg)])
    linreg_stds = np.array(
        [np.std(n_linreg), np.std(t_linreg), np.std(m_linreg)])
    linreg_means = linreg_means.astype(int)
    linreg_stds = linreg_stds.astype(int)

    rects = plt.bar(x=range(len(linreg_means)),
                    height=linreg_means, tick_label=labels, yerr=linreg_stds)
    autolabel(rects, linreg_stds)

    plt.title('Linear Regression on the Boston Housing Dataset')
    plt.xlabel('Library / Vocabulary')
    plt.ylabel(r'Time ($ms$)')
    plt.ylim(top=max(linreg_means) * 1.35)
    plt.show()


def main():
    linreg_benchmarking()


if __name__ == '__main__':
    main()

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize


def autolabel(rects):
    """
    Attach a text label above each bar in *rects*, displaying its height.
    Source:
    https://matplotlib.org/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
    """
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{} us'.format(height),
                     xy=(rect.get_x() + rect.get_width() / 2, height),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom')


def jan_31_benchmarking():
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


def test_func(x, a, b, c):
    return a * np.sin(b * x) + c


def feb_6_benchmarking():
    x_data = np.arange(30) + 1
    no_gc = [3051476, 3012790, 3221173, 2956580, 2596003, 2594998, 2663338,
             2825727, 3076740, 3045100, 2598003, 2592870, 2655172, 2628627,
             3096976, 2923263, 2596609, 2595064, 2592968, 2663469, 3107040,
             2911755, 2611512, 2600538, 2596673, 2623847, 3037184, 2970033,
             2597872, 2834640]

    with_gc = [2617837, 2611595, 2606830, 2608464, 2605527, 2609590, 2610261,
               2604330, 2603769, 2613516, 2609546, 2607349, 2639476, 2688193,
               2608280, 2607027, 2606865, 2605624, 2606139, 2606522, 2613550,
               2702453, 2777699, 2621044, 2780597, 3222790, 2624013, 2751122,
               2735148, 2608397]

    params, params_covariance = optimize.curve_fit(test_func, x_data, no_gc,
                                                   p0=[2500000, 1,
                                                       3000000])

    # 100 linearly spaced numbers
    x = np.linspace(1, 30, 1000)

    # the function, which is y = sin(x) here
    y = params[0] * np.sin(params[1] * x) + params[2]

    plt.plot(x_data, no_gc, 'co')
    plt.plot(x_data, with_gc, 'g+')
    plt.plot(x, y, 'r')
    plt.ylim(bottom=0, top=max(no_gc) * 1.1)
    plt.show()

    print(params)


def main():
    feb_6_benchmarking()


if __name__ == '__main__':
    main()

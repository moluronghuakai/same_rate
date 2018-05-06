#!/usr/bin/python

R = 0.1

direction_unknow = 0
direction_up = 1
direction_down = 2

def choose_peak(data, max_d):
    "get peak from data"
    peak_value = [data[0]]
    peak_index = [0]
    current_dir = direction_unknow
    d0 = 0.0

    for index in range(1, len(data)):
        if current_dir == direction_unknow:
            if data[index] > data[index - 1]:
                current_dir = direction_up
            elif data[index] < data[index - 1]:
                current_dir = direction_down
            continue

        if current_dir == direction_up and data[index] < data[index - 1]:
            current_dir = direction_down
            d0 = (data[index - 1] - peak_value[len(peak_value) - 1])/ max_d
            if d0 >= R:
                peak_value.append(data[index - 1])
                peak_index .append(index - 1)
            continue

        if current_dir == direction_down and data[index] > data[index - 1]:
            current_dir = direction_up
            d0 = (peak_value[len(peak_value) - 1] - data[index - 1]) / max_d
            if d0 >= R:
                peak_value.append(data[index - 1])
                peak_index.append(index - 1)
            continue

    return (peak_value, peak_index)


def calc_slope(peak):
    "calc slope according to peak value"
    slope = []
    sl = 0.0

    for index in range(1, len(peak[0])):
        sl = (peak[0][index] - peak[0][index - 1]) / (peak[1][index] - peak[1][index - 1])
        slope.append(sl)

    return slope


def calc_same(data0, data1, dmax):
    "calc same value"
    num = 0.0
    same_num = 0.0

    peak0 = choose_peak(data0, dmax)
    peak1 = choose_peak(data1, dmax)
    slope0 = calc_slope(peak0)
    slope1 = calc_slope(peak1)

    if len(slope0) <= len(slope1):
        num = len(slope0)
    else:
        num = len(slope1)

    for i in range(num):
        if slope0[i] * slope1[i] > 0:
            same_num += 1.0

    return same_num / num



class DataForm: 
    pass

def get_total_value_and_valid_iterations (distance_array):
    iteration_counter = 0
    total_value = 0

    for distance in distance_array:
        if (distance is not None):
            iteration_counter = iteration_counter + 1
            total_value = total_value + distance

    return [total_value, iteration_counter]

def getd_and_s_array(mid_margin, mid_array):
    d_and_s_array = []
    counter = 0
    counter2 = 0

    for distance in mid_array:
        if (distance is not None):
            if (distance >= mid_margin[1]):
                d_and_s_array.append('d')
                counter = counter + 1
            elif (distance <= mid_margin[0]):
                d_and_s_array.append('s')
                counter = counter + 1
            else:
                d_and_s_array.append(None)
        else:
            d_and_s_array.append(None)
            counter2 = counter2 + 1

    #print(f'None values: {counter2}')
    #print(f'Included values: {counter}')
    return d_and_s_array

def get_d_and_s_means(distance_array, d_and_s_array):
    d_total = 0
    s_total = 0

    iteration_counter_d = 0
    iteration_counter_s = 0

    length = len(distance_array)
    for i in range(length):
        if (d_and_s_array[i] is not None):
            if (d_and_s_array[i] == 'd'):
                iteration_counter_d = iteration_counter_d + 1
                d_total = d_total + distance_array[i]
            else:
                iteration_counter_s = iteration_counter_s + 1
                s_total = s_total + distance_array[i]

    if iteration_counter_d > 0 and iteration_counter_s > 0:
        return [d_total / iteration_counter_d, s_total / iteration_counter_s]                

    return [None,None]


def get_mean(total_value_and_number_of_iterations):
    return total_value_and_number_of_iterations[0] / total_value_and_number_of_iterations[1]

def cardiac_cycle(distances):
    top_array = distances.top
    mid_array = distances.mid
    bot_array = distances.bot

    mid_mean = get_mean(get_total_value_and_valid_iterations(mid_array))

    mid_margin = [mid_mean - mid_mean * 0.1, mid_mean + mid_mean * 0.1]
    d_and_s_array = getd_and_s_array(mid_margin, mid_array)

    top_means = get_d_and_s_means(top_array, d_and_s_array)
    mid_means = get_d_and_s_means(mid_array, d_and_s_array)
    bot_means = get_d_and_s_means(bot_array, d_and_s_array)

    result = DataForm()
    result.top_d = top_means[0]
    result.top_s = top_means[1]
    result.mid_d = mid_means[0]
    result.mid_s = mid_means[1]
    result.bot_d = bot_means[0]
    result.bot_s = bot_means[1]
    #result = {'top_d':, 'top_s':, 'mid_d':, 'mid_s':, 'bot_d':, 'bot_s':}
    return result
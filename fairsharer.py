def fair_sharer(values, num_iterations, share=0.1):
    for i in range(num_iterations):

        max_value = max(values)
        max_index = values.index(max_value)

        if max_index == len(values)-1:
            values[max_index - 1] = values[max_index - 1] + max_value * share
            values[0] = values[0] + max_value * share

            values[max_index] = max_value - 2 * (max_value * share)
        else:
            values[max_index - 1] = values[max_index - 1] + max_value * share
            values[max_index + 1] = values[max_index + 1] + max_value * share

            values[max_index] = max_value - 2 * (max_value * share)

    return values


print(fair_sharer([0, 1000, 800, 1100], 2))

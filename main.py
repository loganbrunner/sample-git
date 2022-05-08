def main(input_vals=[0, 0]):
    sum = sum_vals(input_vals)
    print(sum)


def sum_vals(input_vals):
    return input_vals[0] + input_vals[1]


if __name__ == '__main__':
    input_vals = [2, 5]
    main(input_vals)

def main(input_vals=[0, 0]):
    sum = sum_vals(input_vals)
    print(sum)


def sum_vals(input_vals):
    # MERGE CONFLICT
    x = 1
    return input_vals + input_vals[1]


if __name__ == '__main__':
    input_vals = [5, 50]
    main(input_vals)

def possibleSums(coins, quantity):
    # figure out all the possible sums
    # filter out the non unique coins

    # key: coin, value: total $ of coins
    coins_dict = {}
    quantities = []

    sums = []
    total = 0
    counter = 0

    for coin, num in zip(coins, quantity):
        # print(coin, num)
        coins_dict[coin] = coin * num

    for key, value in coins_dict.items():
        quantities.append(value)

    for x in quantities:
        # running total
        total += x
        # num of sums (prob not needed)
        counter += 1
        # adding possible sum to sums list
        sums.append(x)

    for index, value in enumerate(quantities):
        current = value
        next_value =
        next_pointer = index + 1
        last = len(quantities) - 1

        # print('next: ', next_pointer)
        # print('last: ', last)

        if next_pointer > last:
            new_sum = current + quantities[next_pointer]
            print(new_sum)

        # while next_pointer is not None:
        #     print(next_pointer)

        # while
        # new_sum = current + next_pointer
        # sums.append(new_sum)
        # next_pointer = next_pointer + 1

        # current_num = x
        # temp = x
        # next_num = temp + 1
        # new_sum = quantities[0]

        # new_sum = current_num + next_num
        # total += new_sum


        # while next_sum is not None:
        #     next_sum += 1
        # print(coins_dict)
        # print(quantities)
        # for x in quantity:
        #     coins_dict[coin] =
print(possibleSums([10, 50, 100], [1, 2, 1]))  # 9

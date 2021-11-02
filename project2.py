import random
# global variables for everyone to use
c1_average = 9
c1_sd = 3
c2_average = 7
c2_sd = 5
c3_average = 11
c3_sd = 7


# eGreedy(e) takes in a percent, e, and calculates the total happiness value when
# you go to a random cafeteria e% of the time and your favorite the rest of the time.
# Returns the total happiness within the trip
def eGreedy(e: int) -> int:
    e = e/100  # makes e into a decimal value
    total_happiness = 0  # tracks the total of happiness to be returned

    # track the happiness value for current iteration, for now... lets calculate for the first 3 days
    c1_happiness = random.normalvariate(c1_average, c1_sd)
    c2_happiness = random.normalvariate(c2_average, c2_sd)
    c3_happiness = random.normalvariate(c3_average, c3_sd)

    # tracks how many times the cafeteria is visited
    c1_times = 1
    c2_times = 1
    c3_times = 1

    # tracks the total happiness acquired at each cafeteria
    c1_happy_total = c1_happiness
    c2_happy_total = c2_happiness
    c3_happy_total = c3_happiness

    # holds the average happiness level for each cafeteria
    c1_average_happiness = c1_happiness
    c2_average_happiness = c2_happiness
    c3_average_happiness = c3_happiness

    total_happiness = c1_happiness + c2_happiness + c3_happiness  # get happiness for days 1-3

    for i in range(297):  # next 297 days...
        r = random.random()  # generates random float from 0 to 1
        if r < e:  # pick random cafeteria
            cafeteria = random.randint(1, 3)  # generate random int 1, 2, or 3
            if cafeteria == 1:  # if c1
                c1_happiness = random.normalvariate(c1_average, c1_sd)  # find happiness for trip
                c1_times += 1  # increment times visited variable
                c1_happy_total += c1_happiness  # add this trip to the cafeteria total
                c1_average_happiness = c1_happy_total/c1_times  # calculate average happiness for c1
                total_happiness += c1_happiness  # add happiness value for trip to total
            elif cafeteria == 2:  # if c2
                c2_happiness = random.normalvariate(c2_average, c2_sd)  # find happiness for trip
                c2_times += 1  # increment times visited variable
                c2_happy_total += c2_happiness  # add this trip to the cafeteria total
                c2_average_happiness = c2_happy_total / c2_times  # calculate average happiness for c2
                total_happiness += c2_happiness  # add happiness value for trip to total
            else:  # if c3
                c3_happiness = random.normalvariate(c3_average, c3_sd)  # find happiness for trip
                c3_times += 1  # increment times visited variable
                c3_happy_total += c3_happiness  # add this trip to the cafeteria total
                c3_average_happiness = c3_happy_total / c3_times  # calculate average happiness for c3
                total_happiness += c3_happiness  # add happiness value for trip to total
        else:  # go to favorite
            # like c1 the best
            if c1_average_happiness > c2_average_happiness and c1_average_happiness > c3_average_happiness:
                c1_happiness = random.normalvariate(c1_average, c1_sd)  # find happiness for trip
                c1_times += 1  # increment times visited variable
                c1_happy_total += c1_happiness  # add this trip to the cafeteria total
                c1_average_happiness = c1_happy_total / c1_times  # calculate average happiness for c1
                total_happiness += c1_happiness  # add happiness value for trip to total
            # like c2 the best
            elif c2_happiness > c3_average_happiness and c2_average_happiness > c1_average_happiness:
                c2_happiness = random.normalvariate(c2_average, c2_sd)  # find happiness for trip
                c2_times += 1  # increment times visited variable
                c2_happy_total += c2_happiness  # add this trip to the cafeteria total
                c2_average_happiness = c2_happy_total / c2_times  # calculate average happiness for c2
                total_happiness += c2_happiness  # add happiness value for trip to total
            # like c3 the best
            else:
                c3_happiness = random.normalvariate(c3_average, c3_sd)  # find happiness for trip
                c3_times += 1  # increment times visited variable
                c3_happy_total += c3_happiness  # add this trip to the cafeteria total
                c3_average_happiness = c3_happy_total / c3_times  # calculate average happiness for c3
                total_happiness += c3_happiness  # add happiness value for trip to total
    return int(total_happiness)  # change float to int to make it easier to work with




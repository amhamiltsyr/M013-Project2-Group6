import random
# global variables for everyone to use
c1_average = 9
c1_sd = 3
c2_average = 7
c2_sd = 5
c3_average = 11
c3_sd = 7


def exploitOnly():
    average = [c1_average, c2_average, c3_average]
    standardDev = [c1_sd, c2_sd, c3_sd]
    times = 300    # total 300 times
    totalHappiness = 0  # final value to return

    # create a list to find the best Happiness value
    firstThreeDays = []
    for i in range(3):
        firstThreeDays.append(random.normalvariate(average[i], standardDev[i]))
        times -= 1                          # 300 minus 3

    # find the best cafeteria
    best = 0
    for i in range(len(firstThreeDays)):
        if firstThreeDays[i] > firstThreeDays[best]:
            best = i

    # first three times happiness value
    totalHappiness = sum(firstThreeDays)

    # with remaining 297 times
    while times != 0:
        totalHappiness += random.normalvariate(average[best], standardDev[best])
        times -= 1

    return int(totalHappiness)  # cast to int for ease of simulation


def exploreOnly():
    total = 0
    # visit each cafeteria the same number of times.
    # calculate happiness based on normal distribution with certain mean and standard deviation
    for i in range(100):
        happiness = random.normalvariate(c1_average, c1_sd)
        total = total + happiness
    for i in range(100):
        happiness = random.normalvariate(c2_average, c2_sd)
        total = total + happiness
    for i in range(100):
        happiness = random.normalvariate(c3_average, c3_sd)
        total = total + happiness
    # return the sum of happiness value generated.
    return int(total)


def eGreedy(p_e: int) -> float:
    p_e = p_e/100  # makes e into a decimal value
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
        if r < p_e:  # pick random cafeteria
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
    return int(total_happiness)


def simulation(trial: int, e: int):
    optimumHappiness = max(c1_average, c2_average, c3_average)*300
    exploitResults = 0
    exploreResults = 0
    egreedyResults = 0
    for i in range(trial):
        exploitResults = exploitResults + exploitOnly()

        exploreResults = exploreResults + exploreOnly()

        egreedyResults = egreedyResults + eGreedy(e)

    exploitAverage = exploitResults / trial
    exploreAverage = exploreResults / trial
    egreedyAverage = egreedyResults / trial

    exploitRegret = optimumHappiness - exploitAverage
    exploreRegret = optimumHappiness - exploreAverage
    egreedyRegret = optimumHappiness - egreedyAverage

    print(
    "Optimum Happiness:" + str(optimumHappiness) + "\n"
    "-----------------------" + "\n"
    "Exploit Expected Hapiness:" + str(c1_average+c2_average+c3_average+max(c1_average, c2_average, c3_average)*297) + "\n"
    "Exploit Average Hapiness:" + str(exploitAverage) + "\n"
    "\n"
    "Exploit Expected Regret:" + str(optimumHappiness-(c1_average+c2_average+c3_average+max(c1_average, c2_average, c3_average)*297)) +
    "\n"
    "Exploit Average Regret:" + str(exploitRegret) + "\n"
    "---------------------" + "\n" +
    "Explore Expected Hapiness:" + str(c1_average*100+c2_average*100+c3_average*100) + "\n"
    "Explore Average Hapiness:" + str(exploreAverage) + "\n"
    "\n"
    "Explore Expected Regret:" + str(optimumHappiness -(c1_average*100+c2_average*100+c3_average*100)) + "\n"
    "Explore Average Regret:" + str(exploreRegret) + "\n"
    "---------------------" + "\n"
    "eGreedy Expected Hapiness:" + str((e/100/3)*300*c1_average+(e/100/3)*300*c2_average+(e/100/3)*300*c3_average+(1-e/100)*300*max(c1_average, c2_average, c3_average)) + "\n"
    "eGreedy Average Hapiness:" + str(egreedyAverage) + "\n"
    "\n"
    "eGreedy Expected Regret:" + str(optimumHappiness-((e/100/3)*300*c1_average+(e/100/3)*300*c2_average+(e/100/3)*300*c3_average+(1-e/100)*300*max(c1_average, c2_average, c3_average))) + "\n"
    "eGreedy Average Regret:" + str(egreedyRegret)
    )


question = int(input("Insert number of trials:"))
pass_in_e = 12
simulation(question, pass_in_e)

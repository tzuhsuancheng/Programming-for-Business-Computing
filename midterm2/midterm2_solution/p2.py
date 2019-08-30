sequence = []   # for storing the whole input sequence
while True:
    input_str = input()
    if input_str == "BREAK":    # End of input
        if len(sequence) < 8:   # if number of data < 8, NOT_ENOUGH_DATA
            print("NOT_ENOUGH_DATA")
            break
        
        for idx in range(7, len(sequence)): # from C+1th data to end
            past_sequence = []  # store the history data in the same periodic phase
            for i in range(1, 6):   # search for 5 history data
                if idx - i * 7 < 0: # no available history data
                    break
                past_sequence.append(sequence[idx - i * 7])
            past_sequence = sorted(past_sequence)   # sort the history data for computing median
            length = len(past_sequence)
            if length % 2 == 0: # if number of data is even, median is the mean of middle two
                median = (past_sequence[length // 2 - 1] + past_sequence[length // 2 ]) / 2
            else:   #if number of data is odd, median is the middle data
                median = past_sequence[length // 2]
            print("%0.2f" % (sequence[idx] - median))

        break
    try:    # check for valid number
        input_number = float(input_str)
    except:
        print("DATA_ERROR")
        break
    sequence.append(input_number)   # build the whole sequence

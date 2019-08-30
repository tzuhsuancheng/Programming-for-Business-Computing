import datetime

filename = input()  # filename from input

answer = [] # store the answer, sorted list of dictionary

with open(filename, "r", encoding="CP950") as f:    # open file with CP950 encoding
    lines = f.readlines()   # read all lines
    for line_idx in range(1, len(lines)):   # traverse all lines
        line = lines[line_idx]
        line_split = line.split('\t')   # split by tab

        stock_symbol = line_split[0].strip()    # store the stock symbol

        # date decomposition
        year = int(line_split[2][0:4])
        month = int(line_split[2][4:6])
        day = int(line_split[2][6:8])

        # other fields
        opening = float(line_split[3])
        day_high = float(line_split[4])
        day_low = float(line_split[5])
        closing = float(line_split[6])
        volume = float(line_split[7])

        # insert this data into the answer list
        # if the current year month is already recorded, merge into the record
        # if not, insert new record
        insert_idx = 0
        merge = False   # for the situation is merge or not
        while insert_idx <len(answer):
            if answer[insert_idx]["year"] == year and answer[insert_idx]["month"] == month: # existing record match the year and month
                merge = True
                # check for opening day
                if answer[insert_idx]["opening_day"] > day:
                    answer[insert_idx]["opening_day"] = day
                    answer[insert_idx]["opening"] = opening
                # check for closing day
                if answer[insert_idx]["closing_day"] < day:
                    answer[insert_idx]["closing_day"] = day
                    answer[insert_idx]["closing"] = closing
                # check for day high
                if answer[insert_idx]["day_high"] < day_high:
                    answer[insert_idx]["day_high"] = day_high
                # check for day low
                if answer[insert_idx]["day_low"] > day_low:
                    answer[insert_idx]["day_low"] = day_low
                # accumulate the volume
                answer[insert_idx]["volume"] += volume

            # the list is sorted by the year and month
            # if found year and month is posterior to the current data, can break the loop
            elif answer[insert_idx]["year"] == year and answer[insert_idx]["month"] > month:
                break
            elif answer[insert_idx]["year"] > year:
                break
            insert_idx += 1

        # if it's not merge, insert is needed
        if not merge:
            this_day = {}   # new year-month data for this record
            this_day["year"] = year
            this_day["month"] = month
            this_day["opening_day"] = day
            this_day["closing_day"] = day
            this_day["opening"] = opening
            this_day["day_high"] = day_high
            this_day["day_low"] = day_low
            this_day["closing"] = closing
            this_day["volume"] = volume
            answer.insert(insert_idx, this_day)
# output the answer with required foramt
for idx in range(len(answer)):
    # compose the date format
    date = str(answer[idx]["year"]) + "%02d%02d" % (answer[idx]["month"], answer[idx]["opening_day"])
    print("%s,%s,%0.2f,%0.2f,%0.2f,%0.2f,%d" % (stock_symbol, date, answer[idx]["opening"], answer[idx]["day_high"], answer[idx]["day_low"], answer[idx]["closing"], answer[idx]["volume"]))
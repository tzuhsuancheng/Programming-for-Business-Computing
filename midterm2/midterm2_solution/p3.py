filename = input()  # filename from input

number_character = "0123456789(),$" # recognizing characters

answer = [] # store the answer, sorted list of dictionary

with open(filename, "r", encoding="UTF-8") as f:    # open file with utf-8 encoding
    lines = f.readlines()   # read all lines
    for line_idx in range(len(lines)):  # traverse all lines
        line = lines[line_idx].rstrip() # remove blank, tab and newline in the right of the line

        count = 0
        for idx in range(len(line)):    # count the number of occurrence
            if line[idx] in number_character:
                count += 1
        
        #   insert this line into sorted position in the answer list (insertion sort)
        insert_idx = 0
        while insert_idx < len(answer):
            if answer[insert_idx]["count"] < count: # find the position where the number count of current line is larger than the line in the list position
                break
            insert_idx += 1
        answer.insert(insert_idx, {"line_no":line_idx+1, "line_content": line, "count":count})  # insert this line

for i in range(10): # output top 10 
    print("@%d: %s" % (answer[i]["line_no"], answer[i]["line_content"]))
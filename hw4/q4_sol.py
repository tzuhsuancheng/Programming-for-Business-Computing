### input
line1 = input().split(',')
n = int(line1[0])
m = int(line1[1])

service_time = input().split(',')
reserve_time = input().split(',')
benefit = input().split(',')

### change to int
for i in range(n):
    service_time[i] = int(service_time[i])
    reserve_time[i] = int(reserve_time[i])
    benefit[i] = int(benefit[i])

customer_sequence = [] # record indeces of sorted customers
for customer in range(n):
    customer_sequence.append(customer)

### sort the customers
### bubble sort
for i in range(n):
    for j in range(i+1, n):
        swap = False
        if service_time[customer_sequence[i]] > service_time[customer_sequence[j]]: # smaller service time wins
            swap = True
        elif service_time[customer_sequence[i]] == service_time[customer_sequence[j]]:
            if reserve_time[customer_sequence[i]] > reserve_time[customer_sequence[j]]: # earlier reserve time wins
                swap = True
            elif reserve_time[customer_sequence[i]] == reserve_time[customer_sequence[j]]:
                if customer_sequence[i] > customer_sequence[j]: # smaller customer number wins
                    swap = True
        if swap: # True if swap of the two is needed, then swap customer_sequence[i] and customer_sequence[j]
            temp = customer_sequence[i]
            customer_sequence[i] = customer_sequence[j]
            customer_sequence[j] = temp


### use timeline to record the state of every working minutes for each barber
available_time = [] # timelines of all barbers
for i in range(m):
    timeline = []
    for j in range(360): # 360 minutes each
        timeline.append(0)
    available_time.append(timeline)


service_count = 0 # total service count
total_benefit = 0 # total benefit

### start arranging the customers to barbers in previously sorted order
for customer in customer_sequence:
    least_waiting_time = 31 # initial least waiting time
    chosen_barber = -1 # initial chosen barber index
    for barber in range(m): # traverse all barbers to find the most suitable barber (stored in chosen_barber)
        for start_time in range(reserve_time[customer], reserve_time[customer] + 31): # waiting for 0 ~ 30 mins maxima
            barber_available = True # check if this barber is available for this customer
            for time in range(start_time, start_time + service_time[customer]): # find consecutive available minutes
                if time >= 360 or available_time[barber][time] != 0: # no later than 360 and not occupied
                    barber_available = False
                    break
            if barber_available == True: # True if there is consecutive available minutes
                waiting_time = start_time - reserve_time[customer]
                if waiting_time < least_waiting_time: # record the barber with least waiting time
                    least_waiting_time = waiting_time
                    chosen_barber = barber
                break
                    
    if chosen_barber != -1: # arrange the customer to the chosen barber
        service_count += 1
        total_benefit += benefit[customer]
        # change the timeline status of the chosen barber
        for time in range(reserve_time[customer] + least_waiting_time, reserve_time[customer] + least_waiting_time + service_time[customer]):
            available_time[chosen_barber][time] = 1
            
### output
print(str(service_count) + ',' + str(total_benefit))
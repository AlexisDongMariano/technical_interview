def mimimum_rooms(time_intervals):
    sorted_time = sorted(time_intervals)
    end_time = []

    for index_time in range(len(sorted_time)):
        if end_time and end_time[0] < sorted_time[index_time][0]:
            end_time.pop()
        end_time.append(sorted_time[index_time][1])
        
    print(end_time)
         

# (0, 50), (30, 75), (60, 150)
# 50 < 30

time_intervals = [(30, 75), (0, 50), (60, 150)]


print(mimimum_rooms(time_intervals))
import numpy as np


# creating data for >=2 saensors per object

def upd_x(n, num_of_sensors, max_working_time):
    # max_working_time is n x num_of_sensors vector of values
    data_len = [[0 for _ in range(num_of_sensors)] for _ in range(n)]

    for i in range(n):
        for j in range(num_of_sensors):
            data_len[i][j] = np.random.randint((max_working_time[i][j])/2, (max_working_time[i][j]) + 1)

    x = [[0 for _ in range(num_of_sensors)] for _ in range(n)]
    for i in range(n):
        for j in range(num_of_sensors):
            time_of_break = np.random.randint(data_len[i][j]/2, (data_len[i][j] - 1) + 1)
            z1 = np.random.random(time_of_break)/4
            z2 = np.random.random(data_len[i][j] - time_of_break)*0.75 + 0.25
            z = [*z1, *z2]
            z.sort()
            z[data_len[i][j] - 1] = 1
            x[i][j] = z

    for i in range(len(data_len)):
        print(data_len)
    return x

# update data for 1 specific object

def upd_x_i(n, num_of_sensors, max_working_time, x, ind):

    data_len = [0 for _ in range(num_of_sensors)]

    for j in range(num_of_sensors):
        data_len[j] = np.random.randint((max_working_time[ind][j])/2, (max_working_time[ind][j]) + 1)

    for j in range(num_of_sensors):
        time_of_break = np.random.randint(data_len[j] / 2, (data_len[j] - 1) + 1)
        z1 = np.random.random(time_of_break) / 4
        z2 = np.random.random(data_len[j] - time_of_break) * 0.75 + 0.25
        z = [*z1, *z2]
        z.sort()
        z[data_len[j] - 1] = 1
        x[ind][j] = z

    print(data_len)
    return x


temp1 = 2
temp2 = 2
temp3 = [[10, 10], [10, 10]]

result = upd_x(temp1, temp2, temp3)

for i in range(len(result)):
    print(result[i])

result = upd_x_i(temp1, temp2, temp3, result, 0)

for i in range(len(result)):
    print(result[i])


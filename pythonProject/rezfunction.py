# version 10.24
import numpy as np
import copy


def upd_data(i, x):
    data_len_new = np.random.randint(81, 100 + 1)
    time_of_break = np.random.randint(data_len_new/2, (data_len_new - 1) + 1)
    z1 = np.random.random(time_of_break)/4
    z2 = np.random.random(data_len_new - time_of_break)*0.75 + 0.25
    z = [*z1, *z2]
    z.sort()
    z[data_len_new - 1] = 1
    x[i] = z


def upd_x(n):
    data_len = np.random.random_integers(81, 100, n)
    x = []
    for i in range(n):
        time_of_break = np.random.randint(data_len[i]/2, (data_len[i] - 1) + 1)
        z1 = np.random.random(time_of_break)/4
        z2 = np.random.random(data_len[i] - time_of_break)*0.75 + 0.25
        z = [*z1, *z2]
        z.sort()
        z[data_len[i] - 1] = 1
        x.append(z)

# def upd_data(i, beg, end, x):
#     data_len_new = np.random.random_integers(beg, end, 1)
#     z = np.random.random(data_len_new)
#     z.sort()
#     z[data_len_new - 1] = 1
#     x[i] = z


# def get_fun(n):
#     def fun(x):
#         return x + n
#     return fun
#
# fun = get_fun(3)
# print(fun(10))

def get_rez_func_params(test_time, maint_coef, maint_time, n, x):
    def rez_func(y):
        # n = len(y)
        upd_x(n)
        y_local = copy.deepcopy(y)
        for i in range(n):
            y_local[i] /= 100
        rez = 0  # counter for useful working time of each obj
        # rezminus = 0
        # counter for maintenance cost for each obj
        counter = np.random.random_integers(1, 70, n)  # step in time table showing
        isworking = [1] * n
        # isworking[i] = 1 means object is working , isworking[i] = 0 means obj is stopped for reapair ,2 - waiting
        stop_point = [0] * n

        for i in range(test_time):
            # print(i, isworking)

            for j in range(n):
                if isworking[j] == 0 or isworking[j] == 2:

                    if counter[j] == maint_time:  # 20 ??? iterations stop for maintenance
                        if isworking[j] == 0:
                            upd_data(j, x)   # object supposed to start working again, so we will use new data
                            counter[j] = 0
                        else:
                            counter[j] = stop_point[j]

                        isworking[j] = 1
                else:

                    if x[j][counter[j]] < 0.8:
                        rez += 1

                    if x[j][counter[j]] >= 0.8:
                        # rezminus += x[j][counter[j]] * maint_coef
                        # basic cost for maintenance = maint_coef * percent of usage
                        isworking[j] = 0
                        counter[j] = 0
                        # object j is stopped now we need to check all next
                        for k in range(j + 1, n, 1):
                            if isworking[k] == 0 or isworking[k] == 2:
                                counter[k] = 0
                            else:
                                if x[k][counter[k]] >= y_local[k]:  # checking the vector conditions
                                    # rezminus += x[k][counter[k]] * maint_coef
                                    # cost of maintenance should be proportionate to time the object is used
                                    isworking[k] = 0
                                else:
                                    stop_point[k] = counter[k]
                                    isworking[k] = 2
                                counter[k] = 0

            for j in range(n):
                counter[j] += 1
        return rez
    return rez_func

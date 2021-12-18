import matplotlib.pyplot as plt
def show_dist (x,n):
  for i in range(n):
    plt.plot(x[i])
    plt.ylabel(str(i+1) + ' object data')
    plt.show()
def plot_sieve(all_nmax, all_proportions, xlabel, ylabel, log_scale=True):
    plt.plot(all_nmax, all_proportions)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if log_scale = True:
        plt.xscale("log")
        plt.yscale("log")

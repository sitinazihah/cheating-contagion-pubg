from tools import count_motifs
from simulation_tools import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def main():
    pass


def run_simulations(cheaters, kills):
    '''Given two lists of formatted values i.e. cheaters and kills,
    returns a list containing 10 victim-cheater motif counts for 10
    simulated kills data.'''

    # create the 3 dictionaries needed to run get_simulation
    dic_cheaters = get_matches_with_cheaters(cheaters, kills)
    dic_groups = group_all_matches(kills)
    dic_non_cheaters = get_non_cheaters(dic_cheaters, dic_groups)

    count = []
    # run get_simulation 10 times and get the victim-cheater motif counts
    for i in range(10):
        # call get_simulation straight in the count_motifs function
        # for space optimization (to avoid saving each simulated lists)
        count.append(count_motifs(cheaters, get_simulation\
        (dic_cheaters, dic_groups, dic_non_cheaters)))

    return count


def comparison_plot(real, simulated):
    '''Given an integer i.e. real and a list i.e. simulated, plots a
    histogram from the values in simulated, as well as a vertical line within
    the plot using the integer, real.'''

    fig, ax = plt.subplots(figsize = (12,6))
    plt.hist(simulated, color='darkblue', bins='auto',
            ec='black', label='Simulated')
    plt.xlabel('Victim-Cheater Motif Count', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.title('Histogram - Real vs. Simulated Networks', fontsize=13)

    # set axes ticks to integers to better represent count and frequency
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    # add a vertical line and a label for the real network motif count
    plt.axvline(real, color='red', label='Real')
    plt.text(real+0.1, 1.0, real, color='red', fontsize=12)

    # add a legend outside the plot area since the randomisations would cause
    # the plot to take up different areas within the plot in each run
    plt.legend(fontsize=12, bbox_to_anchor=(1.2, 0.6),
               fancybox=True, shadow=True)
    plt.show()


if __name__ == '__main__':
    main()

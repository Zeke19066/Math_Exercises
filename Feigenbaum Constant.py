'''
The Logistic Map:
Xn+1 = lambda(Xn)*(1-Xn)

X = population level. 0 is empty, 1 is 'full'. You can't have an infinite population...
n = year
lambda = fertility rate. This will have to be a float between zero and four, with the following effects:
        - 0-1:    population declines towards zero.
        - 1-3:    population stabalizes, with higher stabalized value as you approach 3.
        - 3-3.5:  population stabalizes into a range of values as it alternates between them each year.
        - 3.5-4:  chaotic without a clear pattern, with the eception of a 3 fork at 3.84, 3.63, 3.74. These can only be seen at lower lamb_incriment values (.005 - .0001).
        - 4+:     infinite outputs; no plot.

Therefore Xn+1 = next year's population.
(1-Xn); as population increases it can put pressure on resources, so we're accounting for that reduction here as a deathrate.
lambdaXn is the growth portion of the population function.

Feigenbaum Constant = 4.6692016 . This number is a ratio that descrbes the rate of bifourcation in all quadratic functions. As the Logistic Map 
forks in its stabalized value, this ratio decribes the increasing rate at which forks occur.

WARNING: If lamb_incriment less than .005 it takes a while to plot (about 45+ seconds).
'''
import matplotlib.pyplot as plt

#inputs for single iteration of the The Logistic Map [feigenbaum()]
lamb = 3.125
x= 0.5 # 50% Population.
cycles = 100 # How many times will we iterate over this function?

#inputs for generating our graph dataset [feigenbaum_chart()]
lamb_incriment = .001 # Our x axis 'resolution'
lamb_limit = 4 # What is the highest lambda we wish to compute?
detail_level = 5# How much do we want to round down the stabalized population values? Our y axis 'resolution'

def feigenbaum(lamb, x, cycles, print_check=True):
    global detail_data
    forks = [] 
    detail_data = []
    last_pop = x # We're going to start at the beggining population.
    for i in range(1, cycles+1):
        next_pop = lamb*last_pop*(1-last_pop)
        fig = round(next_pop, 3)
        detail = round(next_pop, detail_level) #this data set will be used for the feigenbaum_chart() plot.
        #print(f'Next Pop: {next_pop}   cycle: {i}   fig:{fig}')
        last_pop = next_pop
        if i > (cycles*0.9):
            if fig not in forks:
                forks.append(fig)
            if detail not in detail_data:
                detail_data.append(detail)
    if print_check:
        print(f'Sorted repeating outputs: {sorted(forks)}')
        #print(f'Sorted detail_data: {sorted(detail_data)}')

def feigenbaum_chart(lamb_incriment):
    global plot_points, fork, y_plot, x_plot, lamb_limit
    x_plot = [0]
    y_plot = [[0]]
    last_pop = .5 # Let's start with 50% population.
    last_lamb = 0
    next_lamb = 0

    while next_lamb < lamb_limit: #calculating lambdas upto 4.  
        next_lamb = last_lamb + lamb_incriment
        last_lamb = next_lamb
        x_plot.append(next_lamb)
        feigenbaum(next_lamb, 0.5, 100, print_check=False)
        y_plot.append(detail_data)

    #plotting stuff here.
    print(f'Starting the plot at lamb_incriment {lamb_incriment}. WARNING: lamb_incriment < .005 take about 45+ seconds to plot.')
    plt.rcParams['axes.facecolor'] = 'black'
    for xe, ye in zip(x_plot, y_plot):
        plt.scatter([xe] * len(ye), ye, marker= "*") #c='yellow' drop in this kawrg to change the dot color. 
    plt.subplots_adjust(left=0.09, right=0.99, top=0.99, bottom=0.09)
    plt.ylabel('Stabalized Values')
    plt.xlabel('Input Lambda')
    plt.grid(True)
    plt.show()

# Select which function you want.
#feigenbaum(lamb, x, cycles)
feigenbaum_chart(lamb_incriment)
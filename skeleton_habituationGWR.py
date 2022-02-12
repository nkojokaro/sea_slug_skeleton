# Based on Tom Anastasio's habituationGWR.m
# this script sets up a very simple simulation of habituation
# of the Aplysia gill withdrawal reflex
#
# Modified for BU's RISE Practicum Comp Neuro lab by mbezaire@bu.edu
#
###############################
# import libraries with special
# functions needed in this script
###############################
import numpy as np
import matplotlib.pyplot as plt

###############################
# Define input stimulation
###############################
# TODO: Set a variable called stv CHANGED TO STARTING_WEIGHT to 4, this will define 
#        the weight of the connection from input to output
starting_weight = 4 #formally stv

# TODO: set up an input pulse called pls
pulse = [0, 0, 1, 0, 0] #formally pulse


# TODO: then create a list of 6 pulses, called x CHANGED TO INPUT, to use for input
input_stim = pulse * 6

weight = starting_weight# Set connection weight to start weight value

habituation = 0.7 #rate at which sea slug gets used to the pulse

###############################
# Set up and run simulation
###############################

nTs = len(input_stim) # find the length of the input list
output = np.zeros((1,nTs)) # set up (define) a vector for the output time series

# TODO: use a for-loop to iterate 
#        through each time step in 
#        the input series and calculate
#        the output at each time step. Ex:
for t in range(nTs):
    output[0,t] = input_stim[t] * weight
    
    #when sea slug habituates, set:
    if (input_stim[t] > 0):
        weight *= habituation
    
#     then indent 4 spaces and write the equation that
#     describes how each input value in the vector x is 
#     transformed to the output value in the vector y



###############################
# Plot the results
###############################
def showresults(x,y,nTs,stv):
    # Plot both the input series (vector x)
    # and the resulting output series (vector y)
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.plot(x) #, color='white',  antialiased=False, edgecolors='black', linewidth=1, shade=False, alpha=1)
    ax1.set_ylabel('Input')
    ax1.set_xlim(0, nTs)
    ax1.set_ylim(0, 1.1)
    
    ax2 = fig.add_subplot(212)
    ax2.plot(y[0]) #, color='white',  antialiased=False, edgecolors='black', linewidth=1, shade=False, alpha=1)
    ax2.set_xlabel('Time step')
    ax2.set_ylabel('Output')
    ax2.set_xlim(0, nTs)
    ax2.set_ylim(0, stv+0.5)
    
    plt.show()

# TODO prepare file for Gradescope before committing and submitting!
# - Comment out the call to showresults below
# - Comment out any print statements added during code development
# - Make sure you keep x, y, pls, and other variable names the same
showresults(input_stim,output,nTs,starting_weight)

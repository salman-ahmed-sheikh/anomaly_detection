import numpy as np
#import matplotlib.pyplot as plot
# Get x values of the sine wave

def generate(num = 500):
    # generate sine wave with frequency of 1.4 and amplitude of 3
    time        =  3* np.arange(0, num, 1.4)
    # generate sine wave with frequency of 0.7 and amplitude of 1
    time2        = np.arange(0, num/4, 0.7)
    res = []
    # accumulate both frequencies
    for i,j in zip(time,time2):
        res.append(i+j)
    
    time = np.array(res)
    #convert that data to sine wave using numpy function
    amplitude   = np.sin(time)
    # add ampliture
    m = np.min(amplitude)
    # to make if positive
    amplitude = np.add(amplitude,m * -1)
    # return generated data
    return amplitude

'''
amp = generate()
time = [i for i in range(amp.shape[0])]
# Plot a sine wave using time and amplitude obtained for the sine wave
plot.plot(time, amp)
# Give a title for the sine wave plot
plot.title('Sine wave')
# Give x axis label for the sine wave plot
plot.xlabel('Time')
# Give y axis label for the sine wave plot
plot.ylabel('Amplitude = sin(time)')
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.show()
'''

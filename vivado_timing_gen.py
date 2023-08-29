############################################
#       Vivado Timing Code Generator       #
#                Python 2.7                #
#            Luca Sander-Bowness           #
#               29-08-2023                 #
#******************************************#
#   To generate the timing code for the    #
#       inputs in a Vivado simulation.     #
#           Format output will be:         #
#  '0', '1' after ?ns, '0' after ?ns, etc. #
############################################

import time # imports the time library.
            # The time library is used to get the current system time for the output file name.
import sys # Need this lib to check the python version.
if sys.version_info[0] > 2:
    from six.moves import input as raw_input # Python 3+ does not like raw_input - this fixes that issue

print("\nThis will create a file with vivado timing code that you can paste under each input")
print("The file will be created in the local directory")
print("\n***** Make sure you have write permissions here! *****\n")

bitsNumber = raw_input("How many bits do you need? ")
bitsNumber = int(bitsNumber)    # Converts the raw input to an integer.
                                # Was encountering bugs as the raw input is passed as a string.
if bitsNumber > 16: # Checks to see if the user has input an appropriate number
    print("\nToo many bits. File would be huge!")
    print("\n***** EXITING *****\n")
    raise Exception("bitsNumber too large") 
    exit()

timeStep = raw_input("What is your time step in nanoseconds? ")
timeStep = int(timeStep)    # Converts the raw input to an integer.
                            # Was encountering bugs as the raw input is passed as a string.

currentTime = time.strftime("%y-%m-%d_%H-%M-%S", time.localtime()) # Formats the time for the filename.
fileName = "%s-bit_%s-ns_%s" % (bitsNumber, timeStep, currentTime) # Sets the filename to xxx-bits_xxx-ns_date_time
print("Output file: %s.txt \n" % (fileName)) # Prints the name of the output file to the command line.
f = open("%s.txt" % (fileName), "at") # Opens a file with the name fileName.txt, in append-text mode.

maxTimesteps = (2 ** bitsNumber) - 1    # Calculates the maximum number of steps required.
                                        # 2^bits - 1 = max steps. E.g. 4 bits = 2^4 - 1 = 15 steps
                                        # Does not include the initial step, as it is step 0.

iterate = 0     # Sets the initial value of the outer loop iteration counter.
bit = 1         # Sets the initial value of the bit.

while iterate < bitsNumber:
    # This outer while loop outputs the initial value of '0', 
    # It then sets the inner loop iteration counter, and the timestep, based on the current iteration of the outer loop.
    f.write("'0', "),
    i = maxTimesteps / (2 ** iterate)
    time = timeStep * (2 ** iterate)
    while i > 0:
        if i == 1:  # On the final iteration, changes the format of the output to add a semi-colon.
                    # It also leaves the value of bit as 1, to assist with the next iteration.
            f.write("'%s' after %sns;" % (bit, time))
            i -= 1
        else:       # If it isn't the final iteration, do the normal loop section.
            f.write("'%s' after %sns, " % (bit, time)), # Output the state required at the time step.
            if bit == 0: # Flip the value of the bit variable.
                bit = 1
            else:
                bit = 0
            time += timeStep * (2 ** iterate) # Add the time for the next iteration.
            i -= 1
    # Chuck in a couple of newlines to neaten the file a little.
    f.write("\n")
    f.write("\n")
    iterate += 1 # Add to the outer loop iteration counter.
f.close() # Close the file! Important!!
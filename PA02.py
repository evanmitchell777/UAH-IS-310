"""
Author: Evan Mitchell
Date: 9/17/21
Assignment: PA02_Statistical_Processing
Semester/Year: Fall 2021
Course Number and Title: IS310-01 Adcanced Computer Programming in Business 
About the Program: This program calculates and displays the min, max, range, mean, median, average mode for a list of given cities and their weekly gas prices over a year.

Input: list of gas prices for various cities 
Output: min, max, range, mean, meadian, average mode and mode of requested data 
"""
import statistics

print(__doc__)
def main():
#list for boston prices 
    boston = [2.643, 2.63, 2.632, 2.634, 2.635, 2.633, 2.636, 2.649, 2.654, 2.652, 2.654,
    2.657, 2.663, 2.682, 2.669, 2.663, 2.674, 2.739, 2.761, 2.777, 2.791, 2.79, 2.806,
    2.802, 2.814, 2.799, 2.791, 2.771, 2.788, 2.831, 2.859, 2.882, 2.893, 2.913, 2.923,
    2.881, 2.808, 2.724, 2.654, 2.638, 2.61, 2.543, 2.491, 2.484, 2.477, 2.44, 2.458, 
    2.48, 2.506, 2.521, 2.518, 2.539]

#obtaining max value 
    bos_max=(max(boston))
#obtaining min value 
    bos_min=(min(boston))
#obtaining range value 
    bos_range = bos_max - bos_min
#obtaining mean value 
    bos_mean = sum(boston)/int(len(boston))
#obtaining median value
    bos_median = statistics.median(boston)
#obtaining mode value
    bos_mode = statistics.multimode(boston)
#obtaining average mode value 
    bos_avgmode = sum(bos_mode)/len(bos_mode)

#list for chicago gas prices 
    chicago = [2.731, 2.726, 2.726, 2.757, 2.683, 2.739, 2.804, 2.742, 2.726, 2.793,
    2.839, 2.939, 2.931, 2.858, 2.986, 2.867, 2.792, 2.879, 2.923, 2.889, 2.905, 
    3.083, 3.193, 3.214, 3.385, 3.194, 3.156, 3.052, 2.967, 3.093, 3.265, 3.259, 3.263,
    3.336, 3.267, 3.222, 3.183, 3.09, 3.098, 3.002, 2.88, 2.8, 2.665, 2.578, 2.609, 2.477, 
    2.41, 2.345, 2.255, 2.303, 2.268, 2.237]

#obtaining max value 
    chi_max=(max(chicago))
#obtaining min value 

    chi_min=(min(chicago))
#obtaining range value 

    chi_range = chi_max - chi_min
#obtaining mean value 

    chi_mean = sum(chicago)/int(len(chicago))
#obtaining median value

    chi_median = statistics.median(chicago)
#obtaining mode value

    chi_mode = statistics.multimode(chicago)
#obtaining average mode value 

    chi_avgmode = sum(chi_mode)/len(chi_mode)

#gas price statistics for cleveland 
    cleveland = [2.692, 2.567, 2.632, 2.585, 2.652, 2.554, 2.605, 2.486, 
    2.532, 2.495, 2.581, 2.679,2.613, 2.647, 2.772, 2.656, 2.615, 2.622,
    2.584, 2.661, 2.636, 2.781, 2.762, 2.839, 2.838, 2.733, 2.718, 2.624, 
    2.495, 2.566, 2.841, 2.646, 2.805, 2.702, 2.801, 2.732, 2.755, 2.677, 
    2.693, 2.65, 2.566, 2.502, 2.497, 2.412, 2.419, 2.296, 2.234, 2.18, 2.114, 2.059, 2.046, 2.011]

#obtaining max value 

    clev_max=(max(cleveland))
#obtaining min value 

    clev_min=(min(cleveland))
#obtaining range value 

    clev_range = clev_max - clev_min
#obtaining mean value 

    clev_mean = sum(cleveland)/int(len(cleveland))
#obtaining median value

    clev_median = statistics.median(cleveland)
#obtaining mode value

    clev_mode = statistics.multimode(cleveland)
#obtaining average mode value 

    clev_avgmode = sum(clev_mode)/len(clev_mode)

#tabulating the data 
    print("{}       {}       {}       {}       {}       {}       {}       {}".format("City","Min","Max","Range","Mean","Median","AvgMode","Mode(s)"))
    print("{0}      {1:.2f}      {2:.2f}      {3:.2f}        {4:.2f}        {5:.2f}         {6:.2f}         {7}".format("Boston",bos_min,bos_max,bos_range,bos_mean,bos_median,bos_avgmode,bos_mode))
    print("{0}      {1:.2f}      {2:.2f}      {3:.2f}        {4:.2f}        {5:.2f}         {6:.2f}         {7}".format("Chicago",chi_min,chi_max,chi_range,chi_mean,chi_median,chi_avgmode,chi_mode))
    print("{0}      {1:.2f}      {2:.2f}      {3:.2f}        {4:.2f}        {5:.2f}         {6:.2f}         {7}".format("Clevland",clev_min,clev_max,clev_range,clev_mean,clev_median,clev_avgmode,clev_mode))
if __name__ == '__main__':
    main()
# calibration
code for the calibration at GIGAS Duck installation
This code is a quick code to compute the power observed in the GIGAS duck antenna.
It accounts for calibration data collected prior the installation
and the information collected at the installation.

the calibration and installation data files are in /data
the codes is in /script

in /classes
a class 'calibration' gather the information of the resistor calibration and contains an array of 'detector'
the 'detector' class contains the information related to the installation

in /test
a few test function

in /analysis
script to plot the final results

in /utils
some script to read the files, to convert some basic quantities

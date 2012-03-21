#!/usr/bin/env python
#
# Name: ToSCal.py
# Description: Calculate the ToS and DSCP values for IP Precedence
# or Class Selector argument.
# Author: Brixton Cat
# Date: 10 Mar 2012
# Version: 0.1
# Sintax: ./ToSCalc.py <IP Prec or CS>
#

### Dependencies
import sys

### Functions
def Arguments(decimal):
	""" This function check the introduced argument and call ThreeBits
	function if the value is correct """

	# If not valid value, exit of script
	if decimal < 1 or decimal > 7:
		print "ERROR: %d not valid CS or IP Precedence value" % \
			decimal
		sys.exit(1)
	else:
		ThreeBits(decimal)

def ThreeBits(decimal):
	""" This function convert decimal argument to a 3 bits value and
	check correct lenght of this """

	# Array ['0', 'value']
	bina = bin(decimal).split('b')

	# If less of 3 bits, add 0s to left of binary variable
	if bina[1] < "3":
		rest = 3 - len(bina[1])
		binary = str(0) * rest + bina[1]
	else:
		binary = bina[1]
	
	# Run SixBits functions
	SixBits(decimal, binary)

def EightBits(decimal, binary, dscpb, dscpd):
	""" This function add 0s to right of tosb variable and run Results
	function with all prints values """

	# Rest of 8 and binary lenght
	rest = 8 - len(binary)
	# Type of Service binary value
	tosb = binary + str(0) * rest
	# Type of Service decimal value
	tosd = int(tosb, 2)

	# Call Results function with all values
	Results(decimal, binary, dscpb, dscpd, tosb, tosd)

def Main():
	""" Declare decimal variable and run Arguments function with
	this value """

	# Fisrt argument of the script
	decimal = int(sys.argv[1])
	# Run Arguments functions
	Arguments(decimal)

def Results(decimal, binary, dscpb, dscpd, tosb, tosd):
	""" Prints values relationated with IP Precedence or Class
	Selectors introduced argument"""

	# Header
	print "Value  3bits   DSCP Bin  DSCP   ToS Bin   ToS"
	print "-----  -----   --------  ----   -------   ---"
	# Values
	print "  %d\t%s\t%s\t  %d\t%s  %d" % \
		(decimal, binary, dscpb, dscpd, tosb, tosd)
	
def SixBits(decimal, binary):
	""" This function add 0s to right of dscpb variable and calculate
	their decimal value """

	# DSCP binary value
	dscpb = binary + str(0) * 3
	# DSCP decimal value
	dscpd = int(dscpb, 2)
	
	# Run EightBits function
	EightBits(decimal, binary, dscpb, dscpd)

### Script
Main()

### Exit
# Exit Codes
# 0 -> Normal exit
# 1 -> No valid argument
sys.exit(0)

#EOF
##FVE
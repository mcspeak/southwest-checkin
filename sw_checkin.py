#######################
#	Check me into my flight so my seat doesn't suck
# 	Author: Matthew Speakman
#	Version 1.0 - 11/23/16
#		Base Version
#
#######################

import requests
import webbrowser
import argparse

def runCommandLine(url):
	print("Going to %s" %(url))
	print("I am checking you in via the command line.")

def runBrowser(url):
	print("I am checking you in via the web browser.")
	webbrowser.open_new_tab(url)
########################################################################

argParser = argparse.ArgumentParser(description="Check me into my flight so my seat doesn't suck!")

argParser.add_argument("-w", "--web",action='store_true',help="This will open a browser so you can see the actions.")
argParser.add_argument("-c","--cli",action='store_true',help="This operates on the command line. You will not see the browser.")

args = argParser.parse_args()

url = "https://www.southwest.com/flight/retrieveCheckinDoc.html?int=HOME-BOOKING-WIDGET-AIR-CHECKIN#js-booking-panel-check-in"


if args.cli:
	#Run Command Line
	runCommandLine(url)
elif args.web:
	runBrowser(url)

print("Thank you for checking in using sw_checkin.py. Enjoy your flight! :)")
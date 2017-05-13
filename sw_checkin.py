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
from robobrowser import RoboBrowser

def runCommandLine(url):
	print("Going to %s" %(url))
	print("I am checking you in via the command line.")

def runBrowser(url, confirmationNumber, firstName, lastName):
	print("Checking in %s %s, with a confirmation number of %s." %(firstName, lastName, confirmationNumber))
	success = False
	browser = RoboBrowser(history=True)
	browser.open(url)
	
	itineraryForm = browser.get_form(id="itineraryLookup")
	print("Printing form before values: ")
	print(itineraryForm)
	
	print("Value before: "+ str(itineraryForm['confirmationNumber'].value))
	itineraryForm['confirmationNumber'].value = confirmationNumber
	print("Value after: " + str(itineraryForm['confirmationNumber'].value))
	
	print("Value before: "+ str(itineraryForm['firstName'].value))
	itineraryForm['firstName'].value = firstName
	print("Value after: " + str(itineraryForm['firstName'].value))
	
	print("Value before: "+ str(itineraryForm['lastName'].value))
	itineraryForm['lastName'].value = lastName
	print("Value after: " + str(itineraryForm['lastName'].value))
	
	#Click Submit Button
	#submitInfo = browser.find(id="")
	
	print("Printing form before submit: ")
	print(itineraryForm)
	browser.submit_form(itineraryForm)
	#Check for Second Button
	documentsForm = browser.select("body input [class~=swa-button swa-button_primary]")
	print("documents form:")
	print(documentsForm)
	#Scan for success
	if success:
		print("Thank you for checking in using sw_checkin.py. Enjoy your flight! :)")
	else:
		print("I'm terribly sorry... but I cannot guarantee that you were checked in.")
		print("Please manually check so you get a good seat!")
########################################################################

argParser = argparse.ArgumentParser(description="Check me into my flight so my seat doesn't suck!")

#argParser.add_argument("-w", "--web",action='store_true',help="This will open a browser so you can see the actions.")
argParser.add_argument("-c",help="This is your confirmation number.")
argParser.add_argument("-f",help="This is your first name.")
argParser.add_argument("-l",help="This is your last name.")

args = argParser.parse_args()
print("args are : " + str(args))
url = "https://www.southwest.com/flight/retrieveCheckinDoc.html?int=HOME-BOOKING-WIDGET-AIR-CHECKIN#js-booking-panel-check-in"

if(args.c is not None and args.f is not None and args.l is not None):
	confirmationNumber = args.c
	firstName = args.f
	lastName = args.l
	print(args.f)
	runBrowser(url,confirmationNumber,firstName, lastName)
else:
	print("No arguments! POOR FORM OL' BOY")
	exit(1)
	
exit(0)
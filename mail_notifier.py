#!/usr/bin/env python
import RPi.GPIO as GPIO, imaplib

DEBUG = 1
ERROR = 0

# SETTINGS
USERNAME = "LOGIN"
PASSWORD = "PASSWORD"
SERWER_ADRES = "imap.gmail.com"
PORT_IMAP = "993"

# OFFSET
NEWMAIL_OFFSET = 0

# GPIO SETTINGS
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GREEN_LED = 7
RED_LED = 8

GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)


try:
	
    obj = imaplib.IMAP4_SSL(SERWER_ADRES, PORT_IMAP)
    obj.login(USERNAME, PASSWORD)
    obj.select('Inbox')
    newmails = len(obj.search(None,'UnSeen')[1][0].split())
    
except:
	
    print "!! ERROR (PASSWORD/LOGIN/NETWORK) !!"
    ERROR = 1

if ERROR == 0:
	
	if DEBUG:
		print "New mails: ", newmails

	if newmails > NEWMAIL_OFFSET:
		GPIO.output(GREEN_LED, True)
		GPIO.output(RED_LED, False)

	else:	
		GPIO.output(GREEN_LED, False)
		GPIO.output(RED_LED, True)
		

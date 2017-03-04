#!/usr/bin/python
import RPi.GPIO as GPIO
import time, datetime
import blockspring

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.output(4, True)
time.sleep(1)
GPIO.output(4, False)
GPIO.cleanup()


#print blockspring.runParsed("post-message-to-slack", { "channel": "#house", "message": "Garage door toggled @ " + 
#str(datetime.datetime.now()),
#  "slack_token": "xoxp-4423394221-4423394223-7884479975-dd8e4e",
#  "icon_url":"http://thumbs.dreamstime.com/t/cute-robot-cartoon-character-cool-avatar-vector-eps-30737294.jpg",
#  "username":"BillerBot"
#}
#).params

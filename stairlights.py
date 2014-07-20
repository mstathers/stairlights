#!/usr/bin/env python

import time
import datetime
import sys
import logging
import RPi.GPIO as io
io.setmode(io.BCM)
io.setwarnings(False)

logging.basicConfig(filename='/var/log/stairs.log',
    format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO)


# OUTPUT LED
io.setup(17, io.OUT)
io.output(17, io.LOW)
#INPUT Upstairs
io.setup(18, io.IN)
#INPUT Downstairs
io.setup(23, io.IN)

while 1:
    try:
        # Upstairs
        if io.input(18):
            logging.info('Going downstairs')
            io.output(17, io.HIGH)
            time.sleep(15)
            io.output(17, io.LOW)

        # Downstairs
        if io.input(23):
            logging.info('Going upstairs')
            io.output(17, io.HIGH)
            time.sleep(15)
            io.output(17, io.LOW)

        time.sleep(0.1)

    except KeyboardInterrupt:
        io.cleanup()
        sys.exit()

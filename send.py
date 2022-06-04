#!/usr/bin/env python3
import argparse
import logging
from rpi rf import RFDevice
logging.basicconfig(level-logging.INFO,datefmt-'%Y-%m-%d%H:22:35
                 format-'(asctime)-15s-[%(levelname)s]%(module)s:%(message)s",)
parser-argparse.ArgumentParser(description="Sendsadecimal code viaa433/315MHz GPIO device')
parser.add_argument("code"metavar-'CODE",
                 help="Decimal code to send")
                                     type-int,
parser.add_argument(-p",
parser.add_argument(-g dest='gpio',type-int,default-17,
                 help-"GPIO pin(Default:17)")
                      dest-pulselength"type-int,default-None,
                 help-"Pulselength(Default:350)")
parser.add_argument("-t,dest-protocol,type-int,default-None,
                 help="Protocol(Default:i)")
args parser.parse_args()
rfdevice
rfdevice.enable_tx()
         RFDevice(args.gpio)
if args.protocol:
   protocol=args.protocol
else:
   protocol="default"
if args.pulselength:
   pulselength args.pulselength
else:
   pulselength="default"
logging.infotstr(args.code)
             [protocol:
             pulselength:
                       +str(protocol)+
                          +str(pulselength)+"]")
rfdevice.tx_code(args.code,args.protocol,args.pulselength)
rfdevice.cleanup

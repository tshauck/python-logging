#pylint: skip-file

from __future__ import print_function

import sys

import logging.config
import yaml
import time

#with open('./fluentd-logger.yaml') as fd:
    #conf = yaml.load(fd)

#logging.config.dictConfig(conf['logging'])

i = 0
while True:
    print(i, file=sys.stderr)
    #logging.debug("In debug")
    #logging.info("In info")
    #logging.warning("In warn")
    #logging.error("In info")
    time.sleep(5)
    i = i + 1

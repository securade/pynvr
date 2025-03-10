import os
import logging

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def subFolderNameForDtsGeneratorFunc(dts):
    return "{:04}-{:02}-{:02}".format(dts.year, dts.month, dts.day)

#######################
#   camera settings   #
#######################
# Here you can specify connection string to camera
# Examples:
# cam = "rtsp://login:password@ip:port/stream_url" #connection to camera via RTSP with credentials
cam = 0  # use local camera

#####################
#   logs settings   #
#####################
# folder where logs will be stored
LOG_FILE_PATH = os.path.normpath(os.path.join(APP_ROOT, "./logs/vmd_dvr.log"))

# log level for logging
APP_LOG_LEVEL = logging.DEBUG

# max size for log file in bytes
MAIN_LOG_FILE_MAX_SIZE = 1024 * 1024 * 32

# max count for log files
LOG_BACKUPS_COUNT = 20

# log format
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# send copy of all log messages to console
LOG_TO_CONSOLE = True

#################################
#   motion detection settings   #
#################################
INITIAL_WAIT_INTERVAL_BEFORE_MOTION_DETECTION_SECS = 3600
MINIMAL_MOTION_DURATION = 0

##########################
#   recording settings   #
##########################
PRE_ALARM_RECORDING_SECONDS = 0
PATH_FOR_VIDEO = "./video"
subFolderNameGeneratorFunc = subFolderNameForDtsGeneratorFunc

############################################
#   quality and codec settings for video   #
############################################

# scaleFrameTo = (500, 500) #(width, height)
scaleFrameTo = (640, 480)

# codec for output files
FOURCC_CODEC = "avc1"
OUTPUT_FILES_EXTENSION = ".mp4"
OUTPUT_FRAME_RATE = 15

# loading machine specific configuration
if os.path.exists(os.path.join(APP_ROOT, "machine_specific_configuration.py")):
    from machine_specific_configuration import *  # noqa

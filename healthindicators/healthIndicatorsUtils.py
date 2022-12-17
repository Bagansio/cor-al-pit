# Symbols for calculateHealthIndicators functions #
PERCENTAGE = "%" 
MILLIGRAMS = "mg"
MICROLITER = "μL"
MICROLITERPERMINUTE = "μL/min"

# Minimum indicators to have a unhealthy heart
MINIMUM_INDICATORS_UNHEALTHY_HEART = 3

# Intervals for compareHealthIndicators #

# BW Intervals
BW_POSITIVEINTERVAL = 25.7+3.6
BW_NEGATIVEINTERVAL = 25.7-3.6

# HR Intervals
HR_POSITIVEINTERVAL = 535+75
HR_NEGATIVEINTERVAL = 535-75

# LV mass Intervals
LVMASS_POSITIVEINTERVAL = 96+18
LVMASS_NEGATIVEINTERVAL = 96-18

# LVPWd mass Intervals
LVPWD_POSITIVEINTERVAL = 0.79+0.22
LVPWD_NEGATIVEINTERVAL = 0.79-0.22

# LVPWs mass Intervals
LVPWS_POSITIVEINTERVAL = 1.12+0.33
LVPWS_NEGATIVEINTERVAL = 1.12-0.33

# LVIDs Intervals
LVIDS_POSITIVEINTERVAL = 2.20+0.50
LVIDS_NEGATIVEINTERVAL = 2.20-0.50

# LVIDd Intervals
LVIDD_POSITIVEINTERVAL = 3.69+0.41
LVIDD_NEGATIVEINTERVAL = 3.69-0.41

# IVSd Intervals
IVSD_POSITIVEINTERVAL = 0.71+0.15
IVSD_NEGATIVEINTERVAL = 0.71-0.15

# IVSs Intervals
IVSS_POSITIVEINTERVAL = 0.97+0.19
IVSS_NEGATIVEINTERVAL = 0.97-0.19

# LVESV Intervals
LVESV_POSITIVEINTERVAL = 19.35+11.30
LVESV_NEGATIVEINTERVAL = 19.35-11.30

# LVEDV Intervals
LVEDV_POSITIVEINTERVAL = 57.7+16.5
LVEDV_NEGATIVEINTERVAL = 57.7-16.5

#EF Intervals
EF_POSITIVEINTERVAL = 71+11
EF_NEGATIVEINTERVAL = 71-11

#FS Intervals
FS_POSITIVEINTERVAL = 43+9
FS_NEGATIVEINTERVAL = 43-9

#SV Intervals
SV_POSITIVEINTERVAL = 35.1+8.5
SV_NEGATIVEINTERVAL = 35.1-8.5

#CO Intervals
CO_POSITIVEINTERVAL = 17.7+3.8
CO_NEGATIVEINTERVAL = 17.7-3.8


# PRINT UTILS
NORMAL_TEXT = "\033[0m"
BOLD_TEXT = "\033[1m"
RED_TEXT = "\x1b[1;31m"
GREEN_TEXT = "\x1b[1;32m"



def checkInterval(negativeInterval, positiveInterval, value, name):
    negativeInterval = round(negativeInterval, 2)
    positiveInterval = round(positiveInterval, 2)
    healthy = True
    pr = BOLD_TEXT + str(name) + NORMAL_TEXT + " value and interval : "

    if value < negativeInterval:
        pr = pr+RED_TEXT+str(value)+NORMAL_TEXT
        healthy = False

    pr = pr + " " + str(negativeInterval)
    
    if value >= negativeInterval and value <= positiveInterval:
        pr = pr + " "+ (GREEN_TEXT+str(value)+NORMAL_TEXT)

    pr = pr + " " + str(positiveInterval)

    if value > positiveInterval:
        pr = pr + " "+ (RED_TEXT+str(value)+NORMAL_TEXT)
        healthy = False
    
    print(pr)

    if(healthy): print("VALUE IS" + GREEN_TEXT+ " HEALTHY!"+NORMAL_TEXT+"\n") 
    else: print("VALUE IS" + RED_TEXT+ " UNHEALTHY!"+NORMAL_TEXT+"\n") 
    

    return healthy










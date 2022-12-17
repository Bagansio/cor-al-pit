import healthIndicatorsUtils as HIUtils
import dataManagerUtils as DMUtils

####### COMPARATORS: 3 OR MORE = UNHEALTHY HEART ####### 

# BW (g) 25.7+-3.6
def compareBW(BW):
    """
    Compare if BW (g) 25.7+-3.6

    TRUE = Healthy (between the intervals) \n
    FALSE = Unhealthy (not between the invervals)
    """
    return HIUtils.checkInterval(HIUtils.BW_NEGATIVEINTERVAL, HIUtils.BW_POSITIVEINTERVAL, BW, "BW")


# HR(b.p.m) 535+-75
def compareHR(HR):
    """
    Compare if HR(b.p.m) 535+-75

    TRUE = Healthy (between the intervals) \n
    FALSE = Unhealthy (not between the invervals)
    """
    return HIUtils.checkInterval(HIUtils.HR_NEGATIVEINTERVAL, HIUtils.HR_POSITIVEINTERVAL, HR, "HR")


# LV mass (mg) 96+-18
def compareLV_mass(LV_mass):
    """
    Compare if LV mass (mg) 96+-18

    TRUE = Healthy (between the intervals) \n
    FALSE = Unhealthy (not between the invervals)
    """
    return HIUtils.checkInterval(HIUtils.LVMASS_NEGATIVEINTERVAL, HIUtils.LVMASS_POSITIVEINTERVAL, LV_mass, "LV_mass")

#LVPWd (mm) 0.79+-0.22
def compareLVPWd(LVPWd):
    """
    Compare if LVPWd (mm) 0.79+-0.22

    TRUE = Healthy (between the intervals) \n
    FALSE = Unhealthy (not between the invervals)
    """
    return HIUtils.checkInterval(HIUtils.LVPWD_NEGATIVEINTERVAL, HIUtils.LVPWD_POSITIVEINTERVAL, LVPWd, "LVPWd")

#LVPWs (mm) 1.12+-0.33
def compareLVPWs(LVPWs):
    """
    Compare if LVPWs (mm) 1.12+-0.33

    TRUE = Healthy (between the intervals) \n
    FALSE = Unhealthy (not between the invervals)
    """
    return HIUtils.checkInterval(HIUtils.LVPWS_NEGATIVEINTERVAL, HIUtils.LVPWS_POSITIVEINTERVAL, LVPWs, "LVPWs")


#LVIDs (mm) 2.20+-0.50
def compareLVIDs(LVIDs):
    """
    Compare if LVIDs (mm) 2.20+-0.50

    TRUE = Healthy (between the intervals) \n
    FALSE = Unhealthy (not between the invervals)
    """
    return HIUtils.checkInterval(HIUtils.LVIDS_NEGATIVEINTERVAL, HIUtils.LVIDS_POSITIVEINTERVAL, LVIDs, "LVIDs")


#LVIDd (mm) 3.69+-0.41
def compareLVIDd(LVIDd):
    """
    Compare if LVIDd (mm) 3.69+-0.41

    TRUE = Healthy (between the intervals) \n
    FALSE = Unhealthy (not between the invervals)
    """
    return HIUtils.checkInterval(HIUtils.LVIDD_NEGATIVEINTERVAL, HIUtils.LVIDD_POSITIVEINTERVAL, LVIDd, "LVIDd")


#IVSd (mm) 0.71+-0.15
def compareIVSd(IVSd):
    """
    Compare if IVSd (mm) 0.71+-0.15

    TRUE = Healthy (between the intervals) \n
    FALSE = Unhealthy (not between the invervals)
    """
    return HIUtils.checkInterval(HIUtils.IVSD_NEGATIVEINTERVAL, HIUtils.IVSD_POSITIVEINTERVAL, IVSd, "IVSd")


#IVSs (mm) 0.97+-0.19
def compareIVSs(IVSs):
    """
    Compare if IVSs (mm) 0.97+-0.19

    TRUE = Healthy (between the intervals) \n
    FALSE = Unhealthy (not between the invervals)
    """
    return HIUtils.checkInterval(HIUtils.IVSS_NEGATIVEINTERVAL, HIUtils.IVSS_POSITIVEINTERVAL, IVSs, "IVSs")


#LVESV (μL) 19.35+-11.30
def compareLVESV(LVESV):
    """
    Compare if LVESV (μL) 19.35+-11.30

    TRUE = Healthy (between the intervals) \n
    FALSE = Unhealthy (not between the invervals)
    """
    return HIUtils.checkInterval(HIUtils.LVESV_NEGATIVEINTERVAL, HIUtils.LVESV_POSITIVEINTERVAL, LVESV, "LVESV")


#LVEDV (μL) 57.7+-16.5
def compareLVEDV(LVEDV):
    """
    Compare if LVEDV (μL) 57.7+-16.5

    TRUE = Healthy (between the intervals) \n
    FALSE = Unhealthy (not between the invervals)
    """
    return HIUtils.checkInterval(HIUtils.LVEDV_NEGATIVEINTERVAL, HIUtils.LVEDV_POSITIVEINTERVAL, LVEDV, "LVEDV")


#EF(%) 71+-11
def compareEF(EF):
    """
    Compare if EF(%) 71+-11

    TRUE = Healthy (between the intervals) \n
    FALSE = Unhealthy (not between the invervals)
    """
    return HIUtils.checkInterval(HIUtils.EF_NEGATIVEINTERVAL, HIUtils.EF_POSITIVEINTERVAL, EF, "EF")


#FS(%) 43+-9
def compareFS(FS):
    """
    Compare if FS(%) 43+-9

    TRUE = Healthy (between the intervals) \n
    FALSE = Unhealthy (not between the invervals)
    """
    return HIUtils.checkInterval(HIUtils.FS_NEGATIVEINTERVAL, HIUtils.FS_POSITIVEINTERVAL, FS, "FS")


#SV(μL) 35.1+-8.5
def compareSV(SV):
    """
    Compare if SV(μL) 35.1+-8.5

    TRUE = Healthy (between the intervals) \n
    FALSE = Unhealthy (not between the invervals)
    """
    return HIUtils.checkInterval(HIUtils.SV_NEGATIVEINTERVAL, HIUtils.SV_POSITIVEINTERVAL, SV, "SV")


#CO(mL/min) 17.7+-3.8
def compareCO(CO):
    """
    Compare if CO(mL/min) 17.7+-3.8

    TRUE = Healthy (between the intervals) \n
    FALSE = Unhealthy (not between the invervals)
    """
    return HIUtils.checkInterval(HIUtils.CO_NEGATIVEINTERVAL, HIUtils.CO_POSITIVEINTERVAL, CO, "CO")

def compareAll(BW, HR, LV_mass, LVPWd, LVPWs, LVIDs, LVIDd, IVSd, IVSs, LVESV, LVEDV, EF, FS, SV, CO):
    """
    Compare all the health indicators, if number of unhealthy indicators are 3 or more the heart is unhealthy.

    Return: \n
    TRUE = Healthy heart // FALSE = Unhealthy heart \n
    A list with all the comparations done and if the intervals are healthy or unhealthy
    """
    unhealthyCont = 0
    healthyCont = 0 

    if(compareBW(BW)): healthyCont = healthyCont + 1
    else: unhealthyCont = unhealthyCont +1

    if compareHR(HR): healthyCont = healthyCont + 1
    else: unhealthyCont = unhealthyCont +1
    
    if compareLV_mass(LV_mass): healthyCont = healthyCont + 1
    else: unhealthyCont = unhealthyCont +1

    if compareLVPWd(LVPWd): healthyCont = healthyCont + 1
    else: unhealthyCont = unhealthyCont +1

    if compareLVPWs(LVPWs): healthyCont = healthyCont + 1
    else: unhealthyCont = unhealthyCont +1

    if compareLVIDs(LVIDs): healthyCont = healthyCont + 1
    else: unhealthyCont = unhealthyCont +1

    if compareLVIDd(LVIDd): healthyCont = healthyCont + 1
    else: unhealthyCont = unhealthyCont +1

    if compareIVSd(IVSd): healthyCont = healthyCont + 1
    else: unhealthyCont = unhealthyCont +1

    if compareIVSs(IVSs): healthyCont = healthyCont + 1
    else: unhealthyCont = unhealthyCont +1

    if compareLVESV(LVESV): healthyCont = healthyCont + 1
    else: unhealthyCont = unhealthyCont +1

    if compareLVEDV(LVEDV): healthyCont = healthyCont + 1
    else: unhealthyCont = unhealthyCont +1

    if compareEF(EF): healthyCont = healthyCont + 1
    else: unhealthyCont = unhealthyCont +1

    if compareFS(FS): healthyCont = healthyCont + 1
    else: unhealthyCont = unhealthyCont +1

    if compareSV(SV): healthyCont = healthyCont + 1
    else: unhealthyCont = unhealthyCont +1

    if compareCO(CO): healthyCont = healthyCont + 1
    else: unhealthyCont = unhealthyCont +1

    print("TOTAL HEALTHY INDICATORS: "+ str(healthyCont))
    print("TOTAL UNHEALTHY INDICATORS: "+ str(unhealthyCont))

    if(unhealthyCont >= HIUtils.MINIMUM_INDICATORS_UNHEALTHY_HEART):
        print("PATIENT HAS A"+HIUtils.RED_TEXT+" UNHEALTHY"+HIUtils.NORMAL_TEXT+" HEART" )
    else: print("PATIENT HAS A"+HIUtils.GREEN_TEXT+" HEALTHY"+HIUtils.NORMAL_TEXT+" HEART" )

    HIUtils.healthInformationToExcel(BW, HR, LV_mass, LVPWd, LVPWs, LVIDs, LVIDd, IVSd, IVSs, LVESV, LVEDV, EF, FS, SV, CO)




compareAll(1,500,1,1,1,1.8,3.5,0.7,1,12,50,61,35,30,15)


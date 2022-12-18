import healthIndicatorsUtils as HIUtils
import compareHealthIndicators as compareHI
####### CALCULATIONS TO KNOW THE HEALTH INDICATORS #######

# LVESV = [7/(2.4+LVIDs)]*(LVIDs^3)
def calculateLVESV(LVIDs):
    """
    CALCULATE LVESV = [7/(2.4+LVIDs)]*(LVIDs^3)

    Returns LVESV value and it symbol (μL)
    """
    LVESVCalculation = (7/(2.4+LVIDs))*(LVIDs**3)

    return {LVESVCalculation, HIUtils.MICROLITER}

# LVEDV = [7/(2.4+LVIDd)]*(LVIDd^3)
def calculateLVEDV(LVIDd):
    """
    CALCULATE LVEDV = [7/(2.4+LVIDd)]*(LVIDd^3)

    Returns LVEDV value and it symbol (μL)
    """
    LVEDVCalculation = (7/(2.4+LVIDd))*(LVIDd**3)
    return {LVEDVCalculation, HIUtils.MICROLITER}

# FS(%) = (LVIDd-LVIDs)/LVIDd*100
def calculateFS(LVIDd, LVIDs):
    """
    CALCULATE FS(%) = (LVIDd-LVIDs)/LVIDd*100

    Returns FS value and it symbol (%)
    """
    FSCalculation = ((LVIDd-LVIDs)/LVIDd)*100
    return {FSCalculation, HIUtils.PERCENTAGE}

# EF(%) = (LVEDV-LVESV)/LVEDV*100
def calculateEF(LVEDV, LVESV):
    """
    CALCULATE EF(%) = (LVEDV-LVESV)/LVEDV*100

    Returns EF value and it symbol (%)
    """
    EFCalculation = ((LVEDV-LVESV)/LVEDV)*100
    return {EFCalculation, HIUtils.PERCENTAGE}

# LV mass (mg) = 1.04[(LVIDd+LVAWd+LVPWd)^3-(LVIDd^3)]*0.8+0.6
def calculateLV_mass(LVIDd, LVAWd, LVPWd):
    """
    # CALCULATE LV mass (mg) = 1.04[(LVIDd+LVAWd+LVPWd)^3-(LVIDd^3)]*0.8+0.6

    Returns LV mass value and it symbol (mg)

    """
    LV_massCalculation = 1.04((((LVIDd+LVAWd+LVPWd)**3)-(LVIDd**3))*0.8)+0.6
    return {LV_massCalculation, HIUtils.MILLIGRAMS}

# Stroke volume, SV (μL) = (LVEDV-LVESV)
def calculateStroke_volume(LVEDV, LVESV):
    """
    CALCULATE Stroke volume: SV (μL) = (LVEDV-LVESV)

    Returns Stroke volume value and it symbol (μL)

    """
    SVCalculation = (LVEDV-LVESV)
    return {SVCalculation, HIUtils.MICROLITER}

# Cardiac output : CO(μL/min) = SV*HR
def calculateCardiac_output(SV, HR):
    """
    CALCULATE Cardiac output : CO(μL/min) = SV*HR
    
    Returns Cardiac output and it symbol (μL/min)

    """
    COCalculation = SV*HR
    return {COCalculation, HIUtils.MICROLITERPERMINUTE}

# Relative wall thickness: RWT = (LVPWd+LVIVSd)/(LVIDd)
def calculateRelative_wall_thickness(LVPWd, LVIVSd, LVIDd):
    """
    Relative wall thickness: RWT = (LVPWd+LVIVSd)/(LVIDd)
    
    Returns Relative wall thickness value

    """
    RWTCalculation = (LVPWd+LVIVSd)/(LVIDd)
    return RWTCalculation

def calculateAll(IVSd, IVSs, LVIDd, LVIDs, LVPWd, LVPWs, LVAWd, LVAWs, HR):
    # MISSING VALUES

    LVESV_value = calculateLVESV(LVIDs)
    LVEDV_value = calculateLVEDV(LVIDd)
    FS_value = calculateFS(LVIDd, LVIDs)
    EF_value = calculateEF(LVEDV_value,LVESV_value)
    LV_mass_value = calculateLV_mass(LVIDd, LVAWd, LVPWd)
    SV_value = calculateStroke_volume(LVEDV_value, LVESV_value)
    CO_value = calculateCardiac_output(SV_value, HR)
    RWT_value = calculateRelative_wall_thickness(LVPWd,IVSd,LVIDd)
    

    compareHI.compareAll(25, HR, LV_mass_value, LVPWd, LVPWs, LVIDs, LVIDd, IVSd, IVSs, LVESV_value, LVEDV_value, EF_value, FS_value, SV_value, CO_value)
    return







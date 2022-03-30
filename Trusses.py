# **************************************************************************************************************************************************************************************************** #
# ********************************************************************** 8.	Verification of force transmitted by members of given truss. ************************************************************* #
# **************************************************************************************************************************************************************************************************** #
# -@ AmiLab


'''
Note-
    - **DATA VALIDATION EXCLUDED FOR BEING CHECKED AT THE TIME OF DATA INPUT**
    - All Units of like Physical Quantities are assumed to be in same unit system.
    - All Testings have been logged into the terminal for future debuggings.
'''


# ********************************************************************** Argument / Variable Declaration (for Testing purposes) ********************************************************************** #



n = 5                                                                        # For storing the Number of Observations
N = 3                                                                        # For storing the Number of member(s) of the Truss with Sping balance attached to them for measuring their compressive or tensile forces
ks = [21400, 20800, 17200]                                                   # For storing the values of the Spring Constants of the 3 Spring balances used for calculating the forces
divs = [16, 13, 9]                                                           # For storing the Coinciding divions of the Spring balances
lcs = [0.01, 0.01, 0.01]                                                     # For storing the the Least Counts of the 'N'(= 3 in this case) member(s) of the Truss
theo_forces_readings = [3418.41, 2694.88, 1549.11]                           # For storing the the Least Counts of the 'N'(= 3 in this case) member(s) of the Truss



# **************************************************************************************** Section ends here ***************************************************************************************** #


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #



# **************** Verifying the Forces transmitted by the Members of the given truss, by calculating the minimized Error Difference between the theoretical and experimental readings *************** #



def calScaleDeflection(divs, lcs):                                                                  # For Calculating the Scale Deflection Readings fro the Conciding Division and the Least Counts(LCs) of the Spring Balances' scales
    return list(map(lambda div, lc: div * lc, divs, lcs))

# Testing-
scale_deflects = calScaleDeflection(divs, lcs)
print('Dial Gauge Deflection(s) =', end = ' ')
print(*scale_deflects, sep = ', ')


def calExperimentalForceReadings(scale_deflects, ks):                                               # For Calculating the Experimental Readings from the Scale Deflections and Spring Constants of the Spring Balances used
    return list(map(lambda scale_deflect, k: scale_deflect * k, scale_deflects, ks))

# Testings-
exp_forces_readings = calScaleDeflection(scale_deflects, ks)
print('Experimental Force Reading(s) =', end = ' ')
print(*exp_forces_readings, sep = ', ')

print('Theoretical Force Reading(s) =', end = ' ')
print(*theo_forces_readings, sep = ', ')



def calSignedError(theo_forces_readings, exp_forces_readings):                                        # For Calculating the Signed Error in the Theoretical and Experimental Readings
    return list(map(lambda theo, exp: theo - exp, theo_forces_readings, exp_forces_readings))

# Testing-
signed_err = calSignedError(theo_forces_readings, exp_forces_readings)
print('Signed Error(s) =', end = ' ')
print(*signed_err, sep = ', ')


def calAbsoluteError(signed_err):                                                                     # For Calculating the Absolute Error in the Theoretical and Experimental Readings
    return list(map(lambda err: abs(err), signed_err))

# Testing-
abs_err = calAbsoluteError(signed_err)
print('Absolute Error(s) =', end = ' ')
print(*abs_err, sep = ', ')

def calRelativeError(abs_err, Av_theoretical):                                                        # For Calculating the Relative Error in the Theoretical and Experimental Readings
    return list(map(lambda err, theo: abs(err / theo), abs_err, Av_theoretical))

# Testing-
rel_err = calRelativeError(abs_err, theo_forces_readings)
print('Relative Error(s) =', end = ' ')
print(*rel_err, sep = ', ')


def calPercentageError(rel_err):                                                                      # For Calculating the Percentage Error in the Theoretical and Experimental Readings
    return list(map(lambda rel: abs(rel) * 100, rel_err))

# Testing-
signed_err = calPercentageError(rel_err)
print('Percentage Error(s) =', end = ' ')
print(*list(map(lambda err: str(err) + '%', signed_err)), sep = ', ')



# ********************************************************************************* Section ends here ************************************************************************************************ #


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #





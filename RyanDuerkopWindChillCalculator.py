
#This program allows a user to estimate the perceived temperature based off of the actual air temperature and wind speed.
#The program is able to convert the wind chill into F and mph.
# while doing that it uses the noaa formula to validate those numbers.
# once completed it is converted into F and C. 



import sys


def c_to_f(c: float) -> float:
    "Convert Celsius to Fahrenheit."
    return c * 1.8 + 32.0

def f_to_c(f: float) -> float:
    "Convert Fahrenheit to Celsius."
    return (f - 32.0) / 1.8

def mph_to_kmh(mph: float) -> float:
    "Convert miles per hour to kilometers per hour."
    return 1.609 * mph

def kmh_to_mph(kmh: float) -> float:
    "Convert kilometers per hour to miles per hour."
    return kmh / 1.609

def wind_chill_f(T_f: float, S_mph: float) -> float:
    "Compute wind chill in F using the NOAA formula."
    return 35.74 + 0.6215*T_f - 35.75*(S_mph**0.16) + 0.4275*T_f*(S_mph**0.16)

def time_to_frostbite_f(W_f: float):
    "Return label/minutes based on wind chill F."
    if W_f < -60:
        return ("Frostbite risk: EXTREME", 5)
    elif W_f < -35:
        return ("Frostbite risk: HIGH", 10)
    elif W_f < -17:
        return ("Frostbite risk: ELEVATED", 30)
    else:
        return ("Frostbite unlikely at this wind chill.", None)

print("Wind Chill Calculator")

temp_unit = input("Enter temperature unit (F/C): ").strip().upper()
if temp_unit not in ("F", "C"):
    print("Invalid temperature unit. Must be 'F' or 'C'.")
    sys.exit()

try:
    temp_value = float(input("Enter temperature value: ").strip())
except ValueError:
    print("Temperature must be a number.")
    sys.exit()

wind_unit = input("Enter wind speed unit (MPH/KPH): ").strip().upper()
if wind_unit not in ("MPH", "KPH"):
    print("Invalid wind speed unit. Must be 'MPH' or 'KPH'.")
    sys.exit()

try:
    wind_value = float(input("Enter wind speed value: ").strip())
    if wind_value < 0:
        print("Wind speed cannot be negative.")
        sys.exit()
except ValueError:
    print("Wind speed must be numeric.")
    sys.exit()

T_f = c_to_f(temp_value) if temp_unit == "C" else temp_value
S_mph = kmh_to_mph(wind_value) if wind_unit == "KPH" else wind_value  

if S_mph <= 3:
    W_f = T_f
    message = "No wind chill effect (wind speed of ≤ 3 mph)"
elif T_f >= 50:
    W_f = T_f
    message = "No wind chill effect (50 F)"
else:
    W_f = wind_chill_f(T_f, S_mph)
    message = "Calculate wind chill by using noaa formula"

W_c = f_to_c(W_f)

risk_label, minutes = time_to_frostbite_f(W_f)
frostbite_line = (
    risk_label if minutes is None
    else f"{risk_label} Estimated time to frostbite: {minutes} minutes."
)

print("\n" + "=" * 44)
print("WIND CHILL RESULTS")
print("=" * 44)
print(f"Air Temperature: {T_f:.2f} F")
print(f"Wind Speed:      {S_mph:.2f} mph")
print("-" * 44)
print(f"Wind Chill:      {W_f:.2f} F  |  {W_c:.2f} C")
print("-" * 44)
print(frostbite_line)
print(message)

print("=" * 44)

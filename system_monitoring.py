def GetCoreTemperature():
    import psutil
    return ((str(psutil.sensors_temperatures()["coretemp"][0].current))+" C")

def GetBatteryVoltage():
    volatge_file = open("/sys/class/power_supply/BAT0/hwmon2/in0_input", "r")
    voltage = f"{(int(volatge_file.read())/1000):.2f} V"
    return voltage
def GetCoreVoltage():
    import os
    Core_Voltage = os.popen("sudo dmidecode --type processor | grep Voltage | cut -d: -f2")
    return f"{Core_Voltage.read().strip()}"
def GetBatteryPower():
    volatge_file = open("/sys/class/power_supply/BAT0/hwmon2/in0_input", "r")
    current_file = open("/sys/class/power_supply/BAT0/current_now", "r")
    voltage = int(volatge_file.read())/1000
    current = int(current_file.read())/1000
    power = voltage*current/1000
    return "{:.2f} W".format(power)

def GetMemorySpeed():
    import os
    output = os.popen("sudo dmidecode -t memory | grep -i -m1 '^[[:space:]]speed' | cut -d: -f2 | cut -d\" \" -f2")
    return f"{output.read().strip()} Mhz"

print(GetCoreTemperature())
print(GetBatteryVoltage())
print(GetBatteryPower())
print(GetMemorySpeed())
print(GetCoreVoltage())

import os
import platform
import re
def GetCoreTemperature():
    import psutil
    return ((str(psutil.sensors_temperatures()["coretemp"][0].current))+" C")


def GetBatteryVoltage():
    volatge_file = open("/sys/class/power_supply/BAT0/hwmon2/in0_input", "r")
    voltage = f"{(int(volatge_file.read())/1000):.2f} V"
    return voltage
def GetCoreVoltage():
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
    output = os.popen("sudo dmidecode -t memory | grep -i -m1 '^[[:space:]]speed' | cut -d: -f2 | cut -d\" \" -f2")
    return f"{output.read().strip()} Mhz"

def GetCpuModel():
    raw_cpu_model = os.popen("cat /proc/cpuinfo | grep 'model name' | cut -d: -f2")
    return raw_cpu_model.read().splitlines()[0].strip()
def GetCpuCores():
    cores = set()
    raw_data = os.popen("cat /proc/cpuinfo").readlines()
    physical_id = None
    core_id = None
    for line in raw_data:
        if line.startswith('physical id'):
            physical_id = line.split(':')[1].strip()
        if line.startswith('core id'):
            core_id = line.split(':')[1].strip()
        if physical_id and core_id:
            cores.add((physical_id, core_id))
            physical_id = None
            core_id = None
    return len(cores)
def GetCpuThreads():
    raw_data = os.popen("cat /proc/cpuinfo | grep 'processor' | wc -l")
    return raw_data.read()

def GetCacheSize():
    cache_size= os.popen("cat /proc/cpuinfo | grep 'cache size' | cut -d: -f2")
    return cache_size.read().splitlines()[0].strip()
def GetMotherboardModel():
    mobo_name = os.popen("cat /sys/devices/virtual/dmi/id/board_name")
    return mobo_name.read().strip()

def GetMotherboardVendor():
    mobo_vendor = os.popen("cat /sys/devices/virtual/dmi/id/board_vendor")
    return mobo_vendor.read().strip()

def GetBiosInfo():

    bios_info = os.popen('sudo /usr/sbin/dmidecode -t bios')
    bios_output = bios_info.read()

    bios_info = {"Vendor": None,"Version": None,"Release Date": None,"Address": None,"Runtime Size": None,"ROM Size": None}

    patterns = {"Vendor": r"Vendor:\s*(.*)", "Version": r"Version:\s*(.*)","Release Date": r"Release Date:\s*(.*)",
        "Address": r"Address:\s*(.*)","Runtime Size": r"Runtime Size:\s*(.*)","ROM Size": r"ROM Size:\s*(.*)"}

    for line in bios_output.splitlines():
        for key, pattern in patterns.items():
            match = re.search(pattern, line)
            if match:
                bios_info[key] = match.group(1)

    return bios_info

def GetOsInfo():
    
    os_info = {"Name": None,"Version": None}

    os_fullinfo = os.popen('cat /etc/os-release')
    for line in os_fullinfo:
        if line.startswith('NAME='):
            os_info["Name"] = line.split('=')[1].strip().replace('"', '')
        elif line.startswith('VERSION='):
            os_info["Version"] = line.split('=')[1].strip().replace('"', '')

    return os_info



print(GetCoreTemperature())
print(GetBatteryVoltage())
print(GetBatteryPower())
print(GetMemorySpeed())
print(GetCoreVoltage())
print(GetBiosInfo())
print(GetOsInfo())
print(GetCpuModel())
print(GetCpuCores())
print(GetCpuThreads())
print(GetMotherboardModel())
print(GetMotherboardVendor())
print(GetCacheSize())

import os
import platform
import re
import time
import multiprocessing
import psutil

mem_total_size="{:.2f} GB".format(int(os.popen("cat /proc/meminfo | awk ' NR==1 {print $2}' ").read().strip())/1024/1024) 


def GetCoreTemperature():
    import psutil
    return ((str(psutil.sensors_temperatures()["coretemp"][0].current))+" C")

def GetCpuUsage():
    return psutil.cpu_percent()

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



def GetCpuModel():
    res = os.popen("cat /proc/cpuinfo | grep 'model name' | cut -d: -f2")
    return res.read().splitlines()[0].strip()
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

def GetMemoryInfo_Static():
    global mem_total_size
    mem_info_static_dic = {}
    mem_info_static_dic["Type"] = os.popen("sudo dmidecode --type memory | awk ' /Type/  {print $2}' | sed -n \"2p\" ").read().strip()
    mem_info_static_dic["Speed"] = "{} Mhz".format(os.popen("sudo dmidecode -t memory | grep -i -m1 '^[[:space:]]speed' | cut -d: -f2 | cut -d\" \" -f2").read().strip()) 
    mem_info_static_dic["Channel"] =os.popen("sudo dmidecode --type memory | awk ' /Devices/  {print $4}' ").read().strip()
    mem_info_static_dic["Total_Size"]=mem_total_size
    return mem_info_static_dic

def GetMemoryInfo_Dynamic():
    global mem_total_size
    mem_info_dynamic_dic = {}
    mem_info_dynamic_dic["Available_Size"]="{:.2f} GB".format(int(os.popen("cat /proc/meminfo | awk ' NR==3 {print $2}' ").read().strip())/1024/1024) 
    mem_info_dynamic_dic["Usage"]="{:.2f} %".format((float(mem_total_size.split()[0]) - float(mem_info_dynamic_dic["Available_Size"].split()[0]))/ float(mem_total_size.split()[0]) * 100) 
    return mem_info_dynamic_dic


def StressCpu():
    while True:
        counter = 0
        for i in range(30000000):
            counter += i

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()

    processes = []

    for i in range(num_cores):
        process = multiprocessing.Process(target=StressCpu)
        processes.append(process)
        process.start()

    try:
        time.sleep(10)
    except KeyboardInterrupt:
        print("Closed")

    for process in processes:
        process.terminate()
        process.join()

"""
print(GetCoreTemperature())
print(GetBatteryVoltage())
print(GetBatteryPower())
print(GetCoreVoltage())
print(GetBiosInfo())
print(GetOsInfo())
print(GetCpuModel())
print(GetCpuCores())
print(GetCpuThreads())
print(GetMotherboardModel())
print(GetMotherboardVendor())
print(GetCacheSize())
print(GetMemoryInfo_Static()["Type"])
print(GetMemoryInfo_Static()["Speed"])
print(GetMemoryInfo_Static()["Channel"])
print(GetMemoryInfo_Static()["Total_Size"])
print(GetMemoryInfo_Dynamic()["Available Size"])
print(GetMemoryInfo_Dynamic()["Usage"])
"""

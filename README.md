Here's a revised version of your README, including sections for pictures for each tab and installation instructions:

---

# NTI-EME-R8-PythonProject

The **Linux Monitoring Tool** is an all-in-one system monitoring application that provides comprehensive monitoring of hardware information for a Linux system or virtual machine. It tracks CPU details, motherboard specs, memory attributes, system temperatures, power consumption, and voltage values. The **Testing** tab allows users to perform stress tests on the CPU and other components to ensure optimal performance.

## Features

### CPU Monitoring
- **CPU Name**
- **CPU Clock Speed**
- **Number of Cores and Threads**
- **Cache Levels**

### Motherboard and BIOS Information
- **Chipset**
- **Manufacturer**
- **BIOS Version**

### Operating System Information
- **Detailed OS specifications and versioning.**

### Memory (RAM) Monitoring
- **Frequency**
- **Type**
- **Size**
- **Number of Channels**

### System Temperatures
- **CPU Temperature**
- **RAM Temperature**

### Power Consumption
- **Real-time power consumption data.**

### Voltage Values
- **Current voltage readings for various components.**

### Testing Tab
- **Perform stress tests on the CPU and other components to evaluate performance under load.**

## Screenshots

### CPU Tab
![WhatsApp Image 2024-10-10 at 18 42 31_91bd217c](https://github.com/user-attachments/assets/962f5c6a-5d6e-4ef2-bdb0-790dedacd385)

### Motherboard Tab
![WhatsApp Image 2024-10-10 at 18 42 33_02bef956](https://github.com/user-attachments/assets/84818be9-a2d5-4bd4-818f-4bb49b9a6125)

### OS Tab
![WhatsApp Image 2024-10-10 at 18 42 31_ddfee5ce](https://github.com/user-attachments/assets/c5359351-2179-41eb-a415-3980177807b2)

### Memory Tab
![WhatsApp Image 2024-10-10 at 18 42 32_084a61c7](https://github.com/user-attachments/assets/beb87c96-2bf4-45e5-b64d-d5f7d31cbc13)

### Power Consumption Tab
![WhatsApp Image 2024-10-10 at 18 42 32_f062db07](https://github.com/user-attachments/assets/8c3d8a15-c24a-45b5-ba2c-9eae13a9d432)

### Testing Tab
![image](https://github.com/user-attachments/assets/1c106287-3099-4189-9d33-8cca1da8ef7c)

## Alternative to CPU-Z for Linux

Currently, there is no direct equivalent of CPU-Z available for Linux systems. However, **CPU-X** is an alternative that provides similar functionality, including detailed hardware information. Unfortunately, CPU-X does not include a stress test script, which is a key feature of the **Linux Monitoring Tool**. This tool offers comprehensive monitoring and stress testing capabilities for users operating in Linux environments.

## How to Use

1. **Install Requirements**
   Make sure you have Python 3 and `pip` installed. Then, install the required packages by running:
   ```bash
   pip install -r requirements.txt
   ```

2. **Execute the Application**
   Run the application by executing the following command:
   ```bash
   python3 interface.py
   ```

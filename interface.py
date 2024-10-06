#!/usr/bin/python3
import customtkinter
import system_monitoring_project as data


# Set appearance mode and theme
customtkinter.set_appearance_mode("dark")  # Dark mode for a professional look
customtkinter.set_default_color_theme("blue")  # Blue theme for technical feel

# Create the main application window
app = customtkinter.CTk()
app.geometry("600x400")
app.title("System Information Viewer")  # Title of the application

def update_cpu_info():
    cpu_voltage = data.GetCoreVoltage()  # Get CPU Voltage
    cpu_temperature = data.GetCoreTemperature()  # Get CPU Temperature
    # Update the label with the retrieved information
    cpu_text_label.configure(text=f"CPU Voltage: {cpu_voltage}\nCPU Temperature: {cpu_temperature}")

# Create a tab view for separate sections
tab_view = customtkinter.CTkTabview(master=app)
tab_view.pack(fill="both", expand=True, padx=10, pady=10)

# Create CPU tab
cpu_tab = tab_view.add("CPU")

# Create a frame for CPU Information
cpu_frame = customtkinter.CTkFrame(master=cpu_tab, fg_color="#1e1e1e", corner_radius=10)
cpu_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Title label for CPU Information
cpu_label = customtkinter.CTkLabel(master=cpu_frame, text="CPU Voltage", text_color="white", font=("Arial", 14, "bold"))
cpu_label.pack(pady=10)

# Label to display CPU info
cpu_text_label = customtkinter.CTkLabel(master=cpu_frame, text="", text_color="white", justify="left")
cpu_text_label.pack(pady=10)

# Button to get CPU Voltage
cpu_voltage_button = customtkinter.CTkButton(master=cpu_frame,text="Get CPU Info",command=update_cpu_info)
cpu_voltage_button.pack(pady=10)


# Create Memory tab
memory_tab = tab_view.add("Memory")
memory_tab = tab_view.add("Motherboard")

# Create a frame for Memory Information
memory_frame = customtkinter.CTkFrame(master=memory_tab, fg_color="#1e1e1e", corner_radius=10)
memory_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Title label for Memory Information
memory_label = customtkinter.CTkLabel(master=memory_frame, text="Memory Speed", text_color="white", font=("Arial", 14, "bold"))
memory_label.pack(pady=10)

# Label to display Memory info
memory_text_label = customtkinter.CTkLabel(master=memory_frame, text="", text_color="white", justify="left")
memory_text_label.pack(pady=10)

# Button to get Memory Speed
memory_speed_button = customtkinter.CTkButton(master=memory_frame, text="Get Memory Speed", command=lambda: memory_text_label.configure(text=data.GetMemorySpeed()))
memory_speed_button.pack(pady=10)


# Create Power Consumption tab
power_consumption_tab = tab_view.add("Power Consumption")  # Rename the tab to "Power Consumption"

# Create a frame for Power Consumption Information
power_consumption_frame = customtkinter.CTkFrame(master=power_consumption_tab, fg_color="#1e1e1e", corner_radius=10)
power_consumption_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Title label for Power Consumption Information
power_consumption_label = customtkinter.CTkLabel(master=power_consumption_frame, text="Power Consumption Information", text_color="white", font=("Arial", 14, "bold"))
power_consumption_label.pack(pady=10)

# Label to display Power Consumption info (will be updated dynamically)
power_text_label = customtkinter.CTkLabel(master=power_consumption_frame, text="", text_color="white", justify="left")
power_text_label.pack(pady=10)

# Function to update power information
def update_power_info():
    #Retrieve battery voltage and power
    power_voltage = data.GetBatteryVoltage()  
    power_power = data.GetBatteryPower()  

    # Update the label with the retrieved information
    power_text_label.configure(text=f"Battery Voltage:{power_voltage}\nBattery Power: {power_power}")

# Optional: Start real-time updates every few seconds (e.g., every 2 seconds)
def auto_update_power_info():
    update_power_info()  # Update power information
    app.after(2000, auto_update_power_info)  # Schedule next update in 2 seconds

# Start automatic updates
auto_update_power_info()




disk_tab = tab_view.add("Disks")
memory_tab = tab_view.add("Stress Test")
# Run the application
app.mainloop()




import customtkinter as gui
import psutil
import platform
import subprocess
import system_monitoring as data

gui.set_appearance_mode("dark")
root = gui.CTk()
root.geometry("1050x600")
root.title("Linux Monitoring Tool")
root.resizable(False, False)

BACKGROUND_COLOR = "#1A1A1A"
TEXT_COLOR = "#D9D9D9"
PRIMARY_COLOR = "#1F8EF1"
HOVER_COLOR = "#0096FF"
ACTIVE_COLOR = "#007BB8"
DYNAMIC_COLOR = "#C4C4C4"

root.configure(bg=BACKGROUND_COLOR)



def create_info_box(frame, title, info, row, column, columnspan=1):
    box_color = "#2A2A2A" if (row + column) % 2 == 0 else "#3C3C3C"
    box_frame = gui.CTkFrame(frame, fg_color=box_color, corner_radius=0)
    box_frame.grid(row=row, column=column, columnspan=columnspan, padx=10, pady=10, sticky="nsew")
    info_label = gui.CTkLabel(box_frame, text=info, font=("Arial", 24), text_color=DYNAMIC_COLOR)
    info_label.pack(expand=True)
    title_label = gui.CTkLabel(box_frame, text=title, font=("Arial", 12), text_color=TEXT_COLOR)
    title_label.pack(anchor="s", padx=10, pady=5)
    return info_label

tab_frame = gui.CTkFrame(root, fg_color="#242424", corner_radius=0)
tab_frame.pack(pady=20, padx=20, fill="x")

cpu_usage_label = None
memory_usage_label = None

def update_dynamic_info():
    global cpu_usage_label, memory_usage_label
    if cpu_usage_label:
        cpu_usage_label.configure(text=f"{data.GetCpuUsage()} %")
    if memory_usage_label:
        memory_usage_label.configure(text=data.GetMemoryInfo_Dynamic()["Usage"])
    root.after(500, update_dynamic_info)

def show_tab(tab_name, active_button):
    global cpu_usage_label, memory_usage_label
    for widget in content_frame.winfo_children():
        widget.destroy()
    cpu_usage_label = None
    memory_usage_label = None
    for button in button_frame.winfo_children():
        button.configure(fg_color=PRIMARY_COLOR)
    active_button.configure(fg_color=ACTIVE_COLOR)
    content_frame.grid_rowconfigure(0, weight=1)
    content_frame.grid_columnconfigure(0, weight=1)
    content_frame.grid_columnconfigure(1, weight=1)
    
    if tab_name == "CPU":
        for i in range(4):
            content_frame.grid_rowconfigure(i, weight=1)
        create_info_box(content_frame, "CPU Name", data.GetCpuModel(), 0, 0, 2)
        create_info_box(content_frame, "CPU Cores", data.GetCpuCores(), 3, 1)
        create_info_box(content_frame, "CPU Threads", data.GetCpuThreads(), 1, 0)
        create_info_box(content_frame, "Cache Size", data.GetCacheSize(), 1, 1)
        create_info_box(content_frame, "Core Voltage", data.GetCoreVoltage(), 2, 0)
        create_info_box(content_frame, "Core Temperature", data.GetCoreTemperature(), 2, 1)
        cpu_usage_label = create_info_box(content_frame, "CPU Usage", f"{data.GetCpuUsage()} %", 3, 0)

    elif tab_name == "Motherboard":
        for i in range(4):
            content_frame.grid_rowconfigure(i, weight=1)
        create_info_box(content_frame, "Motherboard Model", data.GetMotherboardModel(), 0, 0)
        create_info_box(content_frame, "Motherboard Vendor", data.GetMotherboardVendor(), 0, 1)
        create_info_box(content_frame, "BIOS Version", data.GetBiosInfo()["Version"], 1, 0)
        create_info_box(content_frame, "BIOS Vendor", data.GetBiosInfo()["Vendor"], 1, 1)
        create_info_box(content_frame, "Release Date", data.GetBiosInfo()["Release Date"], 2, 0)
        create_info_box(content_frame, "ROM Size", data.GetBiosInfo()["ROM Size"], 2, 1)

    elif tab_name == "OS":
        for i in range(1):
            content_frame.grid_rowconfigure(i, weight=1)
        create_info_box(content_frame, "Operating System", data.GetOsInfo()["Name"], 0, 0)
        create_info_box(content_frame, "OS Version", data.GetOsInfo()["Version"], 0, 1)

    elif tab_name == "Memory":
        for i in range(2):
            content_frame.grid_rowconfigure(i, weight=1)
            content_frame.grid_columnconfigure(i, weight=1)
        memory_info = psutil.virtual_memory()
        create_info_box(content_frame, "RAM Frequency", data.GetMemoryInfo_Static()["Speed"], 0, 0)
        create_info_box(content_frame, "Channel", data.GetMemoryInfo_Static()["Channel"], 0, 1)
        memory_usage_label=create_info_box(content_frame, "Memory Usage", data.GetMemoryInfo_Dynamic()['Usage'], 1, 0)
        create_info_box(content_frame, "RAM Type", data.GetMemoryInfo_Static()["Type"], 1, 1)
        create_info_box(content_frame, "Total Memory", data.GetMemoryInfo_Static()["Total_Size"], 2, 0)
        create_info_box(content_frame, "Available Memory", data.GetMemoryInfo_Dynamic()["Available_Size"], 2, 1)

    elif tab_name == "Power Consumption":
        for i in range(2):
            content_frame.grid_rowconfigure(i, weight=1)
            content_frame.grid_columnconfigure(i, weight=1)
        power_box = create_info_box(content_frame, "Power Consumption", data.GetBatteryPower(), 0, 0, columnspan=2)

    #Still in progress
    elif tab_name == "Test":
        content_frame.grid_rowconfigure(0, weight=1)
        create_info_box(content_frame, "Test Info", "This is a test tab for additional data.", 0, 0, 2)
        test_button = gui.CTkButton(content_frame, text="Run Test", command=data.StressCpu, font=("Aptos", 14, "bold"))
        test_button.grid(row=1, column=0, columnspan=2, pady=20)

content_frame = gui.CTkFrame(root, corner_radius=0, fg_color="#242424")
content_frame.pack(pady=10, padx=20, fill="both", expand=True)

button_frame = gui.CTkFrame(tab_frame, fg_color="#242424", corner_radius=0)
button_frame.pack(pady=10, fill="x")

tabs = ["CPU", "Motherboard", "OS", "Memory", "Power Consumption", "Test"]

for tab in tabs:
    tab_button = gui.CTkButton(button_frame, text=tab, font=("Aptos", 14, "bold"), command=lambda t=tab: show_tab(t, tab_button))
    tab_button.grid(row=0, column=tabs.index(tab), padx=10)
    if tab == "CPU":
        tab_button.configure(fg_color=ACTIVE_COLOR)

update_dynamic_info()
show_tab("CPU", tab_button)
root.mainloop()

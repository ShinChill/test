import psutil
import socket
import platform
import tkinter as tk

def get_cpu_info():
    cpu_info = {
        "CPU": platform.processor(),
        "Physical Cores": psutil.cpu_count(logical=False),
        "Total Cores": psutil.cpu_count(logical=True)
    }
    return cpu_info

def get_disk_info():
    disk_info = {
        "Total": round(psutil.disk_usage("/").total / (1024 ** 3), 2),
        "Used": round(psutil.disk_usage("/").used / (1024 ** 3), 2),
        "Free": round(psutil.disk_usage("/").free / (1024 ** 3), 2)
    }
    return disk_info

def get_ram_info():
    ram_info = {
        "Total": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "Available": round(psutil.virtual_memory().available / (1024 ** 3), 2),
        "Used": round(psutil.virtual_memory().used / (1024 ** 3), 2),
        "Percentage": psutil.virtual_memory().percent
    }
    return ram_info

def get_network_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    wifi_ip = None
    interfaces = psutil.net_if_addrs()
    for interface, addresses in interfaces.items():
        for address in addresses:
            if address.family == socket.AF_INET and "wlan" in interface:
                wifi_ip = address.address
                break
        if wifi_ip:
            break

    return hostname, ip_address, wifi_ip

window = tk.Tk()
window.title("System Information")
window.geometry("400x300")


cpu_label = tk.Label(window, text="CPU Information", font=("Helvetica", 16))
cpu_label.pack()
cpu_info = get_cpu_info()
for key, value in cpu_info.items():
    label = tk.Label(window, text=f"{key}: {value}")
    label.pack()


disk_label = tk.Label(window, text="Disk Information", font=("Helvetica", 16))
disk_label.pack()
disk_info = get_disk_info()
for key, value in disk_info.items():
    label = tk.Label(window, text=f"{key}: {value} GB")
    label.pack()


ram_label = tk.Label(window, text="RAM Information", font=("Helvetica", 16))
ram_label.pack()
ram_info = get_ram_info()
for key, value in ram_info.items():
    label = tk.Label(window, text=f"{key}: {value} GB")
    label.pack()


network_label = tk.Label(window, text="Network Information", font=("Helvetica", 16))
network_label.pack()
hostname, ip_address, wifi_ip = get_network_info()
hostname_label = tk.Label(window, text=f"Hostname: {hostname}")
hostname_label.pack()
ip_label = tk.Label(window, text=f"IP Address: {ip_address}")
ip_label.pack()

if wifi_ip:
    wifi_label = tk.Label(window, text=f"WiFi IP Address: {wifi_ip}")
    wifi_label.pack()
else:
    wifi_label = tk.Label(window, text="WiFi IP Address: Not available")
    wifi_label.pack()


window.mainloop()


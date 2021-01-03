import psutil

print("---------------BEGIN---------------")
# Number of Cores
print("Number of Cores")
print("Physical Cores:", psutil.cpu_count(logical=False))
print("Total Cores:", psutil.cpu_count(logical=True))

# CPU Frequencies
cpufreq = psutil.cpu_freq()
print("\nCPU Frequencies")
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")

# CPU Usage
print("\nCPU Usage")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")
print("---------------END---------------")

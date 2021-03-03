import psutil

print("---------------BEGIN---------------")
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656    => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["","K","M","G","T","P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

# Get the Memory Details
svmem = psutil.virtual_memory()
print("Memory Details")
print(f"Total: {get_size(svmem.total)}")
print(f"Available: {get_size(svmem.available)}")
print(f"Used: {get_size(svmem.used)}")
print(f"Percentage: {svmem.percent}%")

# Get the SWAP Memory Details (if exists)
swap = psutil.swap_memory()
print("\nSWAP Partition")
print(f"Total: {get_size(swap.total)}")
print(f"Free: {get_size(swap.free)}")
print(f"Used: {get_size(swap.used)}")
print(f"Total: {swap.percent}%")
print("---------------END---------------")

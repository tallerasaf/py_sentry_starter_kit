import humanfriendly
import psutil

CPU_NUM_DIGITS_ROUND = 3


def get_cpu() -> str:
    cpus = psutil.cpu_percent(interval=1, percpu=True)
    cpu_avg = sum(cpus) / len(cpus)
    return f'{round(cpu_avg, CPU_NUM_DIGITS_ROUND)}%'


def get_ram_none_k8s() -> str:
    memory_info = psutil.virtual_memory()
    return humanfriendly.format_size(memory_info.total - memory_info.available, binary=True)


def get_disk_free_space() -> str:
    disk_info = psutil.disk_usage('.')
    return humanfriendly.format_size(disk_info.used, binary=True)

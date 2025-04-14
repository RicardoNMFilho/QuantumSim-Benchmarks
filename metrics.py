import psutil
import time

def get_metrics(func, *args, **kwargs):
    process = psutil.Process()

    cpu_start = process.cpu_times()
    mem_start = process.memory_info().rss
    time_start = time.time()

    result = func(*args, **kwargs)

    cpu_end = process.cpu_times()
    mem_end = process.memory_info().rss
    time_end = time.time()

    cpu_user = cpu_end.user - cpu_start.user
    cpu_system = cpu_end.system - cpu_start.system
    cpu_total = cpu_user + cpu_system

    stats = {
        "cpu": cpu_total,
        "mem": mem_end - mem_start,
        "time": time_end - time_start
    }

    return stats
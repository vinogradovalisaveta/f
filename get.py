import psutil


def get_processes():
    processes = []
    for process in psutil.process_iter():
        processes.append(process.as_dict(attrs=['name', 'pid', 'status', 'nice', 'num_threads',
                                                'cpu_percent', 'username']))

    return processes


def get_loadavg():
    avgload = psutil.getloadavg()
    return avgload


def get_sleeping():
    sleeping = 0
    for process in get_processes():
        if process['status'] == 'sleeping':
            sleeping += 1
    return sleeping


def get_running():
    running = 0
    for process in get_processes():
        if process['status'] == 'running':
            running += 1
    return running


def get_idle():
    idle = 0
    for process in get_processes():
        if process['status'] == 'idle':
            idle += 1
    return idle


def get_threads():
    threads = 0
    for process in get_processes():
        threads += process['num_threads']
    return threads


def get_cpu_percent():
    cpu_percent = psutil.cpu_percent()
    return cpu_percent


def get_io_counters():
    counters = psutil.net_io_counters()
    return counters


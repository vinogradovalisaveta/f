import decorator
import get


@decorator.save_info_to_json('info.txt', 'info.json')
def num_processes():
    total = get.get_processes()
    running = get.get_running()
    sleeping = get.get_sleeping()
    idle = get.get_idle()
    threads = get.get_threads()
    print(f'Processes: {len(total)} total, {running} running, {sleeping} sleeping, {idle} idle, '
          f'{threads} threads.')
    return total, running, sleeping, idle, threads


@decorator.save_info_to_json('info.txt', 'info.json')
def show_load():
    load = get.get_loadavg()
    print(f'Load Avg: {round(load[0], 2)} {round(load[1], 2)} {round(load[2], 2)}')
    return load


@decorator.save_info_to_json('info.txt', 'info.json')
def show_cpu():
    cpu = get.get_cpu_percent()
    print(f'CPU usage: {cpu}%')
    return cpu


@decorator.save_info_to_json('info.txt', 'info.json')
def show_counters():
    counters = get.get_io_counters()
    print(f'Network statistics: bytes sent {counters[0]}, bytes received {counters[1]}, '
          f'packets sent {counters[2]}, packets received {counters[3]}')
    return counters


@decorator.save_processes_to_json('processes.txt', 'processes.json')
def show_processes():
    processes = get.get_processes()
    print('|{:^40}|{:^5}|{:^10}|{:^6}|{:^11}|{:^11}|{:^20}|'.format(
        'name', 'pid', 'status', 'nice', 'num_threads', 'cpu_percent', 'username'), end='\n')
    i = 0
    for process in processes:
        if i == 30:
            break
        else:
            print('|{:^40}|{:^5}|{:^10}|{:^6}|{:^11}|{:^11}|{:^20}|'.format(
                process['name'], process['pid'], process['status'], process['nice'],
                process['num_threads'], process['cpu_percent'], process['username'])
            )
            i += 1
    return processes

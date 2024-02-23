import json


def save_info_to_json(txt_file, json_file):
    def decorator(func):
        def wrapper():
            info = func()
            with open(txt_file, 'a') as file_txt:
                print(info, end='\n', file=file_txt)

            with open(json_file, 'a') as file_json:
                json.dump(info, file_json, indent=1)

        return wrapper

    return decorator


def save_processes_to_json(file_name_txt, file_name_json):
    def decorator(func):
        def wrapper():
            processes = func()
            i = 0
            with open(file_name_txt, 'w') as name_txt:
                for process in processes:
                    if i == 30:
                        break
                    else:
                        print('|{:^40}|{:^5}|{:^10}|{:^6}|{:^11}|{:^11}|{:^20}|'.format(
                            process['name'], process['pid'], process['status'], process['nice'],
                            process['num_threads'], process['cpu_percent'], process['username']),
                            file=name_txt)
                        i += 1

            with open(file_name_json, 'w') as name_json:
                i = 0
                for process in processes:
                    if i == 30:
                        break
                    else:
                        json.dump(process, name_json, indent=1)
                    i += 1

        return wrapper

    return decorator

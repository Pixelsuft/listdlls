import listdlls
from clear_cache import clear as clear_cache
from time import sleep as time_sleep
from os import system as cmd_run


if not listdlls.download_all():
    print(f'Can\'t download utility.')
    exit()


def scan():
    last_detect = None
    detect = None
    while True:
        try:
            detect = listdlls.listdll(process, arc='x86')[2]
        except BaseException:
            print('Process closed, quiting...')
            break
        if last_detect is not None and not detect == last_detect:
            print('Hax detected, closing game...')
            cmd_run(f'taskkill /f /im "{process}"')
            break
        else:
            last_detect = detect
        time_sleep(1)


process = input('Enter process to detect hax: ')
if process:
    try:
        pid, cmdline = listdlls.listdll(process, arc='x86')[:2]
    except BaseException:
        print('Not found.')
        exit()
    print(f'PID: {pid}\nCMDLine: {cmdline}\nStarting AntiCheat...')
    scan()
clear_cache()

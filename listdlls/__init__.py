from subprocess import check_output as run_cmd_log
from urllib.request import urlretrieve as download
from urllib.error import URLError as DownloadError
from os.path import join as join_path
from os.path import dirname as get_dir_from_filename
from os import access as file_exists
from os import F_OK as file_exists_param
from os import name as os_type


__moduledir__ = get_dir_from_filename(__file__)
joined_32 = join_path(__moduledir__, 'Listdlls.exe')
joined_64 = join_path(__moduledir__, 'Listdlls64.exe')


ProcessError = Exception('No matching processes were found.')
UtilityNotFoundError = Exception('No Listdlls utility was found.')
OsTypeError = Exception('Listdllls can be runned ONLY under Windows.')


def listdll(process, arc='x86'):
    command = None
    if not os_type == 'nt':
        raise OsTypeError
    if '64' in arc:
        if not file_exists(joined_64, file_exists_param):
            raise UtilityNotFoundError
        command = f'"{joined_64}" {process} /accepteula'
    else:
        if not file_exists(joined_32, file_exists_param):
            raise UtilityNotFoundError
        command = f'"{joined_32}" {process} /accepteula'
    log = run_cmd_log(command, shell=True, encoding='utf-8').split('\n')
    if 'No matching processes were found.' in log:
        raise ProcessError
    pid = int(log[6].split('pid: ')[1])
    cmdline = str(log[7][15:-2])
    temp_len = [0, 1, 1, 1]
    for i in range(len(log[9])):
        if temp_len[3] == 1:
            if log[9][i] == 'S':
                temp_len[3] = 2
            else:
                temp_len[0] += 1
        elif temp_len[3] == 2:
            if log[9][i] == 'P':
                temp_len[3] = 3
            else:
                temp_len[1] += 1
        else:
            temp_len[2] += 1
    temp_len = (temp_len[0], temp_len[1], temp_len[2])
    result = []
    for i in log[10:-1]:
        result.append(
            (
                i[:temp_len[0] - 2],
                i[temp_len[0]: temp_len[0] + temp_len[1] - 2],
                i[temp_len[0] + temp_len[1]:]
            )
        )
    return pid, cmdline, tuple(result)


def download_all():
    if not os_type == 'nt':
        raise OsTypeError
    result = True
    if not file_exists(joined_32, file_exists_param):
        try:
            download('https://github.com/Pixelsuft/listdlls/raw/main/listdlls/Listdlls.exe', joined_32)
        except DownloadError:
            result = False
    if not file_exists(joined_64, file_exists_param):
        try:
            download('https://github.com/Pixelsuft/listdlls/raw/main/listdlls/Listdlls64.exe', joined_64)
        except DownloadError:
            result = False
    return result

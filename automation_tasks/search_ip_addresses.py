import re
import logging as log
from Data import data

log.basicConfig(filename='local_logs.log', level=log.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def search_strings(data_file, search_result_file, pattern):
    unique_values = []
    pattern = pattern  # r" ([0-9.]*) "
    log.info(f'set pattern to {pattern}')
    with open(search_result_file, 'w') as search_result:
        pass
    with open(data_file, 'r') as log_file, open(search_result_file, 'a') as search_result:
        for line in log_file:
            result = re.findall(pattern, line)
            if result:
                if len(result) == 1 and result[0] not in unique_values:
                    unique_values.append(result[0])
                    search_result.write(result[0] + '\n')
                elif len(result) > 1:
                    result_row = ''
                    for value in result:
                        if value not in unique_values:
                            unique_values.append(value)
                            result_row += value + ','
                    search_result.write(result_row + '\n')
    return unique_values


# Usage example:
log_file_path = '../Data/netw_logs.txt'
search_result_file = '../Results/ip_adresses.txt'
pattern = data.IP_ADDRESS
ips = search_strings(log_file_path, search_result_file, pattern)
for ip in ips:
    print(ip)

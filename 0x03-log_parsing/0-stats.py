#!/usr/bin/python3

import sys
import signal

total_size = 0
status_code_count = {}

def print_stats(signal, frame):
    print("File size: {}".format(total_size))
    for status_code, count in sorted(status_code_count.items()):
        print("{}: {}".format(status_code, count))
    sys.exit(0)

signal.signal(signal.SIGINT, print_stats)

try:
    line_count = 0
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        if len(parts) != 10:
            continue

        ip_address, _, _, _, _, request, status_code, file_size = parts
        if not status_code.isdigit():
            continue

        total_size += int(file_size)
        status_code = int(status_code)
        status_code_count[status_code] = status_code_count.get(status_code, 0) + 1

        line_count += 1
        if line_count % 10 == 0:
            print_stats(None, None)
except KeyboardInterrupt:
    print_stats(None, None)


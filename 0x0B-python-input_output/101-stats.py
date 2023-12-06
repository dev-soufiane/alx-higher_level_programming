#!/usr/bin/python3
"""
This module processes input data and calculates metrics.
"""


def display_metrics(total_size, http_statuses):
    """
    Display computed metrics.

    :param total_size: The total size computed from the input data.
    :param http_statuses: A dictionary containing
                         HTTP status codes and their counts.
    """
    print("Total size: {}".format(total_size))
    for code in sorted(http_statuses):
        print("{}: {}".format(code, http_statuses[code]))


if __name__ == "__main__":
    import sys

    total_size = 0
    http_statuses = {}
    valid_http_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                display_metrics(total_size, http_statuses)
                line_count = 1
            else:
                line_count += 1

            elements = line.split()

            try:
                total_size += int(elements[-1])
            except (IndexError, ValueError):
                pass

            try:
                if elements[-2] in valid_http_codes:
                    if http_statuses.get(elements[-2], -1) == -1:
                        http_statuses[elements[-2]] = 1
                    else:
                        http_statuses[elements[-2]] += 1
            except IndexError:
                pass

        display_metrics(total_size, http_statuses)

    except KeyboardInterrupt:
        display_metrics(total_size, http_statuses)
        raise

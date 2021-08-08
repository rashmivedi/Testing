  from collections import ChainMap
     import csv
     import re

     regex_device = re.compile('(?P<Router>^.+)[>#]')

     regex = re.compile('(?P<protocol>\S+) +'
                '(?P<network>\d+\.\d+\.\d+\.\d+)/?'
                '(?P<mask>\d*) +'
                '(?P<AD>\[\d+/\d+\]) +via +'
                '(?P<nextHop>\d+\.\d+\.\d+\.\d+)\,\ +'
                '(?P<interface>\S+\d+/\d+)*'
                '(?P<time>\S+)')


     regex_direktly = re.compile('(?P<protocol>[L|C|S]) +'
                        '(?P<network>\d+\.\d+\.\d+\.\d\d?\d?)/?'
                        '(?P<mask>\d*) +'
                        '(?P<nextHop>.*), +'
                        '(?P<interface>\S+\d/\d+|.*)'
                        '(?P<time>\S*)')

     result = []
     result1 = []

     with open('output_route_table.txt') as data:
         for line in data:
            match = regex_device.search(line)
            if match:
               result1.append(match.groupdict())

     with open('output_route_table.txt') as data:
         for line in data:
            match = regex.search(line)
            if match:
               result.append(match.groupdict())

     with open('output_route_table.txt') as data:
        for line in data:
           match = regex_direktly.search(line)
           if match:
              result.append(match.groupdict())

     with open('output_route_table.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=list(result[0].keys()))
        writer.writeheader()
        for d in result:
            writer.writerow(d)

import math

from parser_file import parse
from collections import defaultdict

"""
D - sim duration
I - num intersections
S - number of streets
V - number of cars
F - Base points awarded for each car reached end 

streets
    B - Start intersection
    E - End Intersection
    L - Time to traverse street
    
car_path
    P - number of streets
    total_len -  time to reach end of journey given no traffic
"""

def writeSubmission(intersection, files):
    f = open('results/' + files, 'w')
    f.write(str(len(intersection)) + '\n')
    for i in range(len(intersection)):
        f.write( str(intersection[i]['i']) + '\n')
        f.write( str(intersection[i]['e']) + '\n')
        for n in range(intersection[i]['e']):
            f.write( str(intersection[i]['street'][n][0]) + ' ' + str(intersection[i]['street'][n][1]) + '\n')

def route_len_adder(data):
    for c_path in data['car_path']:
        t_len = 0
        for street in c_path['street_list'][1:]:
            t_len += data['streets'][street]['L']
        c_path['total_len'] = t_len

def freq_method(file):
    def generate_street_time(street_list, street_freq, period_len):
        total = 0
        for s in street_list:
            total += street_freq[s]
        if total == 0:
            total = 1
        out = []
        for street_n in street_list:
            t = math.ceil(street_freq[street_n] / total * period_len)
            if t <= 0:
                t=1
            out.append((street_n, t))
        return out

    def generate_street_time_dynamic_period(street_list, street_freq, intersections_count):
        if intersections_count==0:
            period_len=1
        else:
            if intersections_count >10000:

                period_len = 30
            else:
                period_len=4
            # if period_len > 40:
            #     period_len = 40
            if period_len==0:
                period_len=10
        total = 0
        for s in street_list:
            total += street_freq[s]
        if total == 0:
            total = 1
        out = []
        for street_n in street_list:
            t = math.ceil(street_freq[street_n] / total * period_len)
            if t <= 0:
                t=1
            out.append((street_n, t))
        return out

    data = parse(file)
    route_len_adder(data)
    print('sim length: ', data['D'])
    intersections_out = defaultdict(list)
    intersections_in = defaultdict(list)
    for name, street in data['streets'].items():
        intersections_in[street['E']].append(name)
        intersections_out[street['B']].append(name)


    freq_streets = defaultdict(int)
    intersections_count = defaultdict(int)
    for car_path in data['car_path']:
        print(car_path['total_len'])
        for street in car_path['street_list']:

            freq_streets[street] += 1
            intersections_count[data['streets'][street]['E']] += 1
    result = []
    for inter_name, street_list in intersections_in.items():
        # if a street has not traffic, we delete it lol
        new_street_list = [val for val in street_list if (freq_streets[val] > 0)]

        total = 0
        for s in new_street_list:
            total += freq_streets[s]

        new_street_list = [val for val in new_street_list if ((freq_streets[val] / total)>0.01)]
        if not new_street_list:
            new_street_list = street_list

        i = inter_name
        e = len(new_street_list)
        period_len = 4
        result.append({'i': i, 'e': e, 'street': generate_street_time_dynamic_period(street_list, freq_streets, intersections_count[i])})
        # result.append({'i': i, 'e': e, 'street': generate_street_time(new_street_list, freq_streets, period_len)})
    writeSubmission(result, "sub_"+file)

freq_method('a.txt')
freq_method('b.txt')
freq_method('c.txt')
freq_method('d.txt')
freq_method('e.txt')
freq_method('f.txt')

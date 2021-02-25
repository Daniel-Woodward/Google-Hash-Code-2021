


def parse(filename):
    with open(filename) as f:
        out = dict()
        out['streets'] = dict()
        out['car_path'] = list()
        for idx, line in enumerate(f):
            if idx == 0:
                D, I, S, V, F = line.split(" ")
                out['D'] = int(D)
                out['I'] = int(I)
                out['S'] = int(S)
                out['V'] = int(V)
                out['F'] = int(F)
            elif idx <= out['S']:
                B, E, street_name, L = line.split(" ")
                street_name = street_name.replace('\n', '')
                out['streets'][street_name] = {'B': int(B), 'E': int(E), 'L': int(L)}
            else:
                thing = line.split(" ")
                street_list = [val.replace('\n', '') for val in thing[1:]]
                out['car_path'].append({'P': thing[0], 'street_list': street_list})
        return out

def writeSubmission(numIntersections = 1):
    #number of intersections
    f = open("submission.txt", "w")
    f.write(repr(numIntersections) + "\n")



    for i in range(numIntersections):
        #intersection ID
        f.write( 'ID here' + "\n")

        #number of incoming streets
        f.write( 'Num incoming streets' + "\n")

        #schedule E.g. = 1
        streets = 2
        for i in range(streets):
            f.write( 'streetName' + 'streetTime' + "\n")

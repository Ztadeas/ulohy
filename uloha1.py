import math

def g_dist(a, a2):
    f_1 = (a["x"] - a2["x"])**2
    f_2 = (a["y"] - a2["y"])**2

    return math.sqrt(f_1+f_2)


def g_all(a, a2):
    hadice_length = g_dist(a, a2)

    lower_x = a['x'] if a['x'] < a2['x'] else a2['x']
    bigger_x = a2['x'] if a['x'] < a2['x'] else a['x']
    
    roz_x = bigger_x - lower_x

    c_sqr = hadice_length**2
    a_sqr = roz_x**2

    return {
        'hadice': hadice_length,
        'potrubi': math.sqrt(c_sqr - a_sqr) + roz_x
    }

def prepis_inp(inp):
    
    box_size = int(inp[0])
    try:
        a_raw = list(map(int, inp[1].split()))
        a2_raw = list(map(int, inp[2].split()))

    except:
        return False
    if a_raw == [] or a2_raw == []:
        return False
    a = {'x': a_raw[0], 'y': a_raw[1], 'z': a_raw[2]}
    a2 = {'x': a2_raw[0], 'y': a2_raw[1], 'z': a2_raw[2]}
    return {'box_size': box_size, 'a': a, 'a2': a2}

def xyz_check(c):
    return all(isinstance(num, (int, float)) for num in [c['x'], c['y'], c['z']])

def validate(inp, box_size, a, a2):
    if len(inp) != 4 or not xyz_check(a) or not xyz_check(a2):
        return False

    points = [a['x'], a2['x']]
    clear_border = all(20 <= point <= box_size for point in points)

    return clear_border


file_names = [
    '0000_in.txt',
    '0001_in.txt',
    '0002_in.txt',
    '0003_in.txt',
    '0004_in.txt',
    '0005_in.txt',
    '0006_in.txt',
]

for file_name in file_names:
    with open(file_name, 'r') as file:
        inp_data = file.read().split('\n')
    data = prepis_inp(inp_data)
    if not data:
        print('Nespravny vstup')
        print('===================')
        continue
    box_size, a, a2 = data['box_size'], data['a'], data['a2']
    valid_inp = validate(inp_data, box_size, a, a2)
    lengths = None

    if not valid_inp:
        print(f"Rozmer :\n{box_size}")
    
        if xyz_check(a):
          print(f"Bod #1:\n{a['x']}, {a['y']}, {a['z']}")
        if xyz_check(a2):
          print(f"Bod #2:\n{a2['x']}, {a2['y']}, {a2['z']}")

        if lengths:
          print(f"Delka potrubi:\n{lengths['potrubi']}")
          print(f"Delka hadice:\n{lengths['hadice']}")
        
        print('Nespravny vstup')
        print('===================')
        continue
    
    if a2['z'] == box_size:
        all_possib = [
            {'x': a2['x'], 'y': box_size * 2 + (box_size - a2['y'])},  
            {'x': -1*a2['x'] - box_size, 'y': a2['y']},  
            {'x': a2['x'], 'y': -1*box_size - a2['y']} 
        ]

        all_dist = [g_all(a, possib) for possib in all_possib]

        lowest_hadice = min(dist['hadice'] for dist in all_dist)
        lowest_potrubi = min(dist['potrubi'] for dist in all_dist)

        lengths = {'hadice': lowest_hadice, 'potrubi': lowest_potrubi}

    elif a2['z'] > 0:
        a2_copy = {'x': a2['x'], 'y': a2['y'], 'z': a2['z']}

        if a2_copy['y'] == 0:
            a2_copy['y'] = -1*a2_copy['z']
        elif a2_copy['y'] == box_size:
            a2_copy['y'] = box_size + a2_copy['z']

        if a2_copy['x'] == 0:
            a2_copy['x'] = -1*a2_copy['z']
        elif a2_copy['x'] == box_size:
            a2_copy['x'] = box_size + a2_copy['z']

        lengths = g_all(a, a2_copy)

    print(f"Rozmer :\n{box_size}")
    
    if xyz_check(a):
          print(f"Bod #1:\n{a['x']}, {a['y']}, {a['z']}")
    if xyz_check(a2):
          print(f"Bod #2:\n{a2['x']}, {a2['y']}, {a2['z']}")

    if lengths:
          print(f"Delka potrubi:\n{lengths['potrubi']}")
          print(f"Delka hadice:\n{lengths['hadice']}")


    print('===================')


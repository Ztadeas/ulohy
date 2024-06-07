import math

file_names = [
    '0000_in.txt',
    '0001_in.txt',
    '0002_in.txt',
    '0003_in.txt',
    '0004_in.txt',
    '0005_in.txt',
    '0006_in.txt',
]

def get_dist(s1, s2):
    return math.sqrt((s1[0]-s2[0])**2+(s1[1]-s2[1])**2)


def main(data):
  jmeno_souradnice = {}
  
  for n, i in enumerate(data):
    if ":" not in i:
       print("Nespravny vstup")
       return
    
    splited = i.split(":")
    souradnice = splited[0]
    try:
       souradnice = [float(j) for j in souradnice.split(",")]
       

    except:
       print("Nespravny vstup")
       return
    
    if splited[1] not in jmeno_souradnice:
      jmeno_souradnice[splited[1]] = souradnice

    else:
       jmeno_souradnice[splited[1]+f"{n}"] = souradnice

  vals = list(jmeno_souradnice.values())
  names = list(jmeno_souradnice.keys())
  distances = {}

  for i in range(len(vals)):
    for j in range(i+1, len(vals)):
      dist = get_dist(vals[i], vals[j])
      if dist not in distances:
        distances[dist] = [[names[i], names[j]]]

      else:
        distances[dist].append([names[i], names[j]])

  nejkratsi = sorted(list(distances.keys()))[0]
  print(f"Vzdalenost nejblizsich letadel: {nejkratsi}")
  print(f"Nalezenych dvojic {len(distances[nejkratsi])}")
  for i in distances[nejkratsi]:
    print(i[0]+"-"+i[1])
      
     
    


for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as file:
        input_data = file.read().split('\n')
        main(input_data[:-1]) 
            
        print('-------------------')

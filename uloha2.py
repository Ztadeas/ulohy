import math

names = ["A", "B", "C"]

for i in range(7):
    with open(f"000{i}_in.txt", "r") as f:
        data = f.readlines()
    

    for n, x in enumerate(data):
       print(f"BOD {names[n]}: {x}")

    if len(data) != 3:
        print("Nespravny vstup.")
        print("================")
        
        continue
   
    points = []
    to_stop = False
    for j in data:
      j = j.replace("\n", "")
      point = j.split(" ")
      point = [float(h) for h in point]
      if point in points:
          print("Nektere body splivaji")
          to_stop = True
          break
      points.append(point)

    if to_stop:
      print("=================")
      continue
    

    vector = [points[1][0]-points[0][0], points[1][1]-points[0][1]]
    
    n = False

    try:
       t = round((points[2][0] - points[0][0])/vector[0], 2)
       
       

    except:
       n = True
       

    if points[2][1] == round(points[0][1] + vector[1]*t, 2) or n:
       k = [sum(v) for v in points]
       serazeni = sorted(k)
       prostredni = k.index(serazeni[1])
       print("Body lezi na jedne primce.")
       print(f"Bod {points[prostredni]} je prostedni.")

    else:
       print("Body nelezi na jedne primce.")    

    print("==============")


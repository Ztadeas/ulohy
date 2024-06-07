from math import factorial

file_names = [
    '0000_in.txt',
    '0001_in.txt',
    '0002_in.txt',
    '0003_in.txt',
    '0004_in.txt',
    '0005_in.txt'
]

def main(data):
  if len(data) == 0 or len(data) > 2000:
    print("Neplatny vstup")
    return

  for i in range(len(data)):
    try:
        data[i] = int(data[i])

    except:
        print("Neplatny vstup")
        return

  all_unique = {}
  soucet = 0
  for i in range(len(data)):
    if i == len(data)-1:
        break
    
    for j in range(i+1, len(data)):
      posloupnost = data[i:j+1]
      if sum(posloupnost) not in all_unique:
         all_unique[sum(posloupnost)] = 1

      else:
        all_unique[sum(posloupnost)] += 1

  for i in all_unique:
    if all_unique[i] > 1:
      soucet += factorial(all_unique[i])/ (2*(factorial(all_unique[i]-2)))

  print(soucet)
     

    


for file_name in file_names[1:]:
        with open(file_name, 'r', encoding='utf-8') as file:
            input_data = file.read().replace('\n', ' ').strip()

            main(input_data.split(" "))
            print('-------------------')

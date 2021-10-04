

'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici
  ok=1
  if n==2:
     return True
  if n<2:
     return False
  if n%2==0:
      return False
  for i in range(3,n//2+1,2):
      if n%i==0:
         return False
  return True

def test_verificare_neprim():
    assert is_prime(45) == False
    assert is_prime(13) == True
test_verificare_neprim()

'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  p=1
  for x in lst:
     p=p*x
  return p

def test_verificare_produs():
    assert get_product([4,5,10,1,2]) == 400
    assert get_product([8,6,3]) == 144
test_verificare_produs()

'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
  while x!=y:
      if x>y:
          x=x-y
      else:
          y=y-x
  return x

def test_verificare_cmmdc1():
    assert is_prime(4,5) == 1
    assert is_prime(8,6) == 2
test_verificare_produs()


'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  r=x%y
  while r!=0:
      x=y
      y=r
      r=x%y
  return y

def test_verificare_cmmdc2():
    assert get_cmmdc_v2(4,5) == 1
    assert get_cmmdc_v2(8,6) == 2
test_verificare_produs()

def print_meniu():
    print("1. Verifica daca un numar este prim")
    print("2. Calculeaza produsul numerelor dintr-o lista data")
    print("3. Calculeaza CMMDC prin scaderi repetate")
    print("4. Calculeaza CMMDC cu metoda lui Euclid")
    print("x. Iesire")

def read_list():
    # citim numerele asa: 3,56,7,1,3,43,5,54
    given = input('Dati numerele separate prin virgula: ')
    str_list = given.split(',')
    int_list = []
    for str_num in str_list:
        int_list.append(int(str_num))
    return int_list

def main():
  # interfata de tip consola aici

  lst=[]
  while True:
    print_meniu()
    option = input('Alegeti o optiune: ')
    if option == '1':
        n=int(input('Introduceti numaul: ') )
        if is_prime(n)==True:
          print('Numarul este prim\n')
        else: print('Numarul nu este prim\n')
    elif option == '2':
        print('Introduceti numerele: ')
        lst = read_list()
        print('Produsul numerelor introduse este: ')
        print(get_product(lst))
    elif option == '3':
        x=int(input("Introduceti primul numar: "))
        y=int(input("Introduceti al doilea numar: "))
        print('CMMDC: ')
        print(get_cmmdc_v1(x,y))
    elif option == '4':
      x = int(input("Introduceti primul numar: "))
      y = int(input("Introduceti al doilea numar: "))
      print('CMMDC: ')
      print(get_cmmdc_v2(x, y))
    elif option == 'x':
        break
    else:
        print('Optiune invalida, reincearca!')




if __name__ == '__main__':
  main()

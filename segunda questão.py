import re 
password = input("Digite sua senha: ")
flag = 0
while True:        
    if not re.search("[a-z]", password): 
        flag =flag -1
        
    if not re.search("[A-Z]", password): 
        flag =flag -1
        
    if not re.search("[0-9]", password): 
        flag =flag -1
        
    if not re.search("[!@#$%^&*()-+]", password): 
        flag = flag -1
        
    if re.search("\s", password): 
        print('Senha invalida, por favor não utilize a barra de espaço.')
        flag= 1
        break
    if  flag == 0:
        print("Valid Password") 
        break
    if flag<0 : 
        print("Not a Valid Password")
        break
if (len(password)-flag)>6:
    m=(int(-flag))
    print('faltam {} caracteres para sua senha ser forte'.format(m))
else:
    n=(int(6-len(password)))
    print('faltam {} caracteres para sua senha ser forte'.format(n))
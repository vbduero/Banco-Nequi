print (" MIMI NEQUI")

listaclientes=[] 
listacontra=[] 
listaplata=[]
listacuenta=[]

class ahorro:

    def _init_(self):
        self.cuenta = ""
        self.nombre = ""
        self.apellido = ""
        self.consignacion = ""
        self.retiro = 0
        self.saldo = ""

    def registrocliente(self):
        print("Registro de nuevo cliente")
        self.cuenta= str(input("\nDigite el numero de cedula, este sera el numero de cuenta\n"))
        self.nombre= str(input("\nDigite el nombre\n"))
        self.apellido= str(input("\nDigite el apellido\n"))
        self.consignacion= float(input("\nValor con el que abre su cuenta\n"))
        self.contrasena=str(input("\nDigite contraseña: \n"))
        self.retiro = 0
        print("registro exitoso\n")

        listaclientes.append(self.nombre)
        listacuenta.append(self.cuenta)
        listacontra.append(self.contrasena)
        listaplata.append(self.consignacion)

        print (listaclientes)
        print(listacontra)
        print(listaplata)
        print(listacuenta)


    #def fff(self):
        #self.saldo = (self.consignacion - self.retiro)
        #print(self.saldo)
        #self.saldo.clear

    def este(self):
        self.rr= float(input("Digite el valor a consignar: "))
        listaplata.append(self.rr)
        print (listaplata)
        print ("Consignacion Exitosa")
        print ("Su saldo total es de: $ ",sum(listaplata))

    def ww(self):

        contra= (input("contraseña: "))
        print(listaplata)
        if contra in listacontra:
            print (" . CORRECTO . ")
            self.retiro= int(input("Digite el valor a retirar: "))
            print(listaplata)
            print(self.retiro)
            if listaplata[0] > self.retiro:
                print ("Retiro Exitoso", self.retiro)
                self.saldo = (self.retiro-sum(listaplata))
                listaplata.clear()
                listaplata.append(self.saldo)
                print (listaplata)
                print("Su saldo total es de: $ ",self.saldo)
            else:
                    print('saldo insuficiente',listaplata)
                
           # if self.retiro > listaplata:
               # print("error")
            

        else:
            print ("  -- Contraseña Denegada -- ")
            f=nequi()
            f.login()
    
class nequi(ahorro):


    def login(self):
        print ("  - - - - -  ")
        print ("\n1) Consignar\n2) Retirar\n")
        op=int(input("\neliga su opcion\n"))
        if op == 1:
            print("\npensando...\n")
            b=nequi()
            b.ca()

        if op == 2:
            print ("\nespere...\n")
            #user=input("Numero de la cuenta: ")
            b=ahorro()
            b.ww()
            

    def ca(self):
        self.cuenta=input("Numero de cuenta: ")
        #contra= int(input("contraseña: "))

        if self.cuenta in listacuenta:
                print("    --- bienvenido ---   ")
                p=ahorro()
                p.este()

        else:
            print ("  -- Datos incorrectos -- ")
            f=nequi()
            f.login()
           

class menu(nequi,ahorro):
    while  True:
        print("\nBienvenido a Nequi\n")
        opciones = int(input("\nQue opcion desea realizar?\nOPRIME\n1 PARA REGISTRAR NUEVO CLIENTE\n2 PARA INICIAR\n3 PARA SALIR\n"))
        if opciones == 1:
            a=ahorro()
            a.registrocliente()
        elif opciones == 2:
            e=nequi()
            e.login()
        else:
            print ("CERRANDO...")
            print ("GRACIAS POR CONFIAR EN NOSOTROS")
            break

t=menu()

                
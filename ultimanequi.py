print (" MIMI NEQUI")
listacontra=[] 
class ahorro:

    def __init__(self):
        self.cuenta = ""
        self.nombre = ""
        self.apellido = ""
        self.consignacion = ""
        self.retiro = ""
        self.saldo = ""
        self.listaclientes=[] 
        #self.listacontra=[] 
        self.listaplata=[]
        self.listacuenta=[]

    def registrocliente(self):
        print("Registro de nuevo cliente")
        self.cuenta= str(input("\nDigite el numero de cedula, este sera el numero de cuenta\n"))
        self.nombre= str(input("\nDigite el nombre\n"))
        self.apellido= str(input("\nDigite el apellido\n"))
        self.consignacion= float(input("\nValor con el que abre su cuenta\n"))
        self.contrasena=str(input("\nDigite contraseña: \n"))
        self.retiro = 0
        print("registro exitoso\n")

        v = (self.nombre,self.apellido,self.retiro)
        self.listaclientes.append(v)
        self.listacuenta.append(self.cuenta)
        listacontra.append(self.contrasena)
        self.listaplata.append(self.consignacion)

        print (self.listaclientes)
        print(listacontra)
        print(self.listaplata)
        print(self.listacuenta)

    def registros(self):
        print("Numero de cuenta: {} saldo: {}".format(self.cuenta,self.consignacion))

    def transaccion(self):
        self.sald=self.saldo
        self.consignacion = ""
        self.retiro = ""
        self.saldo= ""
        self.detalle = []
        print ("transaccion exitosa")

    def fff(self):
        self.saldo = (self.sald + self.consignacion - self.retiro)

    #def incluirtransaccion(self):
        #return("Consignacion: {}\nSaldo: {}".format(self.consignacion,self.saldo))

   # def incluirtransaccion1(self):
        #return("Retiro: {}\nSaldo: {} ".format(self.retiro,self.saldo))

    def mate(self):
        self.m1=self.consignacion+self.rr
        self.listaclientes.append(self.m1)

    def ww(self):
        contra= int(input("contraseña: "))
        user=input("Numero de cuenta: ")
        if contra == listacontra:
            print ("entonces")
        if user in self.cuenta :
            print("    --- bienvenido ---   ")
            self.rr= int(input("Digite el valor a consignar"))
            g=ahorro()
            g.mate()
            print (self.listaclientes)


    
class nequi(ahorro):
    def login(self):
        print ("hola")
        print ("\n1) Consignar\n 2)Retirar\n")
        op=int(input("eliga su opcion"))
        if op == 1:
            print("pensando")
            contra= int(input("contraseña: "))
            user=input("Numero de cuenta: ")
            if contra == listacontra:
               print ("entonces")
            if user in self.cuenta :
               print("    --- bienvenido ---   ")
               self.rr= int(input("Digite el valor a consignar"))
               g=ahorro()
               g.mate()
               print (self.listaclientes)
            

        if op == 2:
            print ("espere")
            #user=input("Numero de la cuenta: ")
            b=ahorro()
            b.ww()
            


    def ca(self):
        user=input("Numero de cuenta: ")
        #contra= int(input("contraseña: "))
        if user in self.cuenta :
                print("    --- bienvenido ---   ")
                self.rr= int(input("Digite el valor a consignar"))
                g=ahorro()
                g.mate()
                print (self.listaclientes)
        else:
            print ("  -- Datos incorrectos -- ")
            f=nequi()
            f.login()
           

class menu:
    while  True:
        print("\nBienvenido a Nequi\n")
        opciones = int(input("\nQue opcion desea realizar?\nOPRIME 1 PARA REGISTRAR NUEVO CLIENTE\n2 PARA INICIAR\n3 PARA SALIR\n"))
        if opciones == 1:
            a=ahorro()
            a.registrocliente()
        elif opciones == 2:
            e=nequi()
            e.login()
            e.ca()
        else:
            print ("error jiji")
            break

t=menu()






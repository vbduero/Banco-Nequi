print (" MIMI NEQUI")


listaclientes=[]


class ahorro:

    def __init__(self):
        self.cuenta = ""
        self.nombre = ""
        self.apellido = ""
        self.consignacion = ""
        self.retiro = ""
        self.saldo = ""

    def registrocliente(self):
        print("Registro de nuevo cliente")
        self.cuenta= float(input("\nDigite el numero de cedula, este sera el numero de cuenta\n"))
        self.nombre= str(input("\nDigite el nombre\n"))
        self.apellido= str(input("\nDigite el apellido\n"))
        self.consignacion= float(input("\nValor con el que abre su cuenta\n"))
        self.retiro = 0
        print("registro exitoso\n")

        v = ahorro(self.cuenta,self.nombre,self.apellido,self.consignacion,self.retiro)
        listaclientes.append(v)

    def registros(self):
        print("Numero de cuenta: {}-{} {}-saldo: {}".format(self.cuenta,self.nombre,self.apellido))


a = ahorro()
a.registrocliente()
a.registros()
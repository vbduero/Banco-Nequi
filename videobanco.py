listaclientes=[]
class banco(object):
    def __init__(self, cuenta, nombre, apellido, consignacion, retiro):
        self.cuenta = cuenta
        self.nombre = nombre
        self.apellido = apellido
        self.consignacion = consignacion
        self.retiro = retiro
        self.saldo = (consignacion - retiro)
        self.detalle = []
    
    def registros(self):
        print("Numero de cuenta: {}-{} {}-saldo: {}".format(self.cuenta,self.nombre,self.apellido))
    
    def transaccion(self,consignacion,retiro):
        sald=self.saldo
        self.consignacion = consignacion
        self.retiro = retiro
        self.saldo = (sald + consignacion - retiro)
        self.detalle = []
        print ("transaccion exitosa")

    def incluirtransaccion(self,consignacion):
         return("Consignacion: {}\nSaldo: {}".format(self.consignacion,self.saldo))

    def incluirtransaccion1(self,retiro):

        return("Retiro: {}\nSaldo: {} ".format(self.retiro,self.saldo))

    def registrocliente():
        print("Registro de nuevo cliente")
        cuenta= int(input("\nDigite el numero de cedula, este sera el numero de cuenta\n"))
        nombre= str(input("\nDigite el nombre\n"))
        apellido= str(input("\nDigite el apellido\n"))
        consignacion= int(input("\nValor con el que abre su cuenta\n"))
        retiro = 0
        print("registro exitoso\n")

        v = banco(cuenta,nombre,apellido,consignacion,retiro)
        listaclientes.append(v)

    def listadoclientes():

        print("lista de clientes")
        for v in listaclientes:
            v.registros()

    def buscarcliente():
        print("buscar cliente")
        cuenta = int(input("\nDigite el numero de cuenta\n"))
        for v in listaclientes:
            if cuenta == v.cuenta:
                v.registros()
    
    def transacciones():
        print("iniciando transaccion")
        cuenta1 = int(input("\nDigite el nuumero de cuenta\n"))
        for v in listaclientes:
            if  cuenta1 == v.cuenta:
                opc=int(input("\nQUE TRANSACCION DESEA HACER\n OPRIMA 1 PARA CONSIGNACION\n DIGETE 2 PARA "))
                if opc == 1:
                    consignacion = int(input("\nDigite el vaor de la consignacion\n"))

                    retiro = 0
                    v.transaccion(consignacion,retiro)
                    v.registros()
                    recepcionmensaje - v.incluirtransaccion(consignacion)
                    v.detalle.append(recepcionmensaje)

                if opc == 2:
                    retiro = int(input("\nDigite el valor a retirar\n"))
                    consignacion=0
                    v.transaccion(consignacion,retiro)
                    v.registros()
                    recepcionmensaje = v.incluirtransaccion(retiro)
                    v.detalle.append(recepcionmensaje)

def historial():
    print("Historial de movimientos")
    cuenta1 = int(input("\nDigite el numero de cuenta\n"))
    for v in listaclientes:
        if cuenta1 == v.cuenta:
            for recepcionmensaje in v.detalle:
                    print("Movimiento:{}".format(recepcionmensaje))
    
def main():
    while True:
        print("\nBienvenido a Nequi\n")
        opciones = int(input("\nQue opcion desea realizar?\nOPRIME 1 PARA REGISTRAR NUEVO CLIENTE\n"))
        if opciones == 1:
            r.registrocliente()
        if opciones == 2:
            r.buscarcliente()
        if opciones == 3:
            r.transacciones()
        if opciones == 4:
            r.listadoclientes()
        if opciones == 5:
                historial()
         
if __name__=='__main__':
    
    r =main()
    
            










    
        
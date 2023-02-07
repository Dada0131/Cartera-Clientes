# Imports
from io import open
from abc import ABC, abstractmethod
from datetime import datetime 
import time

"""
Creacion
Apertura
Manipulacion
Cierre
"""

#datetime.strptime(valor,' ','%d-%m-%Y') 

# Clases
class Persona(ABC):
    _secuencia = 0
    def _init_(self, nombre ="Joel", estado = True):
        Persona._secuencia = Persona._secuencia+1
        self.__id = Persona._secuencia
        self.nombre = nombre
        self.estado = estado
 
    @property
    def id(self):
        return self.__id

    @abstractmethod
    def mostrarDatos(self):
        pass



class Cliente(Persona):
    _idCliente = 0
    def __init__(self, nombre="Juan", cedula="2450449067", estado=True):
        Cliente._idCliente += 1
        super()._init_(nombre, estado)
        self.cedula =cedula
        

    @property
    def idCliente(self):
        return self._idCliente


    def mostrarDatos(self):
        with open("usuarios.txt",'r') as archivo:
            for linea in archivo:
                print(linea)


'''def mostrarDatos(self):
    print(f'Id:{self.idCliente}  Nombre:{self.nombre}  CI:{self.cedula}  Estado: {self.estado}')'''



class Factura:
    _idfactura = 0
    def __init__(self, cliente, fecha,total, estado):
        Factura._idfactura += 1
        self.cliente = cliente
        self.fecha = fecha
        self.total = total
        self.estado = estado


    @property
    def idFactura(self):
        return self._idfactura


    def mostrarDatos(self):
        with open("factura.txt",'r') as archivo:
            for linea in archivo:
                print(linea)    
        

'''def mostrardatos(self):
    pass
    print(f"{self.idFactura}.- Cliente:{self.cliente} Fecha:{self.fecha}  Total:{self.total}  Estado:{self.estado}")'''



class CabCredito:
    _idCabCredito = 0
    def __init__(self, factura, fecha, deuda, cuota, estado):
        CabCredito._idCabCredito += 1
        self.factura = factura
        self.fecha = fecha
        self.deuda = deuda
        self.cuota = cuota
        self.aammInicial = 2022
        self.detCredito = []
        self.estado = estado 

    @property
    def idCabCredito(self):
        return self._idCabCredito
        

    def addDetCredito(self, detcredito):
        self.detCredito.append(detcredito)


    def MostrarDatos(self):
        with open("Credito.txt",'r') as archivo:
            for linea in archivo:
                print(linea)




    @staticmethod
    def getInteres(principal, rate, time): #float
        return principal * rate * time

'''def mostrardatos(self):
    pass
    print(f"{self.idCabCredito}.- Factura:{self.factura}  Fecha:{self.fecha}  Deuda:{self.deuda}  Cuota:{self.cuota}")'''



class DetCredito:
    _idDetCredito = 0
    def __init__(self, aamm, cuota, estado):
        DetCredito._idDetCredito += 1
        self.aamm = aamm
        self.cuota = cuota
        self.detPago = []
        self.estado = estado


    @property
    def idDetCredito(self):
        return self._idDetCredito

    def mostrarDatos(self):
        print(f"{self.idDetCredito}.-  Cuota:{self.cuota}  DetPago:{self.detPago}  Estado:{self.estado}")

    def agregarPago(self):
        pass



class Pago:
    _idPago = 0
    def __init__(self, fecha, valor):
        Pago._idPago += 1
        self.fechaPago = fecha
        self.valor = valor


    @property
    def idPago(self):
        return self._idPago

    def MostrarDatos(self):
        with open("Pago.txt",'r') as archivo:
            for linea in archivo:
                print(linea)



    def realizarPago(self):
        return self.idPago, self.fechaPago, self.valor

'''def mostrarDatos(self):
    print(f"{self.idPago}.-  Fecha:{self.fechaPago}  Valor:{self.valor}")'''



class Calculo(ABC):
    @abstractmethod
    def realizarPago(self):
        pass





# Funciones-----------------------------------------


# validar ingreso de cedula
def ingreso_cedula(mensaje, mensajeError):
    while True:         
        valor = str(input(" {} ".format(mensaje)))
        if len(valor) == 10 and valor.isdigit():
            break
        else:
            print("  {} ".format(mensajeError)) 
            print(" "*40)
    return valor


def ingreso_fecha( mensaje, mensajeError):
        while True:
            valor = input("{} ".format(mensaje))            
            try:               
                valor = datetime.strptime(valor,"%d-%m-%Y")
                
                
                if valor:
                    break
            except ValueError:
                print(mensajeError)        
        return valor




def consultar_info():
    print("*** Consulta General ***")
    print("1.- Mostrar Clientes")
    print("2.- Mostrar Facturas")
    print("3.- Mostrar Credito")
    print("4.- Mostrar Pagos")
    print("5.- Regresar al menu principal")
    option = input("Seleccione una opción: ")
    if option == "1":            
        Cliente.MostrarDatos(Cliente)
    elif option == "2":
        Factura.MostrarDatos(Factura)
    elif option == "3":
        CabCredito.MostrarDatos(CabCredito)
    elif option == "4":
        Pago.MostrarDatos(Pago)
    elif option == "5":
        exit()
            



# Clases de manipulacion de archivos -----------------------------------------------

class Archivo:
    def __init__(self,nombreArchivo,separador=';'):
        self.__archivo = nombreArchivo
        self.__separador = separador
        
    def mostrar(self, archivo):
        with open(archivo, 'r') as archivo:
            datos = archivo.read()
            return datos
             
    def buscarLista(self,buscado):
        resultado = []
        with open(self.__archivo, mode='r', encoding='utf-8') as file:
            for linea in file:
                registro = linea[:-1].split(self.__separador) 
                if registro[0] == buscado:
                    resultado.append(registro)
        return resultado
     

 

    def guardar(self, archivo, valor):
        with open(archivo, 'a') as f:
            f.write(f"{valor}\n")
        print("Registro ingresado exitosamente") 

    def consultar_info():    
                print("*** Consulta General ***")
                print("1.- Mostrar Clientes")
                print("2.- Mostrar Facturas")
                print("3.- Mostrar Credito")
                print("4.- Mostrar Pagos")
                print("5.- Regresar al menu principal")



# Programa principal ----------------------------------------------

if __name__ == "__main__":
    opc = ''
    while opc != '6':
        menu = """
        CARTERA DE CLIENTES
        1) Cliente
        2) Factura
        3) Credito
        4) Pagos
        5) Consultas generales
        6) Salir
        """
        print(menu)
        opc = input("Eliga la opción:")
        if opc == "1":
            nombre  = str(input("Ingrese Cliente"))
            cedula = ingreso_cedula("Ingrese Cedula", "Cedula incorrecta")
            estado = True
            cliente = Cliente(nombre,cedula, estado)
            grabar = input("Desea Guardar los datos [s/n]").lower()
            if grabar == "s":
                txt = Archivo("usuarios.txt", "|")
                datos = f"{str(cliente._idCliente)},{cliente.nombre}, {cliente.cedula}, {str(cliente.estado)}"
                txt.guardar("usuarios.txt", datos)
                cliente.mostrarDatos()
            else:
                print("No funciona tu webada")
        elif opc == "2":
            txt = Archivo("usuarios.txt", "|")
            data = txt.mostrar("usuarios.txt")
            datos = data.split(",")
            cliente = Cliente(datos[1], datos[2], datos[3])
            fecha = ingreso_fecha("dd-mm-aa", "Fecha Invalida")
            estado = datos[3]
            print(datos[3])
            total = int(input('Ingrese el total de la factura: $')) 
            factura = Factura(datos[1], fecha, total, estado)
            grabar = input("Desea Guardar los datos [s/n]").lower()
            if grabar == "s":
                txt = Archivo("factura.txt", "|")
                cadenaFactura = f"{str(factura._idfactura)}, {factura.cliente}, {factura.fecha}, {str(factura.total)}, {str(factura.estado)}"
                txt.guardar("factura.txt", cadenaFactura)
            else:
                print("no sirve tu factura de mrd")
            factura.mostrardatos()
        elif opc == "3":      
            txt = Archivo("factura.txt", "|")
            data = txt.mostrar("factura.txt")
            datos = data.split(",")
            factura = f"{datos[1]}, {datos[2]}, {datos[3]}"
            fecha = str(datetime.now().date())
            deuda = int(input('Ingresar el valor de la deuda:$'))
            numeroCuota = int(input('Ingresar el numero de cuotas:$'))
            cuota = int(input('Ingresar el valor de la cuota:$'))
            aammInicial = int(input('Ingresar el saldo inicial$'))
            estado = True
            grabar = input("Desea Guardar los datos [s/n]").lower()
            if grabar == "s":
                archivotxt = Archivo("Credito.txt", "|")
                cabcredito = CabCredito(factura, fecha, deuda, cuota, estado)
                # incluir datos de Detcredito
                
                #Datos de detcredito
                # {cabcredito.addDetCredito(valores para la lista)}

                cadenaCredito = f"{cabcredito.idCabCredito}, {factura}, {fecha}, {deuda}, {numeroCuota}, {cuota}, , {aammInicial}, {estado}"
                archivotxt.guardar("Credito.txt", cadenaCredito)
                cabcredito.MostrarDatos()
            else:
                print("no sirve tu webada")
        
        elif opc == "4":
            valor = float(input("Ingresa el monto a pagar:"))
            fechaPago = datetime.now().date()
            grabar = input("Desea Guardar los datos [s/n]").lower()
            if grabar == "s":
                pago = Pago(fechaPago, valor)
                archivotxt = Archivo("Pago.txt", "|")
                cadenaPago = f"{pago.idPago}, {fechaPago}, {valor}"
                archivotxt.guardar("Pago.txt", cadenaPago)
                pago.mostrarDatos()
                #


                
                txt = Archivo("Credito.txt", "|")
                data = txt.mostrar("Credito.txt")
                datos = data.split(",")
                # DetCredito
                fecha = str(fechaPago)
                aamm = fecha
                detcredito = DetCredito(aamm, datos[6], True)
                detcredito.mostrarDatos()
            else:
                print("sopas")
        
        elif opc == "5":
            consultar_info()
            
            

            

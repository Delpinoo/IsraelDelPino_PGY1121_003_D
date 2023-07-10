from os import system
asientos=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21"
          ,"22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40"
          ,"41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"
          ,"60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78"
          ,"79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97"
          ,"98","99","100"]

reserva=[None]*100
totales=[]
asistentes=[]


platinum = int(120000)
gold     = int(80000)
silver   = int(50000)

def menu():
    print("""
        [1]. Comprar entradas.
        [2]. Mostrar ubicaciones disponbles.
        [3]. Ver listado de asistencias.
        [4]. Mostrar ganancias totales.
        [5]. Salir.
        """)

def pausa():
    input("Ingrese una opcion para continuar....")
    system("cls")

def cant_max_mini(cant_entradas):
    while cant_entradas >= 1 and cant_entradas <= 3:
        print(asientos)
        break
    else:
        print("debe ingresar un minimo de 1 o un maximo de 3 !!!")

def buy_entradas():
    pass
def salir():
    input("Precione cualquier tecla para salir.....")
    return

def selec_asiento(asiento_selec):
    while True:
        if asiento_selec in "123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100" and len(asiento_selec)== 1 or 2 or 3 and asientos[int(asiento_selec)-1 or 2 or 3]!="X":
            asientos[int(asiento_selec)-1 or 2 or 3]="X"
            reserva[int(asiento_selec)-1 or 2 or 3]=None
            print("asiento reservdo con exito!!!")
            break
        else:
            print("Sala invaida o esta ocupada!!!")

def tipo_asiento(asiento_selec):
    if asiento_selec in "1234567891011121314151617181920":
        print("Usted selecciono una entrada Platinumque van del asiento 1 al 20, el calor de las platinum son de : $120000 c/u")
        suma1 = cant_entradas * platinum
        totales.append(suma1)
        print(f" el total a cancelar es de : ${suma1}")
    
    elif asiento_selec in "21222324252627282930313233343536373839404142434454647484950":
        print("Usted selecciono una entrada gol que van del asiento 21 al 50, el valor de las gol son de : $80000 c/u")
        suma2 = cant_entradas * gold
        totales.append(suma2)
        print(f"el total a cancelar es de : ${suma2}")
    elif asiento_selec in "51525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100":
        print("Usted seleccionó entrada/s silver que van del asiento 51 al 100, el valor de las silver son de : $50000 c/u ")
        suma3 = cant_entradas * silver
        totales.append(suma3)
        print(suma3)

def disponibilidad():
    for i in range (len(asientos)):
        if reserva[i]!=None:
            print(f"{i+1}  -  RUT= {rut_o}")



def recaudacion(totales):
    return sum(totales)


while True:
    menu()
    op=str(input("Ingrese una opcion: "))
    match op:
        case "1":
            cant_entradas=int(input("cuantas entradas desea comprar?: "))
            cant_max_mini(cant_entradas)
            for i in range(cant_entradas):
                asiento_selec=str(input("Ingrese el puesto o los puestos que desee: "))
                selec_asiento(asiento_selec)
                tipo_asiento(asiento_selec)
            rut_o=str(input("Ingrese su rut: "))
            rut_o=rut_o.replace(".","").replace("-123456789kK","")
            asistentes.append(rut_o)
            print(asientos)
        case "2":
            print(asientos)
            disponibilidad()
        case "3":
            print(asistentes)
        case "4":
            print(recaudacion(totales))
        case "5":
            salir()
        case other:
            print("opcion no valida!!!")

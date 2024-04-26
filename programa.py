list_programacion = []
list_rutas = []
import os

def fnt_limpiar():
    os.system('cls')
    print('NOMBRE DEL PROGRAMA: <<GEASTION DE RUTAS>>')
    print('AUTOR: <<Mateo Ochoa>>')
    print('AÑO: <<2024>>')
    print('UNIVESIDAD CATOLICA LUISA AMIGO\n')

def fnt_agregar_ruta():
    cod = input('CODIGO:   ')
    nombre = input('NOMBRE:   ')
    descripcion = input('DESCRIPCIÓN:   ')
    r = cod + '' + nombre + '' + descripcion
    list_rutas.append(r)
    input('\nRuta registrada con éxito <<ENTER>>')
    
def fnt_consultar_rutas():
    fnt_limpiar()
    print('\n<<< CONSULTAR RUTAS >>>\n')
    if len(list_rutas) == 0:
        print('\nNo hay rutas registradas')
    else:
        for i in range(0, len(list_rutas)):
            print(list_rutas[i])
    input('\nFIN DEL REGISTRO <ENTER>')

sw2 = True

def fnt_menu_rutas():
    global sw2
    while sw2 == True:
        fnt_limpiar()
    opcion_r = input('<<MENU RUTAS>>\n1. AGREGAR\n2. CONSULTAR\n3. SALIR\n->')
    if opcion_r == '1':
        fnt_agregar_ruta()
    if opcion_r == '2':
        fnt_consultar_rutas()
    if opcion_r == '3':
        sw2 = False
        
    sw3 = True
    def fnt_menu_envios():
        global sw3
        while sw3 == True:
            fnt_limpiar()
            opcion3 = input('<<< MENU ENVIOS >>>\n1. AGREGAR \n2. CONSULTAR\n3. SALIR\n->')
            if opcion3 == '1':
                
def fnt_envio():
    fnt_limpiar()
    print('<<< RUTAS DISPONIBLES >>>\n')
    for i in range(len(list_rutas)):
        print('<<< DATOS DEL ENVIO >>>\n')
        n_envio = input('NUMERO DE ENVÍO:  ')
        nombre = input('NOMBRE DEL CLIENTE:  ')
        valor = input('VALOR $:   ')
        peso = input('PESO DE LA MERCANCÍA:  ')
        ruta = input('RUTA:   ')
        r = 'ENVIO No.'
  
sw = True
while sw == True:
    fnt_limpiar()
    opcionStr = input('<<')
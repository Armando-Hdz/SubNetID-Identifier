import sys

def dec_Bin(d):
    bin(d)
    binary = int(bin(d)[2:])
    return binary

def decimalBinaryOctet(_decimal):
    decimal = _decimal
    binario = [0, 0, 0, 0, 0, 0, 0, 0]
    if decimal >= 0 and decimal <= 255:
        if decimal >= 128:
            binario[0] = 1
            decimal -= 128
        else:
            binario[0] = 0
        if decimal >= 64:
            binario[1] = 1
            decimal -= 64
        else:
            binario[1] = 0
        if decimal >= 32:
            binario[2] = 1
            decimal -= 32
        else:
            binario[2] = 0
        if decimal >= 16:
            binario[3] = 1
            decimal -= 16
        else:
            binario[3] = 0
        if decimal >= 8:
            binario[4] = 1
            decimal -= 8
        else:
            binario[4] = 0
        if decimal >= 4:
            binario[5] = 1
            decimal -= 4
        else:
            binario[5] = 0
        if decimal >= 2:
            binario[6] = 1
            decimal -= 2
        else:
            binario[6] = 0
        if decimal >= 1:
            binario[7] = 1
            decimal -= 1
        else:
            binario[7] = 0
    return binario

def SNID(_binaryNetEndOctet,_binarySbNetMaskEndOctet):
    binario = _binaryNetEndOctet;
    mascara = _binarySbNetMaskEndOctet
    snid = [0, 0, 0, 0, 0, 0, 0, 0]
    for i, j in enumerate(snid):
        if binario[i] == 1 and mascara[i] == 1:
            snid[i] = 1
    print("SNID binario: 11111111.11111111.11111111.", *snid)

    dec = 0
    exp = 7
    for i, j in enumerate(snid):
        if snid[i] == 1:
            dec += 2 ** exp
        exp -= 1
    print("SNID decimal: 255.255.255." + str(dec))

def repetir():
    print("¿Desea realizar otra opcion?")
    print("1.- Si")
    print("2.- No")

print("Desarrollado por María Elizabeth Jiménez Trujillo")

def desarrollo():
    print("2.- Convertir decimal a binario")
    print("3.- Obtener SNID de una IP y mascara clase C")
    print("4.- Saludo")
    print("5.- Salir")

    option = int(input("Ingrese una opción: "))

    if(option >= 1 and option <=5):
        if(option != 1):

            while option == 2:
                dec = int(input("Ingrese numero decimal: "))
                print(dec_Bin(dec))
                repetir()
                rep = int(input("Ingresa opcion: "))
                if rep == 1:
                    desarrollo()
                elif rep == 2:
                    sys.exit("Gracias por usar este codigo ")
                break

            while option == 3:
                octet1 = (int(input("Ingresa el valor del primer octeto: ")))

                if(octet1 >= 192 and octet1 <= 223):
                    octetBin1 = decimalBinaryOctet(octet1)
                    octet2 = (int(input("Ingresa el valor del segundo octeto: ")))
                    octetBin2 = decimalBinaryOctet(octet2)
                    octet3 = (int(input("Ingresa el valor del tercer octeto: ")))
                    octetBin3 = decimalBinaryOctet(octet3)
                    octet4 = (int(input("Ingresa el valor del segundo octeto: ")))
                    octetBin4 = decimalBinaryOctet(octet4)
                else:
                    print(f'Lo lamento, una ip de clase c va de 192 a 223 y el {octet1} está fuera de rango')

                sbNetMask = (int(input("Ingresa una mascara de subred: 255.255.255.")))
                if(sbNetMask >=0 and sbNetMask <= 255):
                    sbNetMaskBin = decimalBinaryOctet(sbNetMask)
                    print(f'La mascara ingresada es: 255.255.255.{sbNetMask}')
                    print(f'IP decimal: {octet1}.{octet2}.{octet3}.{octet4}')
                    print(f'IP binario: ',*octetBin1,'.',*octetBin2,'.',*octetBin3,'.',*octetBin4)
                    print(f'Mascara de subred decimal: 255.255.255.{sbNetMask}')
                    print(f'Mascara de subred binario: 11111111.11111111.11111111.',*sbNetMaskBin)
                else:
                    print(f'Error de mascara, recuerda que la mascara de red clase c va de 255.255.255.0 a 255.255.255.255')

                SNID(octetBin4,sbNetMaskBin)
                repetir()
                rep = int(input("Ingresa opcion: "))
                if rep == 1:
                    desarrollo()
                elif rep == 2:
                    sys.exit("Gracias por usar este codigo ")
                break

            while option == 4:
                nombre = input("¿Cual es tu nombre? ")
                saludo = "*** Hola es un gusto conocerte "
                print(saludo, nombre, " ***")
                repetir()
                rep = int(input("Ingresa opcion: "))
                if rep == 1:
                    desarrollo()
                elif rep == 2:
                    sys.exit("Gracias por usar este codigo ")
                break

            while option == 5:
                sys.exit("Gracias por usar este codigo")
                break
        else:
            print(f'Error, {option} no es una opción')
    else:
        print(f'Error, {option} no es una opción')

desarrollo()
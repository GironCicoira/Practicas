bancoCliente="Santander"
cuentaCliente=True
saldoCliente=1100000
bancoDestino="Galicia"
cuentaDestino=True
hora=8

if (((hora<9) or (hora>12)) and ((hora<15) or (hora>20))):
    print ("Fuera de horario bancario, nuetro horario es de 9 a 12 y de 15 a 20")


if (((cuentaCliente==True) and (cuentaDestino==True)) and (((hora>=9) and (hora<=12)) or ((hora>=15) and (hora<=20)))):
    print ("Sus cuentas han sido validadas")
    if (bancoCliente==bancoDestino):
        comision=0
        if (saldoCliente>=(1000000+comision)):
            print ("La transferencia se realizo exitosamente")
            print ("La comision es de 0")
        else:
            print ("El saldo del cliente es insuficiente")

    else:
        comision=100
        if (saldoCliente<(1000000+comision)):
            print ("El saldo del cliente es insuficiente")
        else:
            print ("La transferencia se realizo exitosamente")
            print ("La comision es de 0")

else:
    if ((cuentaCliente==False) and (cuentaDestino==False)):
        print ("no tienes ningunas de las cuentas validadas")
    if ((cuentaCliente==False) and (cuentaDestino==True)):
        print("La cuenta del cliente no esta verificada")
    if ((cuentaCliente==True) and (cuentaDestino==False)):
        print("La cuenta del destino no esta verificada")



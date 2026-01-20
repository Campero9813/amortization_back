def calcular_tabla_frances(monto, tasa_anual, plazo_meses):
    #Convetir tasa anual a mensual
    tasa_mensual = tasa_anual / 12 / 100
    #Calcular cuota fija mensual
    cuota = monto * (
        tasa_mensual * (1 + tasa_mensual) ** plazo_meses
    ) / ((1 + tasa_mensual) ** plazo_meses -1)

    saldo = monto
    tabla = []

    for mes in range(1, plazo_meses + 1):
        #Calcular interes
        interes = saldo * tasa_mensual
        #Calcular capital
        capital = cuota - interes
        #Reducir saldo 
        saldo -= capital


        #Validacion para evitar saldo negativo en el ultimo pago
        if mes == plazo_meses:
            capital += saldo
            cuota = capital + interes
            saldo = 0

        tabla.append({
            "periodo": mes,
            "cuota": round(cuota, 2),
            "interes": round(interes, 2),
            "capital": round(capital, 2),
            "saldo": round(max(saldo,0), 2)
        })

    return tabla
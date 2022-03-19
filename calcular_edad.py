"""
//Hacer un programa que recibe la fecha de nacimiento de una persona en 3 entradas: día, mes, año; el programa regresa la edad de la persona

^- Valida entrada
^- Maneja adecuadamente excepciones
"""
from calendar import isleap
import argparse
import datetime


def __process_input__numeric__(value: int):
    """
    Convierte una cadena a un número entero, regresa None en caso de no ser posible la conversión
    Arguments:
    value: str
    returns: int || None
    """
    if value.isnumeric():
        return int(value)
    else:
        return None


def __process_month_string__(value: str):
    """
    Procesa si la cadena es alfánumerica; comprueba que esta coincida con algún mes
    """
    months = {
        "enero": 1,
        "febrero": 2,
        "marzo": 3,
        "abril": 4,
        "mayo": 5,
        "junio": 6,
        "julio": 7,
        "agosto": 8,
        "septiembre": 9,
        "octubre": 10,
        "noviembre": 11,
        "diciembre": 12
    }
    if value.isalpha():
        for month in months:
            if value == month:
                return int(months[month])
    else:
        return None


def __validate_inputs__(dia: int, mes: str, anio: int):
    dia = __process_input__numeric__(dia)
    mes = __process_month_string__(mes)
    anio = __process_input__numeric__(anio)
    try:
        return {"dia": int(dia), "mes": int(mes), "anio": int(anio)}
    except:
        print('El o los argumentos son invalidos')


def __current_date__():
    date = datetime.datetime.now()
    return date


def __validate_data__(data):
    """
    Validación de datos de entrada
    Arguments:
    data: dia: int, mes: int, anio: int
    returns:
    dia: int, mes: int, anio: int (validados)
    Validación de meses:
    *Tienen 31 días: enero = 1, marzo = 3, mayo = 5, julio = 7, agosto = 8, octubre = 10, diciembre = 12.
    ^Tienen 30 días: abril 4, junio 6, septiembre 9, noviembre 11.
    //Tienen 28 días: febrero.
    """
    anio_actual = int(__current_date__().strftime("%Y"))
    dia, mes, anio = data['dia'], data['mes'], data['anio']
    # * Validar meses
    validar_meses_31 = ((mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 10) or (mes == 12))
    validar_meses_30 = ((mes == 4) or (mes == 6) or (mes == 9) or (mes == 11))
    validar_mes_28 = (mes == 2)
    # * Validar año
    validar_anio = (anio > 1902 and anio < anio_actual)
    # * Año bisiesto
    bisiesto = isleap(anio)
    if (bisiesto):
        if (validar_mes_28) and (dia > 0 and dia <= 29) and (validar_anio):
            print('Bisiesto', anio)
            return {"dia": dia, "mes": mes, "anio": anio}
        elif (validar_meses_31) and (dia > 0 and dia <= 31) and (validar_anio):
            return {"dia": dia, "mes": mes, "anio": anio}
        elif (validar_meses_30) and ((dia > 0 and dia <= 30)) and (validar_anio):
            return {"dia": dia, "mes": mes, "anio": anio}
        else:
            print('Verifica los datos ingresados')
            print(f'Día: {dia} - Mes: {mes}° - Año: {anio}')
            exit(1)
    else:
        if (validar_mes_28) and (dia > 0 and dia <= 28) and (validar_anio):
            return {"dia": dia, "mes": mes, "anio": anio}
        elif (validar_meses_31) and (dia > 0 and dia <= 31) and (validar_anio):
            return {"dia": dia, "mes": mes, "anio": anio}
        elif (validar_meses_30) and ((dia > 0 and dia <= 30)) and (validar_anio):
            return {"dia": dia, "mes": mes, "anio": anio}
        else:
            print('Verifica los datos ingresados')
            print(f'Día: {dia} - Mes: {mes} ° - Año: {anio}')
            exit(1)


def __leap_years_(anio, anio_actual):
    count_anios = 0
    for anios in range(anio, anio_actual):
        if isleap(anios):
            count_anios += 1
    return count_anios

def calculate_age(data_validate):
    dia, mes, anio = data_validate['dia'], data_validate['mes'], data_validate['anio']
    dia_actual, mes_actual, anio_actual = int(__current_date__().strftime("%d")), int(__current_date__().strftime("%m")), int(__current_date__().strftime("%Y"))
    # * Día actual
    if isleap(anio) and dia == 29 and mes == 2:
        print('Tu edad actual es:', __leap_years_(anio, anio_actual), 'años')
    if mes == mes_actual and dia == dia_actual:
        print('Tu edad actual es: ', anio_actual - anio, 'años')
        exit(0)
    if (mes > mes_actual) or (mes == mes_actual) and dia > dia_actual:
        print('Tu edad actual es:', (anio_actual - 1) - anio, 'años')
        exit(0)
    if mes < mes_actual:
        print('Tu edad actual es:', anio_actual - anio, 'años')
        exit(0)


if __name__ == '__main__':
    all_args = argparse.ArgumentParser()
    all_args.add_argument("-d",
                          "--dia",
                          # type=int,
                          help="Indica tu día de nacimiento",
                          required=True
                          )
    all_args.add_argument("-m",
                          "--mes",
                          help="Indica tu mes de nacimiento",
                          required=True
                          )
    all_args.add_argument("-a",
                          "--anio",
                          # type=int,
                          help="Indica tu año de nacimiento",
                          required=True
                          )
    args = vars(all_args.parse_args())
    # //Procesando entradas de tipo numericas
    if (__validate_inputs__(args['dia'], args['mes'], args['anio'])):
        data = __validate_inputs__(args['dia'], args['mes'], args['anio'])
        calculate_age(__validate_data__(data))

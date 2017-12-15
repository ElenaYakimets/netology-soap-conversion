import osa
from math import ceil


def get_values(path):
    with open(path, 'r') as f:
        data = f.readlines()

    return data


def get_cost_rub(path):
    data = get_values(path)
    money_spent = 0

    for line in data:
        amount, currency = line.split()[1:]
        converted = convert_curr(amount, currency)
        money_spent += converted

    return ceil(money_spent)


def get_avg_temps(path):
    data = get_values(path)
    temps = []

    for line in data:
        amount = line.split()[0]
        temps.append(float(amount))

    avg_temp = convert_temp(sum(temps) / len(temps))
    return '{:.2f}'.format(avg_temp)


def get_sum_dist(path):
    data = get_values(path)
    dist_travelled = 0

    for line in data:
        distance = float(line.split()[1].replace(',', ''))
        dist_travelled += distance

    return '{:.2f}'.format(convert_dist(dist_travelled))


# конверции
def convert_curr(value, from_currency):
    client = osa.Client('http://fx.currencysystem.com/'
                        'webservices/CurrencyServer4.asmx?WSDL')
    conversion = from_currency, 'RUB'

    return client.service.ConvertToNum(None, *conversion, value, False)


def convert_temp(value):
    client = osa.Client('http://www.webservicex.net/'
                        'ConvertTemperature.asmx?WSDL')
    conversion = 'degreeFahrenheit', 'degreeCelsius'

    return client.service.ConvertTemp(value, *conversion)


def convert_dist(value):
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    conversion = 'Miles', 'Kilometers'

    return client.service.ChangeLengthUnit(value, *conversion)


def main():
    print('Средняя температура:', get_avg_temps('temps.txt'), 'C')
    print('Сумма цен билетов:', get_cost_rub('currencies.txt'), 'руб.')
    print('Суммарное расстояние:', get_sum_dist('travel.txt'), 'км.')


main()

from decimal import Decimal


class HourTooLowError(Exception):
    pass


class HourTooHighError(Exception):
    pass


rates = {'Chico': Decimal('0.5'),
         'Groucho': Decimal('0.7'),
          'Harpo': Decimal('0.5'),
          'Zeppo': Decimal('0.4')}


def time_percentage(hour):
    return hour / Decimal('0.24')


def calculate_tax(sum_of_purchase, province, hour):
    if hour < 0:
        raise HourTooLowError(f'Hour of {hour} is < 0')
    if hour > 24:
        raise HourTooHighError(f'Hour of {hour} is >= 24')
    return float(sum_of_purchase + (sum_of_purchase * rates[province] * time_percentage(hour)))

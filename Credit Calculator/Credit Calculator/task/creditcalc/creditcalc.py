import math
import sys


def annuity_count_of_months(p, a, ci):
    """"
    :param p: - principal
    :param a: - payment
    :param ci: - interest
    """
    i = ci / (12 * 100)
    n = math.log(a / (a - i * p), 1 + i)
    n = math.ceil(n)
    if n // 12 == 0:
        if n % 12 == 1:
            print('You need 1 month to repay this credit!')
        elif n % 12 > 1:
            print('You need {0} months to repay this credit!'.format(n % 12))
    elif n // 12 == 1:
        if n % 12 == 0:
            print('You need 1 year to repay this credit!')
        elif n % 12 == 1:
            print('You need 1 year and 1 month to repay this credit!')
        else:
            print('You need 1 year and {0} months to repay this credit!'.format(n % 12))
    else:
        if n % 12 == 0:
            print('You need {0} years to repay this credit!'.format(n // 12))
        elif n % 12 == 1:
            print('You need {0} years and 1 month to repay this credit!'.format(n // 12))
        else:
            print('You need {0} years and {1} months to repay this credit!'.format(n // 12, n % 12))
    print("Overpayment = " + str(n * a - p))


def annuity_monthly_payment(p, n, ci):
    """
    :param p: - principal
    :param n: - periods
    :param ci: - interest
    """
    i = ci / (12 * 100)
    a = (p * i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)
    a = math.ceil(a)
    print('Your annuity payment = {0}!'.format(a))
    print("Overpayment = " + str(a * n - p))


def annuity_credit_principal(a, n, ci):
    """
    :param a: - payment
    :param n: - periods
    :param ci: - interest
    """
    i = ci / (12 * 100)
    p = a / (i * math.pow(1 + i, n) / (math.pow(1 + i, n) - 1))
    p = math.floor(p)
    print('Your credit principal = {0}!'.format(p))
    print("Overpayment = " + str(a * n - p))


def differential_payment(p, n, ci):
    """
    :param p: - principal
    :param n: - periods
    :param ci: - interest
    """
    i = ci / (12 * 100)
    total = 0
    for m in range(1, n + 1):
        d = p / n + i * (p - (p * (m - 1)) / n)
        d = math.ceil(d)
        total += d
        print("Month {0}: paid out {1}".format(m, d))
    print()
    print("Overpayment = " + str(total - principal))


list_parameters = sys.argv
list_parameters.remove(list_parameters[0])
if len(list_parameters) != 4:
    print("Incorrect parameters.")
    sys.exit()
payment = -1
periods = -1
interest = -1
principal = -1
parameters_checksum = 0
for param in list_parameters:
    if param == '--type=diff':
        parameters_checksum += 10000
    elif param == '--type=annuity':
        parameters_checksum += 20000
    else:
        param_split = param.split('=')
        if float(param_split[1]) < 0:
            print("Incorrect parameters.")
            sys.exit()
        else:
            if param_split[0] == '--payment':
                payment = int(param_split[1])
                parameters_checksum += 1000
            elif param_split[0] == '--principal':
                principal = int(param_split[1])
                parameters_checksum += 100
            elif param_split[0] == '--periods':
                periods = int(param_split[1])
                parameters_checksum += 10
            elif param_split[0] == '--interest':
                interest = float(param_split[1])
                parameters_checksum += 1
if parameters_checksum == 21101:
    annuity_count_of_months(principal, payment, interest)
elif parameters_checksum == 20111:
    annuity_monthly_payment(principal, periods, interest)
elif parameters_checksum == 21011:
    annuity_credit_principal(payment, periods, interest)
elif parameters_checksum == 10111:
    differential_payment(principal, periods, interest)
else:
    print("Incorrect parameters.")

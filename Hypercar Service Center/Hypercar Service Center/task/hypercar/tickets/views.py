from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render


class CarLine:
    ticket = 0
    line_of_cars = {}
    current_process_ticket = 0

    def __init__(self, timer):
        CarLine.ticket += 1
        self.order = CarLine.ticket
        self.wait_time = self.set_wait_time()
        CarLine.line_of_cars[CarLine.ticket] = timer

    def get_order_number(self):
        return self.order

    def set_wait_time(self):
        if len(CarLine.line_of_cars) < 2:
            return 0
        elif len(CarLine.line_of_cars) == 2:
            return min(list(CarLine.line_of_cars.values())[0], list(CarLine.line_of_cars.values())[1])
        else:
            return list(CarLine.line_of_cars.values()).count(2) * 2 +\
                   list(CarLine.line_of_cars.values()).count(5) * 5 +\
                   list(CarLine.line_of_cars.values()).count(30) * 30

    def get_order_time(self):
        return self.wait_time


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<http><head></head><body><h2>Welcome to the Hypercar Service!</h2></body></http>')


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'menu.html')


class TiresView(View):
    def get(self, request, *args, **kwargs):
        order = {}
        a = CarLine(5)
        order['number'] = a.get_order_number()
        order['minutes'] = a.get_order_time()
        return render(request, 'order.html', {'order': order})


class OilView(View):
    def get(self, request, *args, **kwargs):
        order = {}
        a = CarLine(2)
        order['number'] = a.get_order_number()
        order['minutes'] = a.get_order_time()
        return render(request, 'order.html', {'order': order})


class DiagnosticView(View):
    def get(self, request, *args, **kwargs):
        order = {}
        a = CarLine(30)
        order['number'] = a.get_order_number()
        order['minutes'] = a.get_order_time()
        return render(request, 'order.html', {'order': order})


class ProcessView(View):
    def get(self, request, *args, **kwargs):
        process = {}
        oil_count = list(CarLine.line_of_cars.values()).count(2)
        tires_count = list(CarLine.line_of_cars.values()).count(5)
        diagnostic_count = list(CarLine.line_of_cars.values()).count(30)
        process['oil_count'] = oil_count
        process['tires_count'] = tires_count
        process['diagnostic_count'] = diagnostic_count
        return render(request, 'process.html', {'process': process})

    def post(self, request, *args, **kwargs):
        if 2 in CarLine.line_of_cars.values():
            for key, value in CarLine.line_of_cars.items():
                if value == 2:
                    CarLine.current_process_ticket = key
                    break
        elif 5 in CarLine.line_of_cars.values():
            for key, value in CarLine.line_of_cars.items():
                if value == 5:
                    CarLine.current_process_ticket = key
                    break
        elif 30 in CarLine.line_of_cars.values():
            for key, value in CarLine.line_of_cars.items():
                if value == 30:
                    CarLine.current_process_ticket = key
                    break

        if CarLine.current_process_ticket != 0:
            CarLine.line_of_cars[CarLine.current_process_ticket] = 0
#            CarLine.line_of_cars.pop(CarLine.current_process_ticket)

        process = {}
        oil_count = list(CarLine.line_of_cars.values()).count(2)
        tires_count = list(CarLine.line_of_cars.values()).count(5)
        diagnostic_count = list(CarLine.line_of_cars.values()).count(30)
        process['oil_count'] = oil_count
        process['tires_count'] = tires_count
        process['diagnostic_count'] = diagnostic_count
        return render(request, 'process.html', {'process': process})


class NextView(View):
    def get(self, request, *args, **kwargs):
        nxt = {}
        if CarLine.current_process_ticket != 0:
            nxt['next'] = 'Next ticket #{}'.format(CarLine.current_process_ticket)
        else:
            nxt['next'] = 'Waiting for the next client'
        return render(request, 'next.html', {'nxt': nxt})

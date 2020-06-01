from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
import json


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        html = "<h2>Welcome to the Hypercar Service!</h2>"
        return HttpResponse(html)


class MenuView(View):
    menu = {
        'change_oil': 'Change oil',
        'inflate_tires': 'Inflate tires',
        'diagnostic': 'Diagnostic',
    }

    def get(self, request, *args, **kwargs):
        return render(request, 'tickets/menu.html', context={'menu': self.menu})


class GetTicketCO(View):

    def get(self, request, *args, **kwargs):
        data = {'t': 0, 'co': 0, 'it': 0, 'd': 0, 'n_t': 0, 'list_co': [], 'list_it': [], 'list_d': []}
        try:
            with open('data.json') as f:
                data = json.load(f)
        except FileNotFoundError:
            with open('data.json', 'w') as f:
                json.dump(data, f)
        data['t'] += 1
        data['co'] += 1
        with open('data.json', 'w') as f:
            json.dump(data, f)
        t = data['t']
        co = data['co']
        it = data['it']
        d = data['d']
        min = (co - 1) * 2
        data['list_co'].append(t)
        with open('data.json', 'w') as f:
            json.dump(data, f)
        return render(request, 'tickets/ticket.html',
                      context={'op': 'Change oil', 'num': t, 'min': min})


class GetTicketIT(View):

    def get(self, request, *args, **kwargs):
        data = {'t': 0, 'co': 0, 'it': 0, 'd': 0, 'n_t': 0, 'list_co': [], 'list_it': [], 'list_d': []}
        try:
            with open('data.json') as f:
                data = json.load(f)
        except FileNotFoundError:
            with open('data.json', 'w') as f:
                json.dump(data, f)
        data['t'] += 1
        data['it'] += 1
        with open('data.json', 'w') as f:
            json.dump(data, f)
        t = data['t']
        co = data['co']
        it = data['it']
        d = data['d']
        min = co * 2 + (it - 1) * 5
        data['list_it'].append(t)
        with open('data.json', 'w') as f:
            json.dump(data, f)
        return render(request, 'tickets/ticket.html',
                      context={'op': 'Inflate tires', 'num': t, 'min': min})


class GetTicketD(View):

    def get(self, request, *args, **kwargs):
        data = {'t': 0, 'co': 0, 'it': 0, 'd': 0, 'n_t': 0, 'list_co': [], 'list_it': [], 'list_d': []}
        try:
            with open('data.json') as f:
                data = json.load(f)
        except FileNotFoundError:
            with open('data.json', 'w') as f:
                json.dump(data, f)
        data['t'] += 1
        data['d'] += 1
        with open('data.json', 'w') as f:
            json.dump(data, f)
        t = data['t']
        co = data['co']
        it = data['it']
        d = data['d']
        min = co * 2 + it * 5 + (d - 1) * 30
        data['list_d'].append(t)
        with open('data.json', 'w') as f:
            json.dump(data, f)
        return render(request, 'tickets/ticket.html',
                      context={'op': 'Diagnostic', 'num': t, 'min': min})


class Processing(View):

    def get(self, request, *args, **kwargs):
        data = {'t': 0, 'co': 0, 'it': 0, 'd': 0, 'n_t': 0, 'list_co': [], 'list_it': [], 'list_d': []}
        try:
            with open('data.json') as f:
                data = json.load(f)
        except FileNotFoundError:
            with open('data.json', 'w') as f:
                json.dump(data, f)
        t = data['t']
        co = data['co']
        it = data['it']
        d = data['d']
        return render(request, 'tickets/processing.html',
                      context={'CO': co, 'IT': it, 'D': d})

    def post(self, request, *args, **kwargs):
        data = {'t': 0, 'co': 0, 'it': 0, 'd': 0, 'n_t': 0, 'list_co': [], 'list_it': [], 'list_d': []}
        try:
            with open('data.json') as f:
                data = json.load(f)
        except FileNotFoundError:
            with open('data.json', 'w') as f:
                json.dump(data, f)

        if len(data['list_co']) > 0:
            data['n_t'] = data['list_co'][0]
            data['list_co'].remove(data['n_t'])
            data['co'] -= 1
            with open('data.json', 'w') as f:
                json.dump(data, f)
        elif len(data['list_it']) > 0:
            data['n_t'] = data['list_it'][0]
            data['list_it'].remove(data['n_t'])
            data['it'] -= 1
            with open('data.json', 'w') as f:
                json.dump(data, f)
        elif len(data['list_d']) > 0:
            data['n_t'] = data['list_d'][0]
            data['list_d'].remove(data['n_t'])
            data['d'] -= 1
            with open('data.json', 'w') as f:
                json.dump(data, f)
        else:
            data['n_t'] = 0
            with open('data.json', 'w') as f:
                json.dump(data, f)
        return redirect('/processing')


class Next(View):

    def get(self, request, *args, **kwargs):
        data = {'t': 0, 'co': 0, 'it': 0, 'd': 0, 'n_t': 0, 'list_co': [], 'list_it': [], 'list_d': []}
        try:
            with open('data.json') as f:
                data = json.load(f)
        except FileNotFoundError:
            with open('data.json', 'w') as f:
                json.dump(data, f)
        return render(request, 'tickets/next.html',
                      context={'next_ticket': data['n_t']})

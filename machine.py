import re
import json
import cart
import ticket
import payment

class Ticket_machine:
    def __init__(self):
        self.cart = cart.Cart()
        with open("prices.json", "r", encoding="UTF-8") as jf:
            self.prices = json.load(jf)
    def choose_ticket(self, menu, category=None, group=None) -> ticket.Ticket:
        print("Jaki rodzaj biletu chcesz kupić? ")
        options = list(menu.keys())
        for index, option in enumerate(options):
            print(f"{index} - {option}")
        try:
            choice = int(input("Wybór: "))
        except ValueError:
            print("Wprowadzono niepoprawny typ wartości.")
            return self.choose_ticket(menu, category, group)
        if choice > len(options)-1 or choice < 0:
            print("Wprowadzono błędny numer opcji.")
            return self.choose_ticket(menu, category, group)
        menu = menu[options[choice]]
        if isinstance(menu, dict):
            if category:
                group = options[choice]
            else:
                category = options[choice]
            return self.choose_ticket(menu, category, group)
        else: 
            return ticket.Ticket(category, group, options[choice], menu)
    def add_tickets(self):
        add_another = 't'
        while add_another.lower()=='t':
            self.cart.add_ticket(self.choose_ticket(self.prices))
            add_another = input("Czy chcesz dodać kolejny bilet (t/n)? ")
    def run(self):
        self.add_tickets()
        self.cart.display()
        payment.Payment_method(self.cart.get_value()).process_payment()
        input("Drukowanie biletów. Proszę czekać...")
        print("Dziękujemy za skorzystanie z automatu biletowego. Zapraszamy ponownie")




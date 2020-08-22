# Write your code here
import random
import sqlite3


def main_menu(bank):
    while True:
        print('1. Create an account')
        print('2. Log into account')
        print('0. Exit')
        main_choose = input()
        print()
        if main_choose == '0':
            print('Bye!')
            return
        elif main_choose == '1':
            bank.create_account()
        elif main_choose == '2':
            print('Enter your card number:')
            card_number = input()
            print('Enter your PIN:')
            pin_code = input()
            print()
            if bank.check_account(card_number, pin_code):
                print('You have successfully logged in!')
                print()
                while True:
                    print('1. Balance')
                    print('2. Add income')
                    print('3. Do transfer')
                    print('4. Close account')
                    print('5. Log out')
                    print('0. Exit')
                    logged_choose = input()
                    print()
                    if logged_choose == '0':
                        print('Bye!')
                        return
                    elif logged_choose == '1':
                        print('Balance: {}'.format(bank.get_balance(card_number)))
                        print()
                    elif logged_choose == '2':
                        print('Enter income:')
                        income_money = int(input())
                        bank.add_income(card_number, income_money)
                        print('Income was added!')
                        print()
                    elif logged_choose == '3':
                        print('Transfer')
                        print('Enter card number')
                        transfer_card_number = input()
                        if card_number_check(transfer_card_number):
                            if bank.check_card_in_database(transfer_card_number):
                                print('Enter how much money you want to transfer:')
                                transfer_money = int(input())
                                if transfer_money > bank.get_balance(card_number):
                                    print('Not enough money!')
                                    print()
                                else:
                                    bank.add_income(card_number, 0 - transfer_money)
                                    bank.add_income(transfer_card_number, transfer_money)
                                    print('Success!')
                                    print()
                            else:
                                print('Such a card does not exist.')
                                print()
                        else:
                            print('Probably you made mistake in the card number. Please try again!')
                            print()
                    elif logged_choose == '4':
                        bank.delete_account(card_number)
                        print('The account has been closed!')
                        print()
                        break
                    elif logged_choose == '5':
                        print('You have successfully logged out!')
                        print()
                        break
            else:
                print('Wrong card number or PIN!')
                print()


def generate_card_number():
    new_card_number = '400000'
    for _ in range(9):
        new_card_number += str(random.randint(1, 9))
    summa = 0
    for i in range(0, len(new_card_number)):
        if i % 2 == 0:
            temp_value = int(new_card_number[i]) * 2
            if temp_value < 10:
                summa += temp_value
            else:
                summa += (temp_value - 9)
        else:
            summa += int(new_card_number[i])
    if summa % 10 == 0:
        new_card_number += '0'
    else:
        new_card_number += str(10 - summa % 10)
    return new_card_number


def card_number_check(card):
    number_body = card[0:15]
    number_checksum = card[15]
    summa = 0
    for i in range(0, len(number_body)):
        if i % 2 == 0:
            temp_value = int(number_body[i]) * 2
            if temp_value < 10:
                summa += temp_value
            else:
                summa += (temp_value - 9)
        else:
            summa += int(number_body[i])
    if summa % 10 == 0:
        summa = '0'
    else:
        summa = str(10 - summa % 10)
    return summa == number_checksum


class Bank:
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()

    def check_card_in_database(self, card):
        self.cur.execute("select * from card where number='{}';".format(card))
        records = self.cur.fetchall()
        return len(records) > 0

    def create_account(self):
        card = generate_card_number()
        while self.check_card_in_database(card):
            card = generate_card_number()
        pin = ''
        for _ in range(4):
            pin += str(random.randint(1, 9))
        self.cur.execute("insert into card(number, pin, balance) values ('{}', '{}', {});".format(card, pin, 0))
        self.conn.commit()
        print('Your card has been created')
        print('Your card number:')
        print(card)
        print('Your card PIN:')
        print(pin)
        print()

    def check_account(self, card, pin):
        self.cur.execute("select * from card where number='{}' and pin='{}';".format(card, pin))
        records = self.cur.fetchall()
        return len(records) > 0

    def get_balance(self, card):
        self.cur.execute("select balance from card where number='{}';".format(card))
        records = self.cur.fetchall()
        return records[0][0]

    def delete_account(self, card):
        self.cur.execute("delete from card where number='{}'".format(card))
        self.conn.commit()

    def add_income(self, card, money):
        self.cur.execute("update card set balance=balance+{} where number='{}'".format(money, card))
        self.conn.commit()


bank_instance = Bank()
main_menu(bank_instance)

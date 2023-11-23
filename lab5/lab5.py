import csv

import os
from pathlib import Path

path = Path(__file__).parents[0]
os.chdir(path)

class Smartphone():
    def __init__(self, price:int, brand:str, model:str, memory:int, battery_capacity:int, tf_slot:bool, display_frequency:int, back_cameras_amount:int, charging_port):
        self.price = price
        self.brand = brand
        self.model = model
        self.memory = memory
        self.battery_capacity = battery_capacity
        self.tf_slot = tf_slot
        self.display_frequency = display_frequency
        self.back_cameras_amount = back_cameras_amount
        self.charging_port = charging_port
    def get_data(self):
        data = [self.price, self.brand, self.model, self.memory, self.battery_capacity, self.tf_slot, self.display_frequency, self.back_cameras_amount, self.charging_port]
        return data
    def __del__(self):
        pass
        #print(f"Object {self.brand}, {self.model} destroyed")

class PhoneStore():
    def __init__(self, name, phones : list):
        self.name = name
        self.phones = phones
    
    def get_phones(self, elements = None):
        data = []
        if elements == None:
            elements = self.phones
        for phone in elements:
            data.append(phone.get_data())
        return data
    
    def sort_by_price(self, sort_type = "decrease", elements = "all"):
        if elements == "all":
            if sort_type == "increase":
                self.phones = sorted(self.phones, key = lambda phone: phone.price)
            elif sort_type == "decrease":
                self.phones = sorted(self.phones, key = lambda phone: phone.price, reverse = True)
            else: print("TypeError")
        else:
            if sort_type == "increase":
                elements = sorted(elements, key = lambda phone: phone.price)
            elif sort_type == "decrease":
                elements = sorted(elements, key = lambda phone: phone.price, reverse = True)
            else: print("TypeError")
            return elements
    
    def get_top_phones(self,max_price,second_atribute = None, data = "all"):
        all_phones = self.phones
        phones = []
        for phone in all_phones:
            if phone.get_data()[0] <= max_price:
                phones.append(phone)
        if second_atribute == "battery":
            phones = sorted(phones, key = lambda phone: phone.battery_capacity, reverse = True)
        elif second_atribute == "memory":
            phones = sorted(phones, key = lambda phone: phone.memory, reverse = True)
        elif second_atribute == "tf_slot":
            phones = sorted(phones, key = lambda phone: phone.tf_slot, reverse = True)
        elif second_atribute == "display_frequency":
            phones = sorted(phones, key = lambda phone: phone.display_frequency, reverse = True)
        elif second_atribute == "camera":
            phones = sorted(phones, key = lambda phone: phone.back_cameras_amount, reverse = True)
        else:
            phones = self.sort_by_price("increase", phones)
        if len(phones) > 5:
            _return_data = self.get_phones(phones)[:5]
        else:
            _return_data = self.get_phones(phones)
        if data != "all":
            return_data = []
            for el in _return_data:
                return_data.append(el[1:3])
            return return_data
        return _return_data
                
    
    def __del__(self):
        print(f"Store {self.name} destroyed")

def main():
    phones = []
    with open("phones.csv", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            price, brand, model, memory, battery_capacity, tf_slot, display_frequency, back_cameras_amount, charging_port = row
            price = int(price)
            memory = int(memory)
            battery_capacity = int(battery_capacity)
            display_frequency = int(display_frequency)
            back_cameras_amount = int(back_cameras_amount)
            phones.append(Smartphone(price, brand, model, memory, battery_capacity, tf_slot, display_frequency, back_cameras_amount, charging_port))
    store = PhoneStore("STORRE", phones)
    store.sort_by_price()
    top = store.get_top_phones(900, "memory",1)
    print(top)

if __name__ == "__main__":
    main()
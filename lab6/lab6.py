"""Module providing a function reading cvs files."""
import csv

class Smartphone():
    """Class representing a smartphone"""
    def __init__(self,data:dict):
        self.price = data["price"]
        self.brand = data["brand"]
        self.model = data["model"]
        self.memory = data["memory"]
        self.battery_capacity = data["battery_capacity"]
        self.tf_slot = data["tf_slot"]
        print(self.tf_slot)
        self.display_frequency = data["display_frequency"]
        self.back_cameras = data["back_cameras"]
        self.charging_port = data["charging_port"]
        self.data = data
    def get_data(self):
        """Method to get data"""
        data = list(self.data.values())
        return data
    def __del__(self):
        pass
        #print(f"Object {self.brand}, {self.model} destroyed")

class PhoneStore():
    """Class representing a store"""
    def __init__(self, name, phones : list):
        self.name = name
        self.phones = phones
        self.__sorted = False
    def get_phones(self, elements = None):
        """Method to get phones data"""
        data = []
        if elements is None:
            elements = self.phones
        for phone in elements:
            data.append(phone.get_data())
        return data
    def sort_by_price(self, sort_type = "decrease", sorted_elements = "all"):
        """Method to sort elements by price"""
        if sorted_elements == "all":
            self.__sorted = True
            elements = self.phones
        else:
            elements = sorted_elements
        if sort_type == "increase":
            elements = sorted(elements, key = lambda phone: phone.price)
        elif sort_type == "decrease":
            elements = sorted(elements, key = lambda phone: phone.price, reverse = True)
        else: raise AttributeError
        if sorted_elements == "all":
            self.phones = elements
            return None
        return elements
    def get_top_phones(self,max_price,second_attribute:str=None,all_data=False,top_amount=5)-> list:
        """Method to get best phones by price and second atribute"""
        all_phones = self.phones
        phones = []
        for phone in all_phones:
            if phone.get_data()[0] <= max_price:
                phones.append(phone)
        if not self.__sorted:
            phones = self.sort_by_price("increase", phones)
        if not second_attribute is None:
            phones = sorted(phones, key = lambda x: x.data[second_attribute], reverse = True)
        if len(phones) > top_amount:
            return_data = self.get_phones(phones)[:top_amount]
        else:
            return_data = self.get_phones(phones)
        if not all_data:
            _return_data = []
            for el in return_data:
                _return_data.append(el[1:3])
            return _return_data
        return return_data
    def __del__(self):
        print(f"Store {self.name} destroyed")

def main():
    """Main program"""
    phones = []
    import os #pylint: disable= C0415
    from pathlib import Path #pylint: disable= C0415
    path = Path(__file__).parents[0]
    os.chdir(path)
    with open("phones.csv", encoding="utf-8") as file:
        reader = csv.reader(file)
        keys = next(reader)
        int_keys = ("price", "memory", "battery_capacity", "display_frequency", "back_cameras")
        str_keys = ("brand", "model", "charging_port")
        bool_keys = ("tf_slot", )
        for args in reader:
            phone_data = {}
            for i, key in enumerate(keys):
                if key in int_keys:
                    phone_data[key] = int(args[i])
                elif key in str_keys:
                    phone_data[key] = args[i]
                elif key in bool_keys:
                    phone_data[key] = True if args[i] == "1" else False
                else:
                    raise KeyError
            phones.append(Smartphone(phone_data))
    store = PhoneStore("STORRE", phones)
    store.sort_by_price()
    top = store.get_top_phones(900, "memory")
    print(top)

if __name__ == "__main__":
    main()

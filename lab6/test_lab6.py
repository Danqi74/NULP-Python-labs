#pylint: disable = W0611, C0301
"""Import pytest module"""
import pytest
from lab6 import Smartphone, PhoneStore

phone_data_1 = {'price': 499, 'brand': 'OnePlus', 'model': 'Nord N20', 'memory': 128, 'battery_capacity': 4500, 'tf_slot': 1, 'display_frequency': 90, 'back_cameras': 3, 'charging_port': 'USB-C'}
phone_data_2 = {'price': 849, 'brand': 'Apple', 'model': 'iPhone 13 Pro Max', 'memory': 256, 'battery_capacity': 4352, 'tf_slot': 0, 'display_frequency': 60, 'back_cameras': 3, 'charging_port': 'Lightning'}
phone_data_3 = {'price': 249, 'brand': 'Xiaomi', 'model': 'Redmi Note 9', 'memory': 64, 'battery_capacity': 5020, 'tf_slot': 1, 'display_frequency': 60, 'back_cameras': 4, 'charging_port': 'USB-C'}

phone_1_list = [499,"OnePlus","Nord N20",128,4500,True,90,3,"USB-C"]
phone_2_list = [849,"Apple","iPhone 13 Pro Max",256,4352,False,60,3,"Lightning"]
phone_3_list = [249,"Xiaomi","Redmi Note 9",64,5020,True,60,4,"USB-C"]

phones = [Smartphone(phone_data_1), Smartphone(phone_data_2), Smartphone(phone_data_3)]
store = PhoneStore("Storre", phones)

def test_smartphone_get_data():
    """Func to test smartphone get_data method"""
    assert phones[0].get_data() == phone_1_list

class TestPhoneStore():
    """Class with tests of PhoneStore"""
    def test_get_phones(self):
        """Func to test store get_phones method"""
        assert store.get_phones()[0] == phone_1_list
    def test_sorting_by_price_decr(self):
        """Func to test store decrease sorting method"""
        store.sort_by_price()
        assert store.get_phones()[0][0] == 849
    def test_sorting_by_price_incr(self):
        """Func to test store increase sorting method"""
        store.sort_by_price("increase")
        assert store.get_phones()[0][0] == 249
    def test_get_top_phone(self):
        """Func to test store get_top_phones method without second attribute"""
        assert store.get_top_phones(500,None,True,1)[0] == phone_3_list
    def test_get_top_phone_by_memory(self):
        """Func to test store get_top_phones method by price and memory"""
        assert store.get_top_phones(1000,"memory",True,1)[0] == phone_2_list
    def test_get_top_phone_by_battery(self):
        """Func to test store get_top_phones method by price and battery"""
        assert store.get_top_phones(1000,"battery_capacity",True,1)[0] == phone_3_list
    def test_get_top_phone_by_tf(self):
        """Func to test store get_top_phones method by price and tf_slot"""
        assert store.get_top_phones(1000,"tf_slot",True,1)[0] == phone_3_list
    def test_get_top_phone_by_display(self):
        """Func to test store get_top_phones method by price and display frequecy"""
        assert store.get_top_phones(1000,"display_frequency",True,1)[0] == phone_1_list
    def test_get_top_phone_by_camera(self):
        """Func to test store get_top_phones method by price and cameras amount"""
        assert store.get_top_phones(1000,"back_cameras",True,1)[0] == phone_3_list

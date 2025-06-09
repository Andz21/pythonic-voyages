# Sort Dictionary by Keys
from typing import OrderedDict

my_dict = {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}

ordered_dict = OrderedDict(sorted(my_dict.items()))
print(ordered_dict)
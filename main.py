#shop_orig is the other file in the directory
from shop import (
    print_menu,
    print_originals,
    print_signatures,
    get_order,
    print_order,
)

print_menu()
print_originals()
print_signatures()
order_list = get_order()
print_order(order_list)

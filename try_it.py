# def shop_list():
#     the_list = []
#     while True:
#         action = input("Do you want to: Show/Add/Delete or Quit?: ")
#         if action.lower() == 'show':
#             for item in the_list:
#                 print(item)
#         elif action.lower() == 'add':
#             add_item = input("What item would you like?: ")
#             the_list.append(add_item)
#         elif action.lower() == 'delete':
#             del_item = input("what item would you like to remove?: ")
#             the_list.remove(del_item)
#         elif action.lower() == 'quit':
#             break
#     print(the_list)

# shop_list()

# from math import sqrt
# def square_or_square_root(arr):
#     return [sqrt(x) for x in arr if isinstance(sqrt(x), int) else x*x]
# new_arr= [4,3,9,7,2,1]
# square_or_square_root(new_arr)
from IPython.display import clear_output

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?
def grocery_list():
    complete_list = {}
    while True:
        response = input("Do you want to: Show/Add/Delete or Quit?")
        if response.lower().strip() == 'add':
            new_item = input("What item would you like?")
            item_qty = input("How many would you like?")
            grocery_list[new_item.lower().strip()]= item_qty.strip()
        elif response.lower().strip() == 'delete':
            to_delete =input("What would you like to remove?")
            del complete_list[to_delete.lower().strip()]
        elif response.lower().strip() == 'show':
            for item, qty in complete_list.items():
                print(f"{item_qty} {new_item}s")
        elif response.lower().strip() == 'quit':
            break
    for item, qty in complete_list.items():
        print(f"{item_qty} {new_item}s")

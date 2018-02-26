available_toppings = ['olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
successfully_finished = True
for requested_topping in requested_toppings: 
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        successfully_finished = False
        print("Sorry, we don't have" + requested_topping)
        
if successfully_finished:
    print("\nFinished making your pizza!")


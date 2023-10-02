# TODO
import cs50
cents_use=0
def get_cents():
    cents = cs50.get_float("Change Owed: ")
    while True:
        if cents < 0:
            cents = cs50.get_float("Change Owed: ")
        if cents > 0:
            break
    dollar=0
    if cents < 1.0:
        cents_use=round(cents, 2)*100
    if cents > 1.0:
        dollar=cents//1.0
        cents_use=round(cents-dollar, 2)*100
    return cents

# todo: Calculate the number of quarters
def calculate_quarters(cents_use):
    fix_num = 0.25
    cents_use = round(cents_use, 2)
    answer = round(cents_use // fix_num)
    return answer


# # Define the calculate_dimes function
def calculate_dimes(cents_use):
    fix_num = 0.10
    cents_use = round(cents_use, 2)
    answer = round(cents_use // fix_num)
    return answer

# # Define the calculate_nickels function
def calculate_nickels(cents_use):
    fix_num = 0.05
    cents_use = round(cents_use, 2)
    answer = round(cents_use // fix_num, 2)
    return answer

# # Define the calculate_pennies function
def calculate_pennies(cents_use):
    fix_num = 0.01
    cents_use = round(cents_use, 2)
    answer = round(cents_use / fix_num, 2)
    return answer


# # Define the main function
def main():
    # Ask how many cents the customer is owed
    cents_use = get_cents()
    # Calculate the number of quarters to give the customer
    quarters = calculate_quarters(cents_use)
    cents_use = cents_use - (quarters * 0.25)
    # Calculate the number of dimes to give the customer
    dimes = calculate_dimes(cents_use)
    cents_use = cents_use - (dimes * 0.10)
    # Calculate the number of nickels to give the customer
    nickels = calculate_nickels(cents_use)
    cents_use = cents_use - (nickels * 0.05)
    # Calculate the number of pennies to give the customer
    pennies = calculate_pennies(cents_use)
    cents_use = cents_use - (pennies * 0.01)

    # Sum coins

    coins = quarters + dimes + nickels + pennies

    # Print total number of coins to give the customer
    print(int(coins))


# Call the main function to start the program
main()

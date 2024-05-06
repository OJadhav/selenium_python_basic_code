# calculation_to_units = 24
# name_of_units = "hours"


# def days_to_units(num_of_days, conversion_units):
#     if conversion_units == "hours":
#         return f"{num_of_days} days are {num_of_days * 24} hours"
#     elif conversion_units == "minutes":
#         return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
#     else:
#         return "Unsupported Units"
#
#
# def validate_number():
#     try:
#         user_input_number = int(days_and_units_dict["days"])
#         if user_input_number > 0:
#             cal_value = days_to_units(user_input_number, days_and_units_dict["units"])
#             print(cal_value)
#         elif user_input_number == 0:
#             print("you entered a 0, so please entered positive value")
#         else:
#             print("you entered a negative number, so please entered positive value")
#     except ValueError:
#         print("Your input is not a valid number")
#



"""from helper import validate_number
user_input = ""
while user_input != "exit":
    user_input = input("Hey User, enter a number of days and conversion unit! Like days:hours(hours, minutes )\n")
    day_of_units = user_input.split(":")
    print(day_of_units)
    days_and_units_dict = {"days": day_of_units[0], "units": day_of_units[1]}
    print(days_and_units_dict)
    print(type(days_and_units_dict))
    #validate_number()
    validate_number(days_and_units_dict)"""

    ##iterate the value through for loop
    # list_of_days = user_input.split(", ")
    # print(list_of_days)
    # print(set(list_of_days))
    # print(type(list_of_days))
    # print(type(set(list_of_days)))
    # for num_of_days in set(user_input.split(", ")):
    #     validate_number()


import logging
logger = logging.getLogger("MAIN")
logger.error("Error happened in app")
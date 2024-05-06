def days_to_units(num_of_days, conversion_units):
    if conversion_units == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_units == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "Unsupported Units"


def validate_number(days_and_units_dict):
    try:
        user_input_number = int(days_and_units_dict["days"])
        if user_input_number > 0:
            cal_value = days_to_units(user_input_number, days_and_units_dict["units"])
            print(cal_value)
        elif user_input_number == 0:
            print("you entered a 0, so please entered positive value")
        else:
            print("you entered a negative number, so please entered positive value")
    except ValueError:
        print("Your input is not a valid number")


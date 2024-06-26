from datetime import datetime

user_input = input("Enter your goal with deadline separated by colon\n")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline,"%d.%m.%Y")
today_date = datetime.today()
till_time = deadline_date-today_date
hours_till = int(till_time.total_seconds() / 60 / 60)
print(f"Dear user! Time remaining for your goal: {goal} is {till_time.days} days")
print(f"Dear user! Time remaining for your goal: {goal} is {hours_till} hours")

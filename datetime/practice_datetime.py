import datetime
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - [%(name)s] - %(message)s",
                    filename="logfile.log"
                    )

logger = logging.getLogger("datetime_task")

now = datetime.date.today()
weekday = now.strftime("%A")


def is_leap(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


print(f"Now is {weekday}")
leap = is_leap(now.year)
print(f"The year {now.year} is{' not' if not leap else ''} leap.")

correct_date = None
while not correct_date:
    user_date = input("Type your date in YYYY-MM-DD format: ")
    try:
        correct_date = datetime.datetime.strptime(user_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid format of date. Please try again.\n")
        logger.error("Invalid input")


def delta_date(current_date, input_date):
    return input_date - current_date


delta = delta_date(now, correct_date)
if delta.days < 0:
    print(f"It has been {abs(delta.days)} days since {correct_date}, counting from today ({now}).")
elif delta.days > 0:
    print(f"There are {delta.days} days left until {correct_date}, counting from today ({now}).")
else:
    print(f"The entered date is today, compared to the current date ({now}).")

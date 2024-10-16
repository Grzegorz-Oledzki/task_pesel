from datetime import datetime


def check_pesel(pesel: str) -> tuple[bool, str]:
    year = pesel[0:2]
    month = pesel[2:4]
    day = pesel[4:6]
    sex = pesel[9]
    odd_numbers = ["1", "3", "5", "7", "9"]
    check_control_number: bool = is_control_number_valid(pesel)
    if check_control_number:
        first_month_number = month[0]
        if first_month_number in ["8", "9"]:
            full_year = f"18{year}"
        elif first_month_number in ["0", "1"]:
            full_year = f"19{year}"
        elif first_month_number in ["2", "3"]:
            full_year = f"20{year}"
        elif first_month_number in ["4", "5"]:
            full_year = f"21{year}"
        elif first_month_number in ["6", "7"]:
            full_year = f"22{year}"
        else:
            return False, "Wrong month format"

        full_month = (
            f"1{month[1]}" if first_month_number in odd_numbers else f"0{month[1]}"
        )
        if int(full_month) > 12:
            return False, f"Mounth of of range {full_month}"

        date_string = f"{day}-{full_month}-{full_year}"
        try:
            datetime.strptime(date_string, "%d-%m-%Y")
        except ValueError:
            return (
                False,
                f"Day is out of range for month. Day: {day}, month: {full_month}",
            )

        gender = "Male" if sex in odd_numbers else "Famale"
        return (
            True,
            f" Pesel is correct. The owner of this PESEL is {gender} born at {date_string}",
        )
    return False, "Control number is wrong"


def is_control_number_valid(pesel: str) -> bool:
    weights = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
    check = sum(w * int(n) for w, n in zip(weights, pesel[0:-1]))
    calculated_number = str((10 - check) % 10)
    control_number = pesel[-1]
    if control_number == calculated_number:
        return True


result = is_control_number_valid("98314092494")

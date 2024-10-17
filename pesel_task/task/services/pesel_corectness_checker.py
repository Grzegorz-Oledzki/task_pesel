from datetime import datetime


class PeselValidator:
    required_pesel_length: int = 11

    def __init__(self, pesel: str) -> None:
        self._pesel = pesel
        self._message = ""

    def is_valid(self) -> bool:
        if not self._pesel.isdigit() or len(self._pesel) != self.required_pesel_length:
            self._message = f"Wrong PESEL format, make sure if PESEL have {self.required_pesel_length} digits"
            return False

        self._control_number = self._pesel[-1]
        self._year = self._get_full_year()
        self._month = self._get_full_month()
        self._day = self._pesel[4:6]
        self._gender = "Male" if self._is_odd(int(self._pesel[9])) else "Famale"

        if not self._is_control_number_valid():
            self._message = "Control number is wrong"
            return False

        date_string = f"{self._day}-{self._month}-{self._year}"
        if not self._is_date_valid(date_string):
            self._message = (
                f"Day is out of range for month. Day: {self._day}, month: {self._month}"
            )
            return False

        self._message = f"Pesel is correct. The owner of this PESEL is {self._gender} born at {date_string}"
        return True

    def _is_control_number_valid(self) -> bool:
        weights = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
        sum_control = sum(
            weight * int(digit) for weight, digit in zip(weights, self._pesel[:-1])
        )
        expected_control_number: int = (10 - sum_control) % 10
        return int(self._control_number) == expected_control_number

    def _is_date_valid(self, date_string: str) -> bool:
        try:
            datetime.strptime(date_string, "%d-%m-%Y")
        except ValueError:
            return False

        return True

    def _get_full_year(self) -> str:
        first_month_digit = self._pesel[2]
        year_id = self._pesel[:2]

        match first_month_digit:
            case "8" | "9":
                century = "18"
            case "0" | "1":
                century = "19"
            case "2" | "3":
                century = "20"
            case "4" | "5":
                century = "21"
            case "6" | "7":
                century = "22"

        return f"{century}{year_id}"

    def _get_full_month(self) -> str:
        month_id = self._pesel[2:4]
        return (
            f"1{month_id[1]}" if self._is_odd(int(month_id[0])) else f"0{month_id[1]}"
        )

    def _is_odd(self, number: int) -> bool:
        return number % 2 == 1

    @property
    def message(self) -> str:
        return self._message

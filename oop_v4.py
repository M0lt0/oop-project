class Dates:
    def __init__(self, date):
        self.__date = date

    def getDate(self):
        return self.__date

    @staticmethod
    def dashDate(date):
        return date.replace("/", "-")


date = Dates("15-10-2022")
dateFromDb = "15/10/2022"
dateWithDash = Dates.dashDate(dateFromDb)
print(dateWithDash)


if (date.getDate() == dateWithDash):
    print("equal")
else:
    print("unequal")

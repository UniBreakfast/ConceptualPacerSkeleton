from datetime import date
today=date.today


# Класс Стремлений
class Endeavor:
    def __init__(self, full_name, short_name, details, endeavor_type, create_date, activities=None):
        self.full_name = full_name
        self.short_name = short_name
        self.details = details
        self.endeavor_type = endeavor_type
        self.create_date = create_date
        self.activities = activities

    def __str__(self):
        if self.activities == None:
            return "Cтремление: "+self.full_name+" ("+self.short_name+") - это "+self.endeavor_type+" (c "+str(self.create_date)\
                    +") Детали: "+self.details
        else:
            return "Cтремление: "+self.full_name+" ("+self.short_name+") - это "+self.endeavor_type+" (c "+str(self.create_date)\
                    +") Детали: "+self.details+" Для этого нужно: "+', '.join(self.activities)+"."

    def __repr__(self):
        return "self.full_name+" ("+self.short_name+")

#TestEndeavor = Endeavor("Ложиться спать до девяти вечера", "Сон21", "Если я буду вовремя ложиться спать, то буду гораздо здоровее и эффективнее.", "+привычка", today(), ["Планировать день", "Не есть после шести"])
#print(str(TestEndeavor))


# Незаконченный класс Действий
class Activity:
    def __init__(self, full_name, short_name, amount, diff, usef):
        self.full_name=full_name
        self.short_name=short_name
        self.amount=amount
        self.diff=diff
        self.usef=usef


class Quest:
    def __init__(self, full_name, short_name, amount, actual_diff, usef, start_date):
        pass
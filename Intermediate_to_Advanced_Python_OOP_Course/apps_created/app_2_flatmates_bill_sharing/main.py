
class Bill:
    '''
    This represents the Bill object
    '''

    def __init__(self, amount, period, period_name):
        self.amount = amount
        self.period = period
        self.period_name = period_name


class Flatmate:
    '''
    This class represents a flatmate
    '''

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pay(self, bill, other_flatmate):
        total_bill_amount = bill.amount 
        flatmate_days_in_house = self.days_in_house
        other_flatmate_days_in_house = other_flatmate.days_in_house
        bill_contribution_percentage = flatmate_days_in_house/(flatmate_days_in_house+other_flatmate_days_in_house)
        bill_to_pay = total_bill_amount*bill_contribution_percentage
        return bill_to_pay

class PdfReport:
    '''
    This class represents the PdfReport that needs to be generated
    '''

    def __init__(self, filename):
        self.filename = filename
        
    def generatePDF(self, flatmate1, flatmate2, bill):
        pass    


pratik = Flatmate(name='Pratik', days_in_house=25)
shraddha = Flatmate(name='shraddha', days_in_house=30)

nov_bill = Bill(500, 30, 'November 2025')

print(pratik.pay(nov_bill, shraddha))
print(shraddha.pay(nov_bill, pratik))

print(shraddha.pay(nov_bill, pratik)+pratik.pay(nov_bill, shraddha))
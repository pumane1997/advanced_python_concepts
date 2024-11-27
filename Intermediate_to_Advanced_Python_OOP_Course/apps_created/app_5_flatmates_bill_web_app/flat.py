
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
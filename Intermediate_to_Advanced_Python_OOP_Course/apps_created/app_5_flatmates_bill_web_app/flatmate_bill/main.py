from fpdf import FPDF
import flat
import reports

'''
Testing with some manual values

nov_bill = Bill(500, 30, 'November 2025')
pratik = Flatmate(name='Pratik', days_in_house=25)
shraddha = Flatmate(name='shraddha', days_in_house=30)
pratik_contribution = pratik.pay(nov_bill, shraddha)
shraddha_contribution = shraddha.pay(nov_bill, shraddha)
pdf = FPDF(orientation='P', unit='pt', format='A4')
PdfReport('Nov2025Bill').generatePDF(pdf, pratik, shraddha, nov_bill)
'''
# Take inputs for Bill Instance 
bill_amount = float(input('What is the total bill amount?: '))
bill_period_name = str(input('Which period is this bill for?: '))
bill_days = int(input(f'How many days does {bill_period_name} has?: '))

# Take inputs for flatmate 1
flatmate1_name = str(input('What is the name of flatmate 1?: '))
flatmate1_days_in_house = int(input(f'How many days did {flatmate1_name} stayed in house for this period?: '))

# Take inputs for flatmate 2
flatmate2_name = str(input('What is the name of flatmate 2?: '))
flatmate2_days_in_house = int(input(f'How many days did {flatmate2_name} stayed in house for this period?: '))

# Take inputs for PDF Report
bill_file_name = str(input('What should be the name of the bill report?: '))

bill = flat.Bill(bill_amount, bill_days, bill_period_name)
flatmate1 = flat.Flatmate(flatmate1_name, flatmate1_days_in_house)
flatmate2 = flat.Flatmate(flatmate2_name, flatmate2_days_in_house)
print(f'{flatmate1_name} pays {flatmate1.pay(bill, flatmate2)}')
print(f'{flatmate1_name} pays {flatmate2.pay(bill, flatmate1)}')
pdf = FPDF(orientation='P', unit='pt', format='A4')
reports.PdfReport(bill_file_name).generatePDF(pdf, flatmate1, flatmate2, bill)
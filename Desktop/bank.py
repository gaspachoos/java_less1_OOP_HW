import string
from datetime import datetime
import easygui
import math
import time
import sys

# Создали функию для проверки фио,есть ли в фио int - овое значение или знак. 
def string_checking(input_string):
    costName,costSurname,costLastName = input_string
    # Проверка на наличие цифры в строке.
    if any(char.isdigit() for char in costName) or any(char.isdigit() for char in costSurname) or any(char.isdigit() for char in costLastName): 
        easygui.msgbox("Вы ввели некоректные данные")  
        fields = ["Имя", "Фамилия", "Отчество"]
        values = easygui.multenterbox("Введите данные:", "Ваши данные", fields)
        return string_checking(values) 
    # Проверка на наличие знака в строке.
    if  has_punctuation(costName) == True or has_punctuation(costSurname) == True or has_punctuation(costLastName) == True:   
        easygui.msgbox("Вы ввели некоректные данные")  
        fio = ["Имя", "Фамилия", "Отчество"]
        fioValues = easygui.multenterbox("Введите данные:", "Ваши данные", fio)
        return string_checking(fioValues) 
    # Проверка на пустое значение(оставил ли пользователь какую нибудь поле заполнения пустой).
    if  costName == "" or costSurname == "" or costLastName == "":
        easygui.msgbox("Необходимо заполнить все поля")
        fio = ["Имя", "Фамилия", "Отчество"]
        fioValues = easygui.multenterbox("Введите данные:", "Ваши данные", fio)
        return string_checking(fioValues) 
# Создали функцию для проверки введенных данных, есть ли там знаковое значение.        
def has_punctuation(input_string):    
    if any(char in string.punctuation for char in input_string):             
        return True
    else:
        return False
# Создали функцию для проверки даты рождения.    
def birth_date_checking(input_digit):
   day,month,year = input_digit
   # Проверка каждого введенного поля для проверки,есть ли там символьное значение.
   if   any(char.isalpha() for char in day) or any(char.isalpha() for char in month) or any(char.isalpha() for char in year):
        easygui.msgbox("Вы ввели некоректные данные")
        date = ["День","Месяц","Год"]
        dateValues = easygui.multenterbox("Введите данные:", "Ваш день рождения", date)
        return birth_date_checking(dateValues)
   # Проверка на наличие знаков.
   if   has_punctuation(day) == True or has_punctuation(month) == True or has_punctuation(year) == True:   
        easygui.msgbox("Вы ввели некоректные данные")  
        date = ["День","Месяц","Год"]
        dateValues = easygui.multenterbox("Введите данные:", "Ваш день рождения", date)
        return birth_date_checking(dateValues)
   # Проверка на наличие пустых полей.
   if   day == "" or month == "" or year == "":
        easygui.msgbox("Необходимо заполнить все поля")
        date = ["День","Месяц","Год"]
        dateValues = easygui.multenterbox("Введите данные:", "Ваш день рождения", date)
        return birth_date_checking(dateValues)
   # Проверка введенных цифер на валидность.
   if   not 1 <= int(day) <= 31 or not 1 <= int(month) <= 12 or not 1900 < int(year) < 2024:
        easygui.msgbox("Вы ввели некоректные данные")  
        date = ["День","Месяц","Год"]
        dateValues = easygui.multenterbox("Введите данные:", "Ваш день рождения", date)
        return birth_date_checking(dateValues)
   # Проверка введенных данных на валидность с календарными данными
   # (к примеру пользователь не может выбрать 31 день с месяцем где дней всего 30). 
   if   check_date(int(day),int(month)) == False:
        easygui.msgbox("Вы ввели некоректные данные")  
        date = ["День","Месяц","Год"]
        dateValues = easygui.multenterbox("Введите данные:", "Ваш день рождения", date)
        return birth_date_checking(dateValues)  

# Проверка введенных данных на валидность с календарными данными.
def check_date(day, month):
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if day > days_in_month[month]:    
        return False
    else:
        return True

# Создали функцию для проверки данных ежемесячной платы,ежемесячных затрат на кредиты,желаемой суммы.        
def money_valid_checking(input_digit):
   salary_prompt,monthly_debt_prompt,desired_loan_prompt  = input_digit
   # Проверка каждого введенного поля для проверки,есть ли там символьное значение.
   if   any(char.isalpha() for char in salary_prompt) or any(char.isalpha() for char in monthly_debt_prompt) or any(char.isalpha() for char in desired_loan_prompt):
        easygui.msgbox("Вы ввели некоректные данные")
        info_about_money = ["Введите ваше ежемесячное заработное плату","Введите сумму ваших текущих месячных кредитных обязательств","Введите желаюмую сумму кредита"]
        infoMoney = easygui.multenterbox("Введите данные","Кредиты",info_about_money)
        return money_valid_checking(infoMoney)    
   # Проверка на наличие знаков.
   if   has_punctuation(salary_prompt) == True or has_punctuation(monthly_debt_prompt) == True or has_punctuation(desired_loan_prompt) == True:   
        easygui.msgbox("Вы ввели некоректные данные")  
        info_about_money = ["Введите ваше ежемесячное заработное плату","Введите сумму ваших текущих месячных кредитных обязательств","Введите желаюмую сумму кредита"]
        infoMoney = easygui.multenterbox("Введите данные","Кредиты",info_about_money)
        return money_valid_checking(infoMoney) 
   # Проверка на наличие пустых полей.
   if   salary_prompt == "" or monthly_debt_prompt == "" or desired_loan_prompt == "":
        easygui.msgbox("Необходимо заполнить все поля")
        info_about_money = ["Введите ваше ежемесячное заработное плату","Введите сумму ваших текущих месячных кредитных обязательств","Введите желаюмую сумму кредита"]
        infoMoney = easygui.multenterbox("Введите данные","Кредиты",info_about_money)
        return money_valid_checking(infoMoney) 

# Функция для вычисления ежемесячного платежа по кредиту   
def calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    monthly_payment = round((monthly_interest_rate * float(loan_amount)) / (1 - (1 + monthly_interest_rate) ** (-float(loan_term))))
    return int(monthly_payment)




def  check_credit_eligibility(salary_prompt,monthly_debt_prompt,monthly_payment):
   half_salary = (int(salary_prompt) * 0.5) + float(monthly_payment)
   if int(monthly_debt_prompt) > half_salary:
      return False
   else:
      return True 
  
def calculate_age(day_now,month_now,year_now,customer_day,customer_month,customer_year,BankMaxAge,date_credit,monthly_payment):
    result = year_now - int(customer_year)
    if int(customer_month) > month_now:
        result = result - 1
    elif customer_month == month_now:
        if int(customer_day) > day_now:
            result = result - 1
    result = result * 12 + month_now
    result1 = BankMaxAge * 12
    result2 = result1 - result
    monthly_payment = round(monthly_payment,1)
    
    
    if int(date_credit) > result2:
       return False
    elif int(date_credit) <= result2:
       easygui.msgbox("Нажмите 'OK' и пожалуйста подождите для обработки запроса.")
       time.sleep(10)
       easygui.msgbox(f"Ваш кредит одобрен! срок погашения кредита {date_credit} месяцев, ежемесячная плата {monthly_payment}.")
       sys.exit()

def  check_credit_eligibility_alternative(salary_prompt,monthly_debt_prompt,monthly_payment):
   half_salary = (int(salary_prompt) * 0.6) + int(monthly_payment)
   if int(monthly_debt_prompt) > half_salary:
       return False
   else:
      return True 
   
def calculate_age_alternative(day_now,month_now,year_now,customer_day,customer_month,customer_year,BankMaxAge,date_credit,monthly_payment):
    result = year_now - int(customer_year)
    if int(customer_month) > month_now:
        result = result - 1
    elif customer_month == month_now:
        if int(customer_day) > day_now:
            result = result - 1
    result = result * 12 + month_now
    result1 = (BankMaxAge+10) * 12
    result2 = result1 - result
    monthly_payment = round(monthly_payment,1)
    
    
    if int(date_credit) > result2:
       easygui.msgbox("Нажмите 'OK' и пожалуйста подождите для обработки запроса.")
       time.sleep(10)
       easygui.msgbox("К сожалению вам отказано в кредите.")
       sys.exit()
    elif int(date_credit) <= result2:
       easygui.msgbox("Нажмите 'OK' и пожалуйста подождите для обработки запроса.")
       time.sleep(10)
       easygui.msgbox(f"Ваш кредит одобрен! срок погашения кредита {date_credit} месяцев, ежемесячная плата {monthly_payment}.")   
       sys.exit()




# Получаем реальную дату
now = datetime.now()  # Получаем текущую дату и время
day_now = now.day  # Извлекаем день
month_now = now.month  # Извлекаем месяц
year_now = now.year  # Извлекаем год

# Устанавливаем начальные требования банка (диапазон возраста и затраты от зарплаты пользователя, и процент банка)
bank_credit_max_age = 50
bank_credit_percent = 17.5
bank_checking_customer_costs = 50     

# Получаем ФИО клиента через easygui
fio = ["Имя", "Фамилия", "Отчество"]
fioValues = easygui.multenterbox("Введите данные:", "Ваши данные", fio)
string_checking(fioValues)  # Проверяем введенные данные на корректность

# Получаем дату рождения клиента 
date = ["День", "Месяц", "Год"]
dateValues = easygui.multenterbox("Введите данные:", "Ваш день рождения", date)
customer_day, customer_month, customer_year = dateValues
birth_date_checking(dateValues)  # Проверяем введенные данные на корректность

# Получаем информацию о финансах клиента
info_about_money = ["Введите ваше ежемесячное заработное плату", 
                    "Введите сумму ваших текущих месячных кредитных обязательств", 
                    "Введите желаемую сумму кредита"]
info_money = easygui.multenterbox("Введите данные", "Кредиты", info_about_money)
salary_prompt, monthly_debt_prompt, desired_loan_prompt = info_money
money_valid_checking(info_money)  # Проверяем введенные данные на корректность

# Получаем выбор клиента о месяце погашения кредита
choices_credit_date = ["6", "12", "18", "24", "30"]
date_credit = easygui.choicebox("Выберите месяц погашения", "Выбор", choices=choices_credit_date)
monthly_payment = calculate_monthly_payment(desired_loan_prompt, bank_credit_percent, date_credit)

# Проверяем доступность кредита по финансам клиента
if check_credit_eligibility(salary_prompt, monthly_debt_prompt, monthly_payment):
    # Проверяем возраст клиента
    if calculate_age(day_now, month_now, year_now, customer_day, customer_month, customer_year, bank_credit_max_age, date_credit, monthly_payment):
       easygui.msgbox("Спасибо, что воспользовались услугами нашего банка!")
    else:
        # Альтернативная проверка с большим диапазоном возраста 
        calculate_age_alternative(day_now, month_now, year_now, customer_day, customer_month, customer_year, bank_credit_max_age, date_credit, monthly_payment)
else: 
    # Альтернативно проверяем доступность кредита по финансам клиента
    check_credit_eligibility_alternative(salary_prompt, monthly_debt_prompt, monthly_payment)
    # Альтернативная проверка с большим диапазоном возраста 
    calculate_age_alternative(day_now, month_now, year_now, customer_day, customer_month, customer_year, bank_credit_max_age, date_credit, monthly_payment)

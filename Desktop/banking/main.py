from functions import *  # Импортируем все функции из модуля functions

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

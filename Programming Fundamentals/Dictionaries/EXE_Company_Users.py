data = input()

company_book = {}

while not data == "End":
    company_name, employee_id = data.split(" -> ")

    if company_name not in company_book:
        company_book[company_name] = []
    if employee_id not in company_book[company_name]:
        company_book[company_name].append(employee_id)

    data = input()

company_name_order = sorted(company_book.items(), key=lambda x: (x[0]))

for key, value in company_name_order:
    print(key)
    for employee in value:
        print(f'-- {employee}')

# 50 / 100 with set()

# data = input()
#
# company_book = {}
#
# while not data == "End":
#     company_name, employee_id = data.split(" -> ")
#
#     if company_name not in company_book:
#         company_book[company_name] = set()
#     company_book[company_name].add(employee_id)
#
#     data = input()
#
# company_name_order = sorted(company_book.items(), key=lambda x: (x[0]))
#
#
# for key, value in company_name_order:
#     print(key)
#     for employee in sorted(value):  #sorted() makes the program go to 50/100, can't be done with set() 'cause it needs to keep to order of employees
#         print(f'-- {employee}')

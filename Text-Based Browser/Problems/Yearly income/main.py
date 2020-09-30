# write your code here
with open('salary.txt') as month_salary:
    with open('salary_year.txt', 'w') as year_salary:
        month_salary_list = month_salary.readlines()
        year_salary_list = [str(int(x) * 12) for x in month_salary_list]
        for slr in year_salary_list:
            year_salary.write(slr + '\n')

def salary(income,target,rests=0.06):
    result = 0
    year = 0

    while result  < target:

        result = (income * 12 +result)  *(1+rests)
        year+=1
    rundu = (result -target)
    intrests = result - income*12*year
    return income,year,rests,target,rundu,intrests
tar = 100
salary_my = 1.0
print(salary(salary_my,tar,rests=0.035))
print(salary(salary_my,tar,rests=0.04))
print(salary(salary_my,tar,rests=0.045))
print(salary(salary_my,tar,rests=0.047))
print(salary(salary_my,tar,rests=0.05))
print(salary(salary_my,tar,rests=0.06))
print(salary(salary_my,tar,rests=0.08))
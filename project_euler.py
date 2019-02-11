def problem_19(): # Wall time: 14.4 ms
    from dateutil.relativedelta import relativedelta
    from datetime import datetime
    def get_next_months(start_date):
        date = start_date
        while True:
            yield date
            date += relativedelta(months = 1)
    strt_time = datetime.strptime('1 Jan 1901', '%d %b %Y')
    end_time = datetime.strptime('31 Dec 2000', '%d %b %Y')
    sundays = 0
    for x in get_next_months(strt_time):
        if x > end_time:
            print(sundays)
            return sundays
        if x.weekday() == 6:
            sundays+=1

def problema_20():
    import math
    return sum([int(x) for x in list(str(math.factorial(100)))])

def problem_21(): # Aprox 40 seconds
    import numpy as np
    def residuos(x):
            c = x//2+1
            while c>0:
                yield x%c
                c-=1
    def divisors_sum(num):
        x = np.array(list(residuos(num)))
        handle = sorted(range(1,len(x)), reverse=True)
        divisores = [y+1 for x,y in zip(x,handle) if x==0]
        return sum(divisores)+1
    numeros_amicos = []
    for num in range(1,10001):
        p1 = divisors_sum(num)
        p2 = divisors_sum(p1)
        if num == p2:
            numeros_amicos.append([num, p1])
    return sum([x+y for x,y in numeros_amicos if x != y])/2

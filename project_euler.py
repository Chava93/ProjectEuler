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

def problem_22():
    import csv
    import requests
    url = 'https://projecteuler.net/project/resources/p022_names.txt'
    with requests.Session() as sess:
        page = sess.get(url)
        names = page.content.decode('utf-8')
        names = [x[0] for x in list(csv.reader(names)) if len(x[0])>0]
    namesToNumber = list(map(lambda z: sum([ord(x)-64 for x in list(z)]), sorted(names) ))
    total = sum([x*y for x,y in zip(namesToNumber, range(1, len(namesToNumber)+1 ))])
    return total
    
def problem42():
    import pandas as pd
    triangular = lambda x: 1/2*x*(x+1) # Def Triangular Numbers generator
    triangular = [int(triangular(x)) for x in range(21)] # Create list of triangular numbers
    url = "https://projecteuler.net/project/resources/p042_words.txt"
    d = (
        pd.read_csv(url, header=None, dtype=str)
        .T
        .rename(columns = {0:'words'})
        .words
        .map(lambda x: sum([ord(x)-64 for x in list(x)]))
        .map(lambda x: x in triangular)
        .sum()
    )
    return d

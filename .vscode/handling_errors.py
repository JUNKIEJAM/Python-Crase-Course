try:
    age=int(input("Age: "))
    income=2
    risk=income/age
    print(age)

except ValueError:  #ValueError only gives error for integer
    print('Invalid error')
    
except ZeroDivisionError:
    print('Age cannot be 0')
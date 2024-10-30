from datetime import datetime, timedelta

now = datetime.now()
print(f'Now has a type of {type(now)}')
current_time = (now + timedelta(hours=-12)).strftime("%H:%M")
# test_time = now + timedelta(hours=6)
# current_time = ''
print(f'Current time is: {current_time}')
print(f'current_time has a type of: {type(current_time)}')

if current_time >= '23:00' or current_time < '04:00': 
    print("What are you doing up so late?")
elif current_time < '10:00':
    print('Good morning!')
elif current_time < '17:00':
    print('Good day!')
elif current_time >= '17:00':
    print('Good evening!')







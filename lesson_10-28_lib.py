# import math
# import statistics

# gar_bill = [1.33, 4, 14.95, 2, 10, 29.98, 3.46]
# gar_bill.sort()

# print(f'Total garbage bill is: ${math.fsum(gar_bill)}')
# print(f'Average line item amount: ${statistics.mean(gar_bill)}')
# print(f'Median item amount: ${statistics.median(gar_bill)}')
# print(f"Bill sorted by amount: {gar_bill}")


# import random

# gar_bill = [1.33, 4, 14.95, 2, 10, 29.98, 3.46]

# print(random.choices(gar_bill, k=2))

import datetime

now = datetime.datetime.now()
print(now)
print(now.strftime("%A"))


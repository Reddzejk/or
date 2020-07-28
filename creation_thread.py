import timeit
import matplotlib.pyplot as plt
import seaborn as sns

import_thread = 'from threading import Thread'

create_thread = 'Thread().start()'

values = [None] * 10
result = [None] * 10

j = 0
for i in range(10, 110, 10):
    iterations = 1000 * i
    t = timeit.timeit(setup=import_thread, stmt=create_thread, number=iterations)
    unit_time = t * 100000 / iterations
    print(f'iterations: {iterations} time: {t} unit_time:{unit_time}')
    result[j] = unit_time
    values[j] = iterations
    j = j + 1

sns.set_context('talk')
sns.set_style('darkgrid')
plt.bar(values, result, width=9000)
plt.show()

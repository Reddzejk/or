import threading
import timeit
import matplotlib.pyplot as plt
import seaborn as sns
import time


# Wątek pracjący w pętli, aby móc zasymulować pracę ciąŋłą
class MyThread(threading.Thread):
    def run(self):
        start = int(time.time())
        while int(time.time()) - start < 60:
            pass


# przygotowanie procedur dla timeit
import_thread = 'from __main__ import MyThread'
create_thread = 'MyThread().start()'

values = [None] * 10
result = [None] * 10

j = 0
thread_sum = 0
for iterations in range(1, 11, 1):
    thread_sum += 10
    # Wykonanie operacji
    t = timeit.timeit(setup=import_thread, stmt=create_thread, number=10)
    # Wynii dla kolejnej próby
    unit_time = t / 10
    print(f'threads: {thread_sum} iterations: {iterations} time: {t} unit_time:{unit_time}')
    result[j] = unit_time
    values[j] = thread_sum
    j = j + 1

while threading.activeCount() > 1:
    pass

# Wykres słupkowy przedstawiajacy wyniki
sns.set_context('talk')
sns.set_style('darkgrid')

plt.bar(values, result)
plt.show()

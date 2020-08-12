import threading
import timeit
import matplotlib.pyplot as plt
import seaborn as sns
import time


# Wątek pracjący w pętli, aby móc zasymulować pracę ciągłą
class MyThread(threading.Thread):
    def run(self):
        start = int(time.time())
        # zakoczenie pracy wątku po jednej minucie
        while int(time.time()) - start < 90:
            pass


# przygotowanie procedur dla timeit
import_thread = 'from __main__ import MyThread'
create_thread = 'MyThread().start()'

values = [None] * 20
result = [None] * 20

j = 0
thread_sum = 0
for iterations in range(1, 21, 1):
    thread_sum += 10
    # Wykonanie operacji (utworzenie nowych 10 wątków)
    t = timeit.timeit(setup=import_thread, stmt=create_thread, number=10)
    # Wynii dla kolejnej próby stworzenia 10 wątków
    unit_time = t / 10
    print(f'threads: {thread_sum} iterations: {iterations} time: {t} unit_time:{unit_time}')
    # Czasy kolejnych iteracji tworzenia wątków
    result[j] = unit_time
    # Ilość wątków dla dla kolejnych iteracji
    values[j] = thread_sum
    j = j + 1

# Oczekiwanie na zakończenie działania wątków
while threading.activeCount() > 1:
    pass

# Wykres słupkowy przedstawiajacy wyniki
sns.set_context('talk')
sns.set_style('darkgrid')

plt.bar(values, result)
plt.show()

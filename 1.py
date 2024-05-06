from random import random
from timeit import timeit
from insert_sort import insertion_sort
from merge_sort import merge_sort


def measure_sort():
    tim_time = timeit(lambda: sorted([random() for _ in range(1000)]), number=1000)
    print('Час на сортування методом Timsort: ', tim_time)

    merge_time = timeit(lambda: merge_sort([random() for _ in range(1000)]), number=1000)
    print('Час на сортування методом злиття: ', merge_time)

    insert_time = timeit(lambda: insertion_sort([random() for _ in range(1000)]), number=1000)
    print('Час на сортування методом вставки: ', insert_time)

    print(f'''
        Таким чином найшвидшим алгоритмом сортування виявися Timsort
        Метод сортування злиттям є повільнішим за Timsort в {round(merge_time/tim_time, 0)} разів
        В свою чергу метод вставки є повільнішим за Timsort в {round(insert_time/tim_time, 0)} разів
        
        Також по результатах помітно різницю між часовою складністю O(n) сортування злиттям (логарифмічна) 
        та сортування вставкою (квадратична)
        
        Отже вбудований алгоритм Timsort є найшвидшим, хоча й будується на основі двох інших. Це показує
        що інколи доцільно використовувати не просто найшвидший алгоритм, а оптимальну комбінацію існуючих   
    ''')

if __name__ == "__main__":
    measure_sort()

почему индексы это важно:
ну те кто работают с базами данных знают что индексы ускоряют поиск значений. Тоесть без индексов - чтобы получить строчку где какое-то значение равно чему-то - нужно сделать поиск / линейная операция O(n) - где n - число строчек. В худшем случае значение которое вы ищете будет самой последней строчкой и вам придется пройти полностью все строчки (займет n lookups)

Индекс хеширует ваши значения и каждому значению сопостовляет индекс строчки в которой лежит это значение. 

Объяснить про хеш. что это как. 

Это получается такая структура как hash-table. У нее в среднем lookup  занимает `O(1)` там если нет коллизий. Ну также стоит сказать что в других хранилищах данных, не в pandas (там в реаляционнках DB) обычно используют не hashtable а более продвинутые структуры данных в частности B+ trees. 
В частности mysql позволяет юзать как хеш таблицы, так и B-trees. И даже позволяет самому выбирать какой способ использовать.

В чем плюсы  B-trees. Они позволяют не только найти индекс какого-то значения за O(1). А также возможность делать такие штуки как select ranges 

The difference between using a b-tree and a hash table is that the former allows you to use column comparisons in expressions that use the =, >, >=, <, <=, or BETWEEN operators, while the latter is used only for equality comparisons that use the = or <=> operators.


Index: the generic “ordered set” object, an ndarray of object dtype assuming nothing about its contents. The labels must be hashable (and likely immutable) and unique. Populates a dict of label to location in Cython to do O(1) lookups.

Индексы создают оптимизированные ярлыки для конкретных значений, используя пря-мой поиск.
Чтобы начать изучение значений индексов, создадим объект DataFrame из 10 000 случайных чисел:


тех кто хочет глубоко понять как индексы работают изнутри в реляционных БД / есть такой классический уже сайт на котором прям суть - рекомендую:
![screenshot 2019-03-04 at 11 50 08](https://user-images.githubusercontent.com/5549677/53721230-baf09180-3e73-11e9-84e5-ec58c1305b53.png)

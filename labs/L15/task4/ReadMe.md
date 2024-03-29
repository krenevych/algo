# Двобічно зв'язний список з розширеним переліком операцій

Реалізуйте структуру даних двобічно зв'язний список з поточним елементом
та реалізуйте додаткові операції для роботи зі списком.
Реалізацію здійсніть у вигляді сукупності функцій описаних нижче.

```python
def init()
```

Викликається один раз на початку виконання програми.

```python
def empty()
```

Перевіряє чи список порожній.

```python
def set_first()
```

Робить перший елемент списку поточним.

```python
def set_last()
```

Робить останній елемент списку поточним.

```python
def next()
```

Перейти до наступного елемента – робить поточним елементом списку,
елемент, що йде за поточним.
Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.

```python
def prev()
```

Перейти до попереднього елемента – робить поточним елементом елемент списку,
що йде перед поточним. Породжує виключення StopIteration,
якщо поточний елемент є першим у списку.

```python
def current()
```

Повертає навантаження поточного елементу.

```python
def insert_after(item)
```

Вставляє новий елемент у список після поточного.

```python
def insert_before(item)
```

Вставляє новий елемент у список перед поточним.

```python
def delete()
```

Видаляє поточний елемент. Поточним при цьому стає наступний елемент,
що йшов у списку після поточного.
Якщо елемент, що видаляється був у списку останнім, то поточним стає
передостанній елемент цього списку.

```python
def damp()
```

Повертає масив у якому записані всі елементи поточного списку.

```python
def len()
```

Повертає кількість елементів у списку

```python
def swap_prev()
```

Міняє місцями поточний елемент списку з попереднім.
Гарантується, що виклик функції здійснюється лише, якщо поточний
елемент не перший у списку. Поточний елемент лишається не змінним

```python
def swap_next()
```

Міняє місцями поточний елемент списку з наступним. Гарантується, що виклик функції здійснюється лише, якщо поточний
елемент не останній у списку. Поточний елемент лишається не змінним.

Реалізуйте згадані вище функції, інтерфейси яких містяться у файлі *user.py*.
Для перевірки правильності алгоритму запустіть файл *main.py*.
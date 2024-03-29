# Двобічно зв'язний список

Реалізуйте структуру даних двобічно зв'язний список з поточним елементом.
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
Гарантується, що функція не буде викликана, якщо список порожній.

```python
def insert_after(item):
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
Якщо елемент, що видаляється був у списку останнім, 
то поточним стає передостанній елемент цього списку.
Гарантується, що функція не буде викликана, якщо список порожній.

Реалізуйте згадані вище функції, інтерфейси яких містяться у файлі *user.py*.
Для перевірки правильності алгоритму запустіть файл *main.py*.
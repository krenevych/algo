# Зв'язний список з поточним елементом

Реалізуйте структуру даних зв'язний список з поточним елементом.
Реалізацію здійсніть у вигляді сукупності функцій описаних нижче.

```python
def init()
```

викликається один раз на початку виконання програми.

```python
def empty()
```

перевіряє чи список порожній.

```python
def reset()
```

робить перший елемент списку, поточним.

```python
def next()
```

перейти до наступного елемента – робить поточним елементом списку, елемент, що йде за поточним.
Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.

```python
def current()
```

повертає навантаження поточного елементу.
Гарантується, що функція не буде викликана, якщо список порожній.

```python
def insert_after(item)
```

вставляє новий елемент у список після поточного.

Реалізуйте згадані вище функції, інтерфейси яких містяться у файлі *user.py*.
Для перевірки правильності алгоритму запустіть файл *main.py*.
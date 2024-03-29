# Хеш таблиця 


Реалізуйте інтерфейс асоціативного масиву, 
ключами якого є цілі числа, а значеннями – рядки. 
**Реалізацію здійсніть як хеш-таблицю з розв’язанням 
колізій методом ланцюжків** у вигляді сукупності функцій 
описаних нижче функцій.

Функція 

```python
def init()
```

Викликається один раз на початку виконання програми.

Функція

```python
def set(key: int, value: str) -> None
```
встановлює значення `value` для ключа `key`. 
Якщо такий ключ відсутній у структурі – додає пару,
інакше змінює значення для цього ключа.

Функція
```python
def get(key: int) -> str
```

за ключем `key` повертає значення зі структури 
(або `None`, якщо ключ відсутній у структурі). 

Нарешті, функція


```python
def delete(key: int) -> None
```

видаляє пару ключ-значення за заданим ключем,
якщо такий ключ міститься у таблиці.

Реалізуйте згадані вище функції, інтерфейси яких містяться у файлі  *user.py*. 
Для перевірки правильності алгоритму запустіть файл *main.py*.

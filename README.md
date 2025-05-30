# Payments System - Django Interview Solution

## Описание
Простой API-сервис на Django для обработки webhook-ов от банка и учета баланса организаций по ИНН.

## Автор проекта:
*  [Никита Малумашвили](https://github.com/TLS228)

## Технологии
- Python 3.9
- Django 4.2.17
- Django REST Framework
- MySQL

## Запуск проекта
1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:TLS228/Payments-System.git
```

```
cd Payments-System
```

2. Создать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```

```
python -m pip install --upgrade pip
```

3. Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

## Эндпоинты

- POST `/api/webhook/bank/` — приём webhook от банка
- GET `/api/organizations/<inn>/balance/` — текущий баланс по ИНН

## Пример запроса

```json
{
  "operation_id": "ccf0a86d-041b-4991-bcf7-e2352f7b8a4a",
  "amount": 145000,
  "payer_inn": "1234567890",
  "document_number": "PAY-328",
  "document_date": "2024-04-27T21:00:00Z"
}
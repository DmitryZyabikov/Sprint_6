import requests

def test_email_name():
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2YTRmOWNjOWE1YzcxMjAwM2QwZWFiYjUiLCJpYXQiOjE3ODUxMDI1OTIsImV4cCI6MTc4NTcwNzM5Mn0.B_m6wMZ3hwd9AeDtW5vZlVQqrGCTbiNvj1oylK-7Sug'
    
    response = requests.get(
        'https://qa-mesto.praktikum-services.ru/api/users/me',
        headers={'Authorization': f'Bearer {token}'}
    )
    
    data = response.json()
    print(data)  # Посмотрим, какие данные приходят
    
    assert data['email'] == 'dmitriy47@yandex.ru', f"Ожидался email dmitriy47@yandex.ru, получен {data['email']}"
    print("Тест пройден: email совпадает")

test_email_name()
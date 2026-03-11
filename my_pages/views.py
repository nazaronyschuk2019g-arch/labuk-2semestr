from django.shortcuts import render

def home_view(request):
    context = {
        'title': 'Головна сторінка',
        'content': 'Це головна сторінка. Обирай, куди йти далі:',
        'is_main': True  # Цей прапорець скаже шаблону показати посилання на інші сторінки
    }
    return render(request, 'my_pages/base.html', context)

def page1_view(request):
    context = {
        'title': 'Перша сторінка',
        'content': 'Ти знаходишся на першій сторінці!',
        'is_main': False  # Цей прапорець скаже шаблону показати посилання НАЗАД на головну
    }
    return render(request, 'my_pages/base.html', context)

def page2_view(request):
    context = {
        'title': 'Друга сторінка',
        'content': 'Ти знаходишся на другій сторінці!',
        'is_main': False
    }
    return render(request, 'my_pages/base.html', context)
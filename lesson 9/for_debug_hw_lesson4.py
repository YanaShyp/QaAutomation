import textwrap
from datetime import datetime
from decimal import Decimal

"""
симулятор каси магазину
код, наведений нижче, приймає від покупця наступну інформацію про закупівлю 2-х товарів
- назва
- кількість (ціле число)
- ціна за одиницю
на підставі отриманих даних формується чек
всі ціни та вартість мають бути виведені в форматі з копійками, кількість - цілі числа
програма розрахована на використання на території України
"""

# goods 1 section
item_1_title = textwrap.shorten(input('Введіть назву першого товару: ').ljust(20, '.'), width=20, placeholder='...')

while True:
    try:
        item_1_quantity = int(input('Введіть бажаєму кількість першого товару: '))
        assert (item_1_quantity > 0), 'Number must be bigger than 0'
        break
    except ValueError:
        print("Введіть ціле число")


while True:
    try:
        item_1_zina = Decimal(float(input('Введіть ціну першого товару: ')))
        assert (item_1_zina > 0), 'Number must be bigger than 0'
        break
    except ValueError:
        print("Введіть число")


item_1_zina_right_format = item_1_zina.quantize(Decimal('1.00'))

# goods 2 section
item_2_title = textwrap.shorten(input('Введіть назву другого товару: ').ljust(20, '.'), width=20, placeholder='...')

while True:
    try:
        item_2_quantity = int(input('Введіть бажаєму кількість другого товару: '))
        assert (item_2_quantity > 0), 'Number must be bigger than 0'
        break
    except ValueError:
        print("Введіть ціле число")

while True:
    try:
        item_2_zina = Decimal(float(input('Введіть ціну другого товару: ')))
        assert (item_2_zina > 0), 'Number must be bigger than 0'
        break
    except ValueError:
        print("Введіть число")


item_2_zina_right_format = item_2_zina.quantize(Decimal('1.00'))


item_1_total_cost = Decimal(item_1_quantity) * Decimal(item_1_zina)
item_1_total_cost_right_format = item_1_total_cost.quantize(Decimal('1.00'))

item_2_total_cost = Decimal(item_2_quantity) * Decimal(item_2_zina)
item_2_total_cost_right_format = item_2_total_cost.quantize(Decimal('1.00'))

all_zina = Decimal(item_1_zina) + Decimal(item_2_zina)
all_zina_right_format = all_zina.quantize(Decimal('1.00'))

printing_template = '{}\t\t\t\t\t{}\t\t\t\t{}\t\t\t{}'

# printing receipt
print('\n\n\n')
print('фіскальний чек'.capitalize().center(80, '~'))
print('магазин "все для дому"'.upper().center(80))
print('Товар\t\t\t\t\t\t\t\t\tкількість\t\tціна(грн)\t\tвартість(грн)')
print(printing_template.format(item_1_title, item_1_quantity, item_1_zina_right_format, item_1_total_cost_right_format))
print(printing_template.format(item_2_title, item_2_quantity, item_2_zina_right_format, item_2_total_cost_right_format))
print('~' * 80)
print(printing_template.format(
    'ВСЬОГО'.ljust(20),
    item_1_quantity + item_2_quantity,
    all_zina_right_format,
    item_1_total_cost_right_format + item_2_total_cost_right_format
    )
)
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S').rjust(80))
print('\n\n')

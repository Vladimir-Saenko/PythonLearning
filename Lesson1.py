import sys

os = sys.platform
if 'linux' == os:
    print('Ваша ОС - Линуха')
else:
    print('Вы используете ОС', os)

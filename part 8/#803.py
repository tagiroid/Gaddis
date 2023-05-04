data = str(input('Enter your date of birth(dd/mm/yyyy): ')).split('/')

month = {'01': 'january', '02': 'february', '03': 'march', '04': 'april', '05': 'may', '06': 'june',
         '07': 'july', '08': 'august', '09': 'september', '10': 'october', '11': 'november', '12': 'december'}

print(f'{data[0]} {month.get(data[1])} {data[2]} y.')


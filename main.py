# Sw 1 Website
from pyscript import display, document


your_name = 'Amanda Cassiddy E. Bower'
age ='15'
height ='157.5'
countries3 =  ['USA, NYC','France, Paris', 'Japan, Tokyo']
student_type = False
me_dict = {'color': 'Yellow', 
           'car_brand': 'Toyota',
             'shoe_size': '8', 
             'best_friend': 'Nicole Manalang'}
fruits = set(['strawberry','mango', 'grapes','peach','kiwi'])
week_days = (1, 2, 3, 4, 5, 6, 7)

display(
    f'Hello! My name is {your_name}.\n'
    f'I am {age} years old.\n'
    f'My height is {height}.\n'
    f'Three countries I want to go to are {countries3}.\n'
    f'I am {student_type} new student.\n'
    f'Things about me: {me_dict}.\n'
    f'My 5 favorite fruits are {fruits}.\n'
    f'There are {week_days} days of the week.',
    target='result'
)

document.getElementById('result').innerHTML = (
    f'Hello! My name is {your_name}.<br>'
    f'I am {age} years old.<br>'
    f'My height is {height}.<br>'
    f'Three countries I want to go to are {countries3}.<br>'
    f'I am {student_type} new student.<br>'
    f'Things about me: {me_dict}.<br>'
    f'My 5 favorite fruits are {fruits}.<br>'
    f'There are {week_days} days of the week.'
)
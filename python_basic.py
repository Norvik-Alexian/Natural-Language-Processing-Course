from datetime import datetime

library = [('Author', 'Topic', 'Pages'),
           ('Twain', 'Rafting in water alone', 601),
           ('Faymen', 'Physics', 95),
           ('Hamilton', 'Mythology', 144)]

for author, topic, pages in library:
    print(f'{author:{10}} {topic:{30}} {pages:>{10}}')


today = datetime(year=2021, month=12, day=30)
print(f'\n{today:%B %d, %Y}')
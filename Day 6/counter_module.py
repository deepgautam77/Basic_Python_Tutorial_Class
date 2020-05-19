from collections import Counter
response = [
    'vanilla',
    'chocolate',
    'vanilla',
    'vanilla',
    'strawberry',
    'caramel',
    'caramel'
    ]

print("The maximum children loves ",Counter(response).most_common(1)[0][0])
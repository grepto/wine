from collections import defaultdict

WINES_FILE = 'vino.txt'


def serialize_wine(vine: list) -> dict:
    serialization_dict = {
        'Название': 'name',
        'Сорт': 'type',
        'Цена': 'price',
        'Картинка': 'image',
        'Выгодное предложение': 'promo',
    }

    serialized_vine = dict()

    for parameter in vine:
        try:
            attribute, value = parameter.split(': ')
        except ValueError:
            attribute, value = parameter.rstrip(':'), ''
        serialized_vine[serialization_dict[attribute]] = value

    serialized_vine['promo'] = 'promo' in serialized_vine

    return serialized_vine


def get_wines(wines_file: str = WINES_FILE) -> dict:
    wines = defaultdict(list)
    with open(wines_file, 'r', encoding='utf8') as wines_file:
        file_content = [row.strip() for row in wines_file]
    wine = []
    category = ''
    for row in file_content:
        if row.startswith('#'):
            _, category = row.split('# ')
        elif row:
            wine.append(row)
        elif wine:
            wines[category].append(serialize_wine(wine))
            wine = []

    wines[category].append(serialize_wine(wine))

    return wines


if __name__ == '__main__':
    print(get_wines())

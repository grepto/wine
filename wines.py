WINES_FILE = 'vino.txt'


def serialize_wine(vine: list) -> dict:
    serialize_dict = {
        'Название': 'name',
        'Сорт': 'type',
        'Цена': 'price',
        'Картинка': 'image',
        'Выгодное предложение': 'promo',
    }

    serialized_vine = dict()

    for line in vine:
        try:
            attribute, value = line.split(': ')
        except ValueError:
            attribute, value = line.rstrip(':'), ''
        serialized_vine[serialize_dict[attribute]] = value

    if 'promo' in serialized_vine:
        serialized_vine['promo'] = True

    return serialized_vine


def get_wines() -> dict:
    wines = dict()
    with open(WINES_FILE, 'r', encoding='utf8') as wines_file:
        file_content = [row.strip() for row in wines_file]
    wine = []
    category = ''
    for row in file_content:
        if row.startswith('#'):
            _, category = row.split('# ')
            wines[category] = []
        elif row:
            wine.append(row)
        elif wine:
            wines[category].append(serialize_wine(wine))
            wine = []

    wines[category].append(serialize_wine(wine))

    return wines

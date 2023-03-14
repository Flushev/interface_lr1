
META_DATA = [
    {
        "organization_name": "ООО Рога и копыта",
        "sub_organizations": ['Рога и копыта - Север', 'Рога и копыта - Юг'],
        "okpo": "65464644",
        "okpd": "A",
        "operation": "Учет",
        "response_persone": [
            {
                "name": "Петров Петр Петрович",
                "job": "Главный технолог"
            },
            {
                "name": "Сидоров Иван Федорович",
                "job": "Директор"
            }
        ]

    },
    {
        "organization_name": "ИП Иванов Иван Иванович",
        "sub_organizations": ["ИП Иванов Иван Иванович - Главное"],
        "okpo": "19154585",
        "okpd": "H",
        "operation": "Учет",
        "response_persone": [
            {
                "name": "Попов Никита Сергеевич",
                "job": "Управляющий"
            },
            {
                "name": "Иванов Иван Иванович",
                "job": "Директор"
            }
        ]

    },
    {
        "organization_name": "МБОУ Гимназия №123",
        "sub_organizations": ["МБОУ Гимназия №123 - Главное"],
        "okpo": "19154585",
        "okpd": "M",
        "operation": "Учет",
        "response_persone": [
            {
                "name": "Лабенко Татьяна Анатольевна",
                "job": "Зав. хоз."
            },
            {
                "name": "Иринина Ольга Александровна",
                "job": "Директор"
            }
        ]
    }
]

ITEMS_DATA = [
    {
        'item_name': 'Тарелка',
        'item_code': '001'
    },
    {
        'item_name': 'Кружка',
        'item_code': '002'
    },
    {
        'item_name': 'Стакан',
        'item_code': '003'
    },
    {
        'item_name': 'Ложка',
        'item_code': '004'
    },
    {
        'item_name': 'Вилка',
        'item_code': '005'
    }
]

AVAILABLE_ORGANIZATIONS = [item['organization_name'] for item in META_DATA]
AVAILABLE_ITEMS = [item['item_name'] for item in ITEMS_DATA]

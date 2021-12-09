def get_qss():
    with open('./Resources/qss/app.qss', encoding='utf-8') as f:
        return f.read()


def get_config():
    from json import loads
    with open('./Resources/json/config.json', encoding='utf-8') as f:
        return loads(f.read())
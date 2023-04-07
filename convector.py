import json
from datetime import datetime

ADD_FILE = "operations.json"


def read_file(file_json):
    with open(file_json, encoding="utf-8") as file:
        data = json.loads(file.read())
        return data


def executed(r_file):
    data = []
    for item_executed in r_file:
        if item_executed.get("state") == "EXECUTED":
            data.append(item_executed)
    return data


def sorted_date(data):
    s = sorted(data, key=lambda d: d["date"], reverse=True)
    return s[:5]


def card1(card):
    f = []
    card = card.split(" ")
    if card[0] in ("MasterCard", "Maestro"):
        f.append(card[0])
        card = [card[1][i:i + 4] for i in range(0, len(card[1]), 4)]

        for i, it in enumerate(card):
            if i == 2:
                it = "****"
            elif i == 1:
                it = it[0] + it[1] + "**"
            f.append(it)

    elif card[0] == "Visa":
        f.append(card[0] + " " + card[1])
        card = [card[2][i:i + 4] for i in range(0, len(card[2]), 4)]

        for i, it in enumerate(card):
            if i == 2:
                it = "****"
            elif i == 1:
                it = it[0] + it[1] + "**"
            f.append(it)
    elif card[0] == "Счет":
        card = card[0] + " **" + card[1][16:]
        f.append(card)
    return " ".join(f)


def hide_data(data):
    for item_executed in data:
        item_executed["date"] = datetime.strptime(item_executed.get('date').split('T')[0], "%Y-%m-%d").strftime("%d.%m.%Y")

        if item_executed.get("from"):
            item_executed["from"] = card1(item_executed["from"])
        else:
            item_executed["from"] = ''

        item_executed["to"] = card1(item_executed["to"])


    return item_executed


def output(data):
    for i in data:
        d = f"{i['date']} {i['description']}\n" \
            f"{i['from']} -> {i['to']}\n" \
            f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}.\n"
        print(d)


p = sorted_date(executed(read_file(ADD_FILE)))
hide_data(p)
output(p)



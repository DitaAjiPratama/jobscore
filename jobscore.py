def compare(history, data):

    for row in history:
        if row['year'] == data['from' ]:
            before = row
        if row['year'] == data['to'   ]:
            after  = row
        else:
            pass

    before_value = before ['salary'] / before ['based'][data['based']]
    after_value  = after  ['salary'] / after  ['based'][data['based']]
    change       = (after_value - before_value) / before_value * 100

    return change

def proposal(history, data):
    for row in history:
        if row['year'] == data['from']:
            before = row
        else:
            pass

    new_value = ((data['percent']/100)+1) * before['salary'] / before['based'][data['based']['type']] * data['based']['value']

    return new_value

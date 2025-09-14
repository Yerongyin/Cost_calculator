print('Loading...')
print('type q to leve.')
total=0
while True:
    amount=input('金额: ')
    if amount!='q':
        total+=float(amount)
        print(f'总额：{total}')
        continue
    else:
        break


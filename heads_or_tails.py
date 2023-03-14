class Coin:
    def __init__(self):
        self.side=None

    def throw(self):
        import random
        self.side=random.choice(['head','tail'])
        return self.side

    def __str__(self):
        return self.side
coin1=Coin()
coin2=Coin()
coin5=Coin()

balance=0
wins=0
losses=0

for i in range(100):
    while balance<20:
        coin1.throw()
        coin2.throw()
        coin5.throw()
        if (coin1.side=='head'):
            balance+=1
        if (coin2.side=='head'):
            balance+=2
        if (coin5.side=='head'):
            balance+=5
        print(f'Throw: {coin1.side}, {coin2.side}, {coin5.side}')
        print(f'Current balance: {balance}zl.')
        print()
    if balance==20:
        print('YOU WIN!')
        wins+=1
        balance=0
    else:
        print('YOU LOST')
        losses+=1
        balance=0

print(f'Final result: wins: {wins}, losses: {losses}')

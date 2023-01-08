import coin

def main():
    my_coin = coin.Coin()

    print('This side is up:', my_coin.get_sideup() )

    print('tossing a coin ten times:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

if __name__ == '__main__':
    main()
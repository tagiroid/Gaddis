# import animals

def main():
    show_mammal_info('Im random text')

def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()

if __name__ == '__main__':
    main()
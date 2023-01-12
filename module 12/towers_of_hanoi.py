def main():
    num_discs = 3
    from_peg = 1
    temp_peg = 2
    to_peg = 3

    move_discs(num_discs, from_peg, to_peg, temp_peg)
    print('All discs moved!')

def move_discs(num, frm, to, temp):
    if num > 0:
        move_discs(num - 1, frm, temp, to)
        print(f'Moving disc from tower {frm} to {to} tower')
        move_discs(num - 1, temp, to, frm)

if __name__ == '__main__':
    main()
"""
COMP.CS.100 Ohjelmointi 1: Inflaatiolaskin
Tekijä: Patrick Selin
Opiskelunumero: tuni.fi:xxxxx
Tehtävä: 3.3
"""

def main():
    """The main function is the only funcition and includes all the code.
    The purpose of this function is to count differences of inflation
    price. It asks user to input numbers and it prints the maximum rate
    change in decimal points.

    :param : no params.
    :return: print the output.
    """
    x = 1
    flag = ""
    numbers_lst = []

    while True:
        input_str = input(f"Enter inflation rate for month {x}: ")

        # tarkista onko painanut enter ja onko syöttänyt yli 2 lukua,
        # jotta voidaan antaa printtaus lupa lopussa
        if input_str == flag:
            if x == 1 or x == 2:
                print(
                    "Error: at least 2 monthly inflation rates must be entered.")
                can_print = False
                break
            # jos on antanut yli 2 lukua niin voidaan antaa lupa printata lopussa
            elif x > 2:
                can_print = True
                break
        # jos on lisännyt luvun, muunna floatiksi
        else:
            input_float = float(input_str)
            # lisää luku listan perällä
            numbers_lst.append(input_float)
            x += 1

    if can_print == True:
        # laske listan numeroiden suurin väli
        biggest_gap = max(numbers_lst[i + 1] - numbers_lst[i] for i in range(len(numbers_lst) - 1))
        # pyöristä floatti printtaa tulos
        print(f"Maximum inflation rate change was {round(biggest_gap, 1)} points.")

if __name__ == "__main__":
    main()


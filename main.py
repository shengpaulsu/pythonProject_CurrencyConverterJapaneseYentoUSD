def main():
    print("This program converts Japanese Yen to USD/EUR/CNY/KRW/NTD/AUD/IDR/INR")
    yen = eval(input("Enter amount in yen: "))

    dollars = convert_to_yen(yen)
    euro = convert_to_euro(yen)
    yuan = convert_to_yuan(yen)
    won = convert_to_won(yen)
    taiwandollar = convert_to_taiwandollar(yen)
    austrailiandollar = convert_to_australiandollar(yen)
    indonesianrupiah = convert_to_won(yen)
    indianrupee = convert_to_indianrupee(yen)

    print("That is", dollars, "Dollars (USD).")
    print("That is", euro, "Euros (EUR).")
    print("That is", yuan, "Yuan (CNY).")
    print("That is", won, "Won (KRW).")
    print("That is", taiwandollar, "Taiwan Dollar (NTD).")
    print("That is", austrailiandollar, "Australian Dollar (AUD).")
    print("That is", indonesianrupiah, "Indonesian Rupiah (IDR).")
    print("That is", indianrupee, "Indian Rupee (INR).")

convert_to_yen = lambda yen: yen * 0.0073
convert_to_euro = lambda euro: euro * 0.0069
convert_to_yuan = lambda yuan: yuan * 0.051
convert_to_won = lambda won: won * 9.52
convert_to_taiwandollar = lambda taiwandollar: taiwandollar * 0.22
convert_to_australiandollar = lambda australiandollar: australiandollar * 0.011
convert_to_indonesianrupiah = lambda indonesianrupiah: indonesianrupiah * 114.09
convert_to_indianrupee = lambda indianrupee: indianrupee * 0.60

main()
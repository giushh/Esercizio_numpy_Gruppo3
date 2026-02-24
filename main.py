
import Gabriele.csv_manager
import Ilaria.analisi

def main():
    print("****** Esercizio - Sistema analisi  *****")

    stop = False
    while not stop:

        scelta = input("\nPuoi:"
                       "\n1. Analisi su array 1D"
                       "\n2. Analisi su matrice 2D"
                       "\n3. Uscita"
                       "\nIndica il numero corrispondente \n> ")

        match scelta:
            case "1":
                n = int(input("\nNumero valori (N) da prelevare da file\n> "))
                arr = carica_array_1d(n)

                risultati = esegui_analisi_1d(arr)
                print("\n" + risultati)

                salva = input("Vuoi salvare i risultati? (s/n)\n> ").lower()
                if salva == "s":
                    nome_file = input("Nome file txt\n> ")
                    salva_risultati(risultati, nome_file)

            case "2":
                righe = int(input("\nNumero righe (N) da prelevare da file\n> "))
                colonne = int(input("Numero colonne (M) da prelevare da file\n> "))
                mat = carica_matrice_2d(righe, colonne)

                risultati = esegui_analisi_2d(mat)
                print("\n" + risultati)

                salva = input("Vuoi salvare i risultati? (s/n)\n> ").lower()
                if salva == "s":
                    nome_file = input("Nome file txt\n> ")
                    salva_risultati(risultati, nome_file)

            case "3":
                print("\n-- Uscita")
                stop = True

            case _:
                print("\nComando non valido. \nRiprova.")
                continue


if __name__ == "__main__":
    main()
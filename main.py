"""
DISCLAIMER
è da completare, abbiamo unito i pezzi ma dobbiamo farli funzionare insieme
"""

import Gabriele.csv_manager
import Ilaria.analisi


def main():
    print("****** Esercizio - Sistema analisi  *****")

    ultimo_file_csv = None

    stop = False
    while not stop:

        scelta = input("\nPuoi:"
                       "\n1. Generare file CSV con numeri casuali"
                       "\n2. Analisi su array 1D"
                       "\n3. Analisi su matrice 2D"
                       "\n4. Uscita"
                       "\nIndica il numero corrispondente \n> ")

        match scelta:

            case "1":
                nome_file = input("\nNome del file da creare\n> ").strip()
                quante_righe = int(input("Quanti numeri casuali generare?\n> "))

                file_creato = Gabriele.csv_manager.Riempi_con_casuali(nome_file, quante_righe)
                if file_creato is not None:
                    ultimo_file_csv = file_creato

            case "2":
                percorso = input(f"\nPercorso/Nome file CSV da cui estrarre i numeri (invio per '{ultimo_file_csv}')\n> ").strip()
                if percorso == "":
                    percorso = ultimo_file_csv

                if percorso is None:
                    print("\nErrore: prima crea un file (opzione 1) oppure inserisci un percorso valido.")
                    continue

                if not percorso.endswith(".csv"):
                    percorso += ".csv"

                n = int(input("Numero valori (N) da prelevare da file\n> "))

                arr = Gabriele.csv_manager.Prendi_numeri_casuali(percorso, n)
                if arr is None:
                    print("\nErrore: impossibile caricare/estrarre i dati.")
                    print(f"Hai inserito: {percorso}")
                    print("Se il file è stato creato, prova a premere invio al percorso per usare l'ultimo file generato.")
                    continue

                risultati = Ilaria.analisi.esegui_analisi_1d(arr)
                print("\n" + risultati)

                salva = input("Vuoi salvare i risultati? (s/n)\n> ").lower()
                if salva == "s":
                    nome_file = input("Nome file\n> ").strip()
                    Gabriele.csv_manager.salva_risultati(risultati, nome_file)

            case "3":
                percorso = input(f"\nPercorso/Nome file CSV da cui estrarre i numeri (invio per '{ultimo_file_csv}')\n> ").strip()
                if percorso == "":
                    percorso = ultimo_file_csv

                if percorso is None:
                    print("\nErrore: prima crea un file (opzione 1) oppure inserisci un percorso valido.")
                    continue

                if not percorso.endswith(".csv"):
                    percorso += ".csv"

                righe = int(input("Numero righe (N) della matrice\n> "))
                colonne = int(input("Numero colonne (M) della matrice\n> "))

                mat = Ilaria.analisi.carica_matrice_2d(percorso, righe, colonne)
                if mat is None:
                    print("\nErrore: impossibile creare la matrice 2D.")
                    print(f"Hai inserito: {percorso}")
                    continue

                risultati = Ilaria.analisi.esegui_analisi_2d(mat)
                print("\n" + risultati)

                salva = input("Vuoi salvare i risultati? (s/n)\n> ").lower()
                if salva == "s":
                    nome_file = input("Nome file\n> ").strip()
                    Gabriele.csv_manager.salva_risultati(risultati, nome_file)

            case "4":
                print("\n-- Uscita")
                stop = True

            case _:
                print("\nComando non valido. \nRiprova.")
                continue


if __name__ == "__main__":
    main()
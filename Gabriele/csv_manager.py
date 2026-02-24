

'''carica_array(n) che restituisce un array,
per prelevare i numeri  che riempiono l'array, n è scelto da utente

salva_risultati(risultati, nome file)  dove risultati è una stringa da salvare (sia per array che per matrice),

carica_matrice(righe, colonne) che restituisce una matrice'''


import pandas as pd
import os
import numpy as np


#carica csv
def load_csv(filepath: str):
    
    if not os.path.exists(filepath):
        return None
    try :
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError as e:
        print(f"errore:  {e}")
        return None


#mostra csv
def show_csv(percorso):
    
    
    df_risultato = load_csv(percorso)
    
    if df_risultato is not None:
        print("\n" + "="*30)
        print("DATI CARICATI CON SUCCESSO")
        print("="*30)
        
        print(df_risultato)
        
        print("-" * 30)
        print(f"Totale righe: {len(df_risultato)}")
    else:
        print("Operazione annullata per errore nel caricamento.")
        
        
        
#estrazione casuale        
def Prendi_numeri_casuali(percorso,n):
    df_ris =load_csv(percorso) 
    
    if df_ris is not None:
        try:
            max_righe = len(df_ris)
            print(f"il file ha tot righe: {max_righe}")
            
            quantitaU = n
            
            if 0 < quantitaU <= max_righe:
                estratti = df_ris.sample(n=quantitaU)
                print(f"\n--- Ecco i {quantitaU} numeri estratti ---")
                print(estratti)
                
                return estratti
            else:
                print("Numero non valido.")
                return None
            
        except ValueError:
            print("Errore: Inserisci un numero intero valido.")
            return None
    else:
        print("Errore nel caricamento del file per l'estrazione.")
        return None

    


#creazione array 1d
def carica_array(df_estratti):
    
    if df_estratti is not None:
        
        array_1d = df_estratti.values.flatten()
        return array_1d
    return None



#creazione matrice 
def carica_matrice_da_array(array1, array2):
    
        matrice = np.vstack((array1, array2))
        return matrice
   
    
    
    
    
   

#salva operazioni
def salva_risultati(risultati_str, nome_file):
    
    try:
        with open(nome_file, "w", encoding="utf-8") as f:
            f.write(risultati_str)
        print(f"Salvataggio completato in: {nome_file}")
    except Exception as e:
        print(f"Errore nel salvataggio: {e}")
    
    
    











import numpy as np

# analisi 1D

def analisi_1d_statistiche_base(arr):
    minimo = np.min(arr)
    massimo = np.max(arr)
    media = np.mean(arr)
    deviazione = np.std(arr)

    testo = ""
    testo += "--- Statistiche di base (1D) ---\n"
    testo += f"Min: {minimo}\n"
    testo += f"Max: {massimo}\n"
    testo += f"Media: {media}\n"
    testo += f"Deviazione standard: {deviazione}\n"
    return testo


def analisi_1d_posizionale(arr):
    indice_min = int(np.argmin(arr))
    indice_max = int(np.argmax(arr))

    p25 = np.percentile(arr, 25)
    p50 = np.percentile(arr, 50)
    p75 = np.percentile(arr, 75)

    testo = ""
    testo += "--- Analisi posizionale (1D) ---\n"
    testo += f"argmin: {indice_min}\n"
    testo += f"argmax: {indice_max}\n"
    testo += f"Percentili: 25%={p25} | 50%={p50} | 75%={p75}\n"
    return testo


def analisi_1d_searchsorted(arr, valore):
    arr_ordinato = np.sort(arr)
    posizione = int(np.searchsorted(arr_ordinato, valore))

    testo = ""
    testo += "--- searchsorted (1D) ---\n"
    testo += f"Valore: {valore}\n"
    testo += f"Posizione ordinata: {posizione}\n"
    return testo


def esegui_analisi_1d(arr):
    if arr.ndim != 1 or arr.size == 0:
        return "Dati non coerenti: serve un array 1D non vuoto.\n"

    testo = ""
    testo += analisi_1d_statistiche_base(arr) + "\n"
    testo += analisi_1d_posizionale(arr) + "\n"

    valore = float(input("\nInserisci un valore per searchsorted\n> "))
    testo += analisi_1d_searchsorted(arr, valore) + "\n"

    return testo


# analisi 2D

def analisi_2d_assi(mat):
    somma_colonne = np.sum(mat, axis=0)
    somma_righe = np.sum(mat, axis=1)

    media_colonne = np.mean(mat, axis=0)
    media_righe = np.mean(mat, axis=1)

    testo = ""
    testo += "--- Analisi per assi (2D) ---\n"
    testo += f"Somma colonne (axis=0): {somma_colonne}\n"
    testo += f"Somma righe (axis=1): {somma_righe}\n"
    testo += f"Media colonne (axis=0): {media_colonne}\n"
    testo += f"Media righe (axis=1): {media_righe}\n"
    return testo


def analisi_2d_operazioni(mat):
    trasposta = np.transpose(mat)
    norma = np.linalg.norm(mat)

    testo = ""
    testo += "--- Operazioni matriciali (2D) ---\n"
    testo += f"Trasposta:\n{trasposta}\n"
    testo += f"Norma (Frobenius): {norma}\n"
    return testo


def analisi_2d_prodotto(mat):
    testo = ""
    testo += "--- Prodotto matriciale (2D) ---\n"

    if mat.shape[0] != mat.shape[1]:
        testo += "Prodotto mat·mat non eseguibile (matrice non quadrata).\n"
        return testo

    prodotto = np.dot(mat, mat)
    testo += f"mat·mat:\n{prodotto}\n"
    return testo


def analisi_2d_covarianza(mat):
    cov = np.cov(mat.T)

    testo = ""
    testo += "--- Matrice di covarianza (2D) ---\n"
    testo += f"{cov}\n"
    return testo


def esegui_analisi_2d(mat):
    if mat.ndim != 2 or mat.size == 0:
        return "Dati non coerenti: serve una matrice 2D non vuota.\n"

    testo = ""
    testo += analisi_2d_assi(mat) + "\n"
    testo += analisi_2d_operazioni(mat) + "\n"
    testo += analisi_2d_prodotto(mat) + "\n"
    testo += analisi_2d_covarianza(mat) + "\n"

    return testo



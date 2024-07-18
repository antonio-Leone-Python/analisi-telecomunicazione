import pandas as pd
import numpy as np

#tempo stimato per il lavoro: minimo 3 ore

#creo una funzione con la funzione describe()
def esamina_distribuzione(df):  #1 munuto stimato per l'esecuzione, un minuto applicato      funzionante
    descrizione=df.describe()
    print(descrizione)

#creo la funzione per eliminare i valori cancanti      tempo stimato 2 minuti inizio 14:32 fine 14:38  funzionante
def elimina_spazi_vuoti(df):
    elimina_vuoto=df.dropna()
    print(elimina_vuoto)


#creo la funzione per la gestione anomalie             tempo stimato 15 minuti inizio ora 14:39  fine 14:44   funzionante 
def gestione_anomalie(df):
    pagamento_esagerato=df[df["tariffa_mensile"]>500]
    print(pagamento_esagerato)

#creo la funzione per creare un anuova colonna         tempo stimato 15 minuti inizio 14:48    fine 15:07 non funzionante
def nuova_colonna(df): 
    df["costo_per_giga"] = df["tariffa_mensile"] / df["dati_consumati"] 
    print(df)
    





 # creo un dizionario
dizionario = {
    "id": [1234,456,789,657],
    "eta": [34,67,90,99],
    "durata_abbonamento": [34,45,81,None],
    "tariffa_mensile": [345,500,789,435],
    "dati_consumati": [7,900,60,56],
    "servizio_clienti_contattati": [7,54,None,None],
    "churn":[True,False,True,False]
}

#creo un dataframe
df = pd.DataFrame(dizionario) 

nuova_colonna(df)





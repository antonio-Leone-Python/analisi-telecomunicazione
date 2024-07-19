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

#creo la funzione per creare un anuova colonna         tempo stimato 15 minuti inizio 14:48    fine 15:07 13:13 funzionante
def nuova_colonna(df): 
    df["costo_per_giga"] = df["tariffa_mensile"] / df["dati_consumati"] 
    print(df)

# esploro relazioni tra Età, Durata_Abonnamento, Tariffa_Mensile e la Churn.  tempo stimato 5 minuti 15:15  fine 15:43 funzionante
def esplora_relazioni(df):
    esplora = df.groupby("churn").mean()[["eta","durata_abbonamento","tariffa_mensile"]]
    print(esplora)
    
# identifico le possibili correlazioni del dataframe            tempo stimato 10/15 minuti 15:50    fine 14:57 funzionante
def possibili_relazioni(df):
    relazioni=df.corr()
    print(relazioni)
    
      
# converto la colonna churn in formato numerico(0,1)            tempo stimato 15 minuti 16:00        fine 16:54 funzionante
def conversione(dataframe):
    dataframe=df["churn"].map({"si":1,"no":0})
    print(dataframe)

#normalizzo le colonne numeriche                                 tempo stimato 25 minuti 17:15     fine 17:36
def normalizzazione(df):
    df['eta'] = (df['eta'] - df['eta'].mean()) / df['eta'].std()
    df['durata_abbonamento'] = (df['durata_abbonamento'] - df['durata_abbonamento'].mean()) / df['durata_abbonamento'].std()
    df['tariffa_mensile'] = (df['tariffa_mensile'] - df['tariffa_mensile'].mean()) / df['tariffa_mensile'].std()
    df['dati_consumati'] = (df['dati_consumati'] - df['dati_consumati'].mean()) / df['dati_consumati'].std()
    df['servizio_clienti_contattati'] = (df['servizio_clienti_contattati'] - df['servizio_clienti_contattati'].mean()) / df['servizio_clienti_contattati'].std()
    




 #importo il file csv da un altro modulo per la lettura
df=pd.read_csv("file.csv")


#creo il menu     tempo stimato 10 minuti   data inizio9:23
print("""menu
      1. per la descrizione del dataframe
      2. per eliminare gli spazi vuoti
      3. per gestire le anomalie
      4. per creare una nuova colonna con "costo_oer_giga"
      5. per per esplorare la relazione tra vari dati
      6. per avere le possibili relazione con il dataframe 
      7. per convertire la colonna churn in 0 e 1 
      8. esci
      """)
# creo il ciclo gestendo le varie opzioni
while True:
    scelta=input("seleziona un numero")
    if scelta=="1":
        esamina_distribuzione(df)
    elif scelta=="2":
        elimina_spazi_vuoti(df)
    elif scelta=="3":
        gestione_anomalie(df)
    elif scelta=="4":
        nuova_colonna(df)
    elif scelta=="5":
        esplora_relazioni(df)
    elif scelta=="5":
        possibili_relazioni(df)
    elif scelta=="6":
        conversione(df)
    elif scelta=="7":
        break                    












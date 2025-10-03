def carica_da_file(file_path):
    """Carica i libri dal file"""
    # TODO
    # creazione della biblioteca e dei libri con dizionari
    # leggendo la prima riga contenente il numero di sezioni
    try:
        file = open(file_path, 'r')
        num_sezioni = int(file.readline())
        biblioteca = {}
        for riga in file:
            riga = riga.strip()
            campi = riga.split(',')
            titolo = campi[0]
            autore = campi[1]
            anno_pubblicazione = int(campi[2])
            num_pagine = int(campi[3])
            sezione = campi[4]
            libro = {'titolo' : titolo,
                     'autore' : autore,
                     'anno_pubblicazione' : anno_pubblicazione,
                     'num_pagine' : num_pagine,
                     'sezione' : sezione}
            # se la sezione letta è nuova creo una sezione nuova(lista) e ci appendo i libri
            if sezione not in biblioteca:
                biblioteca[sezione] = []
            biblioteca[sezione].append(libro)
        file.close()
        return biblioteca
    except FileNotFoundError:
        return None

def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    # TODO
    # se esiste già il libro o se non esiste la sezione o non trova il file ritorno None
    sezione = str(sezione)
    if sezione not in biblioteca:
        return None
    for libro in biblioteca[sezione]:
        if libro['titolo'].lower() == titolo.lower():
            return None
    try:
        file = open(file_path, 'a')  # Apre il file in modalità append
        file.write(f"{titolo}, {autore}, {anno}, {pagine}, {sezione}\n")
        file.close()  # Chiude il file esplicitamente
    except FileNotFoundError:
        return None
    # altrimenti aggiungo il nuovo libro alla sezione richiesta
    nuovo_libro = {'titolo': titolo,
                   'autore': autore,
                   'anno_pubblicazione': anno,
                   'num_pagine': pagine,
                   'sezione': sezione}
    biblioteca[sezione].append(nuovo_libro)
    return nuovo_libro

def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO
    # itero in ogni sezione chiedendo se il libro chiesto è lo stesso di quello su cui sta iterando
    #  e poi alla fine se non ne ho trovato nessuno ritorna None
    for sezione in biblioteca.values():
        for libro in sezione:
            if libro['titolo'].lower() == titolo.lower():
                return f"{libro['titolo']}, {libro['autore']}, {libro['anno_pubblicazione']}, {libro['num_pagine']}, {libro['sezione']}"
    return None


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO
    # ordino ogni sezione per nome del libro, poi creo una lista contenente i titoli dei libri ordinati
    sezione = str(sezione)
    if sezione in biblioteca:
        ordinati = sorted(biblioteca[sezione], key=lambda libro: libro['titolo'].lower())
        titoli_ordinati = []
        for libro in ordinati:
            titoli_ordinati.append(libro['titolo'])
        return titoli_ordinati
    else:
        return None


def main():
    biblioteca = {}
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()


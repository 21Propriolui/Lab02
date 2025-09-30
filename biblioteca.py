def carica_da_file(file_path):
    """Carica i libri dal file"""
    # TODO
    try:
        file = open(file_path, 'r')
    except FileNotFoundError:
        return None
    max_sezioni = int(file.readline())
    biblioteca = {}
    for riga in file:
        riga = riga.strip()
        campi = riga.split(',')
        nome_libro = campi[0]
        autore = campi[1]
        anno_pubblicazione = int(campi[2])
        num_pagine = int(campi[3])
        sezione = campi[4]
        if sezione not in biblioteca:
            nome_libro = {'autore' : autore,
            'anno_pubblicazione' : anno_pubblicazione,
            'num_pagine' : num_pagine,
            'sezione' : sezione}
            biblioteca[sezione] = {sezione : nome_libro}
        file.close()
    return biblioteca

def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    # TODO


def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO
    titolo = input('Digitare il nome del titolo da cercare')
    for sezione in biblioteca:
        for libro in sezione:
            if titolo == libro['titolo']:
                output = f"{titolo}, {titolo['autore']}, {titolo['anno_pubblicazione']}, {titolo['num_pagine']}, {titolo['sezione']}"
                return output
            else:
                return None


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO
    sezione = input('Quale sezione si vuole ordinare?')
    if sezione in '12345':
        for s in biblioteca:
            if s == sezione:
                biblioteca[s].sort(key=lambda a: a['titolo'])
                titoli = (s['titolo'])
                return titoli
            else:
                return None


def main():
    biblioteca = []
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


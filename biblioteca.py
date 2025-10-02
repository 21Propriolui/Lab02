def carica_da_file(file_path):
    """Carica i libri dal file"""
    # TODO
    try:
        file = open(file_path, 'r')
    max_sezioni = int(file.readline())
    biblioteca = {}
    for riga in file:
        riga = riga.strip()
        campi = riga.split(',')
        titolo = campi[0]
        autore = campi[1]
        anno_pubblicazione = int(campi[2])
        num_pagine = int(campi[3])
        sezione = campi[4]
        if sezione not in biblioteca:
            libro = {'titolo' : titolo,
                     'autore' : autore,
                     'anno_pubblicazione' : anno_pubblicazione,
                     'num_pagine' : num_pagine,
                     'sezione' : sezione}
            biblioteca[sezione].apend(libro)
        return biblioteca
    except FileNotFoundError:
        return None

def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    # TODO
    sezione = str(sezione)
    if sezione not in biblioteca:
        return None
    for libro in biblioteca[sezione]:
        if libro['titolo'].lower() == titolo.lower():
            return None
    nuovo_libro = {'titolo' : titolo,
             'autore': autore,
             'anno_pubblicazione': anno,
             'num_pagine': pagine,
             'sezione': sezione}
    try:
        biblioteca[sezione].append(nuovo_libro)
        file = open(file_path, 'a')
        file.write(f"{titolo}\n, {autore}\n, {anno}\n, {pagine}\n, {sezione}\n")
        return nuovo_libro
    except FileNotFoundError:
        biblioteca[sezione].remove(libro)
        return None

def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO
    for sezione in biblioteca.values():
        for libro in sezione:
            if libro['titolo'].lower() == titolo.lower():
                return f"{libro['titolo']}, {libro['autore']}, {libro['anno_pubblicazione']}, {libro['num_pagine']}, {libro['sezione']}"
            else:
                return None


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO
    sezione = str(sezione)
    if sezione in biblioteca:
        ordinati = sorted(biblioteca[sezione], key=lambda libro: libro['titolo'].lower())
        titoli_ordinati = []
        for libro in ordinati:
            titoli_ordinati.append(libro['titolo'])
            return libro['titolo']
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


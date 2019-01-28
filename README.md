Projekt ma na celu proste porównanie prędkości przetwarzania danych za pomocą pakietu pandas w języku Python oraz pakietu DataFrames używanym w języku Julia.

Analiza została wykonana dla trzech typów operacji:
* grupowania
* sortowania
* ładowania pliku CSV.


# Co zrobić żeby skrypt był reprodukowalny
Konieczne zmiany należy wykonać w pliku `main.py`:
1. Zmiana ścieżki projektu (zmienna `path`)
2. Dodanie ścieżek dostępu do interpreterów Pythona i Julii (zmienne `python_exec` oraz `julia_exec`)

* Można także zmienić lub dodać kolumny do grupowania i sortowania, co wymaga rozszerzenia list argumentów odpowiednich fumkcji w plikach `script.py` oraz `script.jl`. W przypadku dodawanie nowych kolumn do sortowania lub grupowania najpierw należy dodać je na etapie generowania danych w pliku `main.py`.

# Wykonywanie skryptu
Do poprawnego wykonania analizy wystarczy uruchomić plik `main.py`, który jest "wrapperem" dla pozostałych dwóch skryptów `script.py` oraz `script.jl`. W tym pliku możliwe jest utalenie odpowiedniej ścieżki dostępu oraz interpreterów Pythona i Julii. Tutaj można także zmienić rozmiar generowanych danych, lub dodać ich kolejne wymiary.

Dane zostały wynenerowane sztucznie za pomocą generatora pseudolosowego. Wartości kolumny `key` są liczbami cąłkowitymi określonymi są za pomocą trzech atrybutów: 
* data_min - zakres minimum
* data_max - zakres maksimium
* n - liczebność.

Kolumna `value` przyjmuje wartości z rozkładu normalnego ~N(0,1).

Wygenerowane dane zapisywane są do pliku `data.csv` znajdującym się w głównym katalogu projektu. Następnie wywoływane są pliki `script.py` oraz `script.jl` gdzie wykonuje się faktyczne przetwarzanie danych. Powyższe skrypty mają za zadanie wczytanie wcześniej zapisanego pliku `data.csv`, grupowanie i sortowanie po wybranej kolumnie (domyślnie `key`) oraz zapisanie wyników do pliku. 

Następnie wyniki są wczytywane i dla każdej metryki tworzone są wykresy porównawcze.
 


# Wyniki
* Skrypt w Pythonie nie był w stanie stworzyć zbioru danych zawierającego 500 milionów wierszy (przy dwóch kolumnach)

* wykonywanie julii w REPLu vs z konsoli??

Credits: [db-benchmark](https://github.com/h2oai/db-benchmark)
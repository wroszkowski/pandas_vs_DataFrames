Projekt ma na celu proste porównanie prędkości przetwarzania danych za pomocą pakietu `pandas` w języku Python oraz pakietu `DataFrames` używanym w języku Julia.

Analiza została wykonana dla trzech typów operacji:
* ładowania pliku CSV
* grupowania
* sortowania.


# Co zrobić żeby skrypt był reprodukowalny
Konieczne zmiany należy wykonać w pliku `main.py`:
1. Zmiana ścieżki projektu (zmienna `path`)
2. Dodanie ścieżek dostępu do interpreterów Pythona i Julii (zmienne `python_exec` oraz `julia_exec`)

* Można także zmienić lub dodać kolumny do grupowania i sortowania, co wymaga rozszerzenia list argumentów odpowiednich funkcji w plikach `script.py` oraz `script.jl`. W przypadku dodawanie nowych kolumn do sortowania lub grupowania najpierw należy dodać je na etapie generowania danych w pliku `main.py`.


# Wykonywanie skryptu
Do poprawnego wykonania analizy wystarczy uruchomić plik `main.py`, który jest "wrapperem" dla pozostałych dwóch skryptów `script.py` oraz `script.jl`. W tym pliku możliwe jest ustalenie odpowiedniej ścieżki dostępu oraz interpreterów Pythona i Julii. Można tu także zmienić rozmiar generowanych danych, lub dodać ich kolejne wymiary.

Dane zostały wynenerowane sztucznie za pomocą generatora pseudolosowego. Wartości kolumny `key` są liczbami cąłkowitymi określonymi są za pomocą trzech atrybutów: 
* data_min - zakres minimum
* data_max - zakres maksimium
* n - liczebność.

Kolumna `value` przyjmuje wartości z rozkładu normalnego `~N(0,1)`.

Wygenerowane dane zapisywane są do pliku `data.csv` znajdującym się w głównym katalogu projektu. Następnie wywoływane są pliki `script.py` oraz `script.jl` gdzie wykonuje się faktyczne przetwarzanie danych. Powyższe skrypty mają za zadanie wczytanie wcześniej zapisanego pliku `data.csv`, grupowanie i sortowanie po wybranej kolumnie (domyślnie `key`) oraz zapisanie wyników do pliku. 

Następnie, powyższe wyniki są wczytywane i dla każdej metryki tworzone są wykresy porównawcze zapisywane w katalogu `/charts`. 


# Wyniki
Skrypt został wykonany dwukrotnie dla 5 różnych rozmiarów zbioru:
- 500 000,
- 5 000 000,
- 50 000 000,
- 100 000 000,
- 200 000 000 wierszy.

Nie udało się stworzyć zbioru danych zawierającego 500 milionów wierszy (przy dwóch kolumnach) z powodu braku pamięci. Zbiór 100 milionów wierszy zajmował 5.31 GB pamięci na dysku twardym. Analiza została wykonana na komputerze z systemem operacyjnym Windows 10 (64 bit) posiadającej 8 GB pamięci RAM oraz procesor Intel Core i7-7500 2.90 GHz.

Wykresy w folderze `/charts` pokazują porównanie czasu wykonania jednej z trzech operacji: ładowania pliku CSV, grupowania oraz sortowania. Jednostką na osi OX są sekundy. Nie uwzględniają czasu kompilacji ani załadowania bibliotek.

W 13 z 15 operacji pakiet `pandas` okazywał się szybszy od `Dataframes`. Jedynie sortowanie 200 milionów wierszy, oraz jedno podejście do grupowania 100 milionów wierszy okazało się szybsze w Julii. Największe różnice w wydajności obu rozwiązań widać w operacji ładowania pliku CSV do pamięci. `pandas` był między ~30x a ~3x szybszy dla kolejnych rozmiarów zbioru. W przypadku grupowania danych, różnica między pakietami zmiejszała się wraz ze zwiększaniem zbioru. Różnice na najmniejszym zbiorze sięgały kilkudziesięciokrotności, podczas gdy grupowanie zbioru o rozmiarze 100 milionów wierszy zajęło już niemal tyle samo. Najmniejsze różnice można zauważyć w czasie sortowania. Różnica czasu wykonania spadała systematycznie wraz ze wzrostem rozmiaru zbioru, by przy 200 milionach wierszy okazało się, że `DataFrames` wykonuje operację sortowania nieco szybciej niż `pandas` (376.298s vs. 508.035s).

Ogólna tendecja wskazuje na to, że im wiekszy rozmiar danych, tym różnice między pakietem `pandas` w Pythonie i `DataFrames` w Julii zmniejszają się. `pandas` radzi sobie o wiele lepiej z mniejszymi zbiorami danych, ale `DataFrames` zaczyna zdobywać przewagę w zbiorach zawierających ponad 200 milionów wierszy.


Credits: [db-benchmark](https://github.com/h2oai/db-benchmark)
# API-automation
> script was created by: Xhelios05X
> github.com/Xhelios05X
----------------------------------
eng. below

Repozytorium zawiera skrypty automatyzujące pewne zadania odwołujące się do różnych API: news-api, api NBP oraz Shodan api.

## CurrencyExchangeRate.py

Skrypt zwraca aktualny kurs zadanej waluty oraz zmiany kursów tej waluty w ostatnich 5 dniach.

### Użycie:

za pomocą iterpretera python3:

```shell
python3 CurrencyExchangeRate.py [-h] currency
```

alternatywnie dla systemu Linux:

```shell
chmod +x ./CurrencyExchangeRate.py

./CurrencyExchangeRate.py [-h] currency
```

## newsSearch.py

Skrypt pobiera słowo kluczowe ('keyword') na temat którego użytkownik chciałby otrzymać infromacje. **Warunkiem działania programu jest podanie klucza API dla serwisu [newsAPI](https://newsapi.org/)**:
Account > API key

### Użycie:

za pomocą interpretera python3:

```shell
python3 newsSearch.py [-h] APIkey keyword
```

alternatywnie dla systemu Linux:

```shell
chmod +x ./newsSearch.py

./newsSearch.py [-h] APIkey keyword
```

## shodanSearch.py

Dzięki skryptowi można poznać aktywne porty określonego hosta. Program używa API Shodan do wykrywania aktywnych portów. **Warunkiem działania skryptu jest podanie klucza API dla serwisu [Shodan](https://developer.shodan.io/?language=en)**: 
login > logowanie > prawy górny róg > `Show API key`

### Użycie:

za pomocą interpretera python3:

```shell
python3 shodanSearch.py [-h] APIkey hostIP
```

alternatywnie dla systemu Linux:
```shell
chmod +x ./shodanSearch.py

./shodanSearch.py [-h] APIkey hostIP
```
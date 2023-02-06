# DeepGravityTool, la user interface di DeepGravity

## Introduzione al DeepGravity Tool
Lo scopo di DeepGravity Tool è quello di aiutare utenti nell’esecuzione dell’algoritmo DeepGravity, offrendo una GUI che si occupi di eseguire codice a linea di comando. L’idea del tool, nasce a causa dell’importanza che DeepGravity potrebbe riservare e che potrebbe però passare in sordina a causa della poca facilità di utilizzo, se non si non si è avvezzi al mondo informatico, dell’algoritmo stesso.

## Installazione del DeepGravity Tool
### Consigli per l'installazione
Per poter instalalre sia DeepGravity che DeepGravity Tool, è consigiabile la realizzazione di un enviroment, ad esempio mediante Anaconda Navigator. Sia DeepGravity che DeepGravity Tool dovranno essere scaricati, con relative librerie, nello stesso enviroment, in modo tale da rendere più facile l'esecuzione e la corrispettiva installazione.

### Prerequisiti
Per poter funzionare correttamente, il DeepGravity Tool necessita l'installazione di DeepGravity, reperiribile al [link qui indicato](https://github.com/scikit-mobility/DeepGravity). Una volta installato DeepGravity, è possibile seguire i passaggi sotto riportati per installare anche DeepGravity Tool.

### Step per l'installazione
Scaricato DeepGravity Tool dalla seguente repository come ulteriore passaggio, per far sì che il tool funzioni è necessario installare la versione 4.1.4 di Django. Poiché Django alla creazione del progetto fornisce una SECRET KEY che deve rimanere personale, per far sì che il tool funzioni è necessario installare la versione 3.6 della libreria "python-decouple" e la versione 3.2.1 di "python-extensions".
La gestione della SECRET KEY avverrà per mezzo del file ".env", che dovrà essere creato nello stesso folder contenente il file "manage.py" di DeepGravityTool. All’interno del file ".env" dovrà poi essere creata una variabile chiamata "SECRET KEY". A quest’ultima dovrà essere passata la stringa ottenuta come risultato del "python manage.py generate_secret_key". Tale comando, dovrà essere però eseguito all’interno di DeepGravity Tool, dovendo quindi arrivare, mediante linea di comando, al folder contenente il file "manage.py". 

### Esecuzione di DeepGravity Tool
È ora possibile avviare il tool mediante codice "python manage.py runserver", nello stesso folder in cui è stato eseguito il comando per la creazione della SECRET KEY. Se l'installazione del tool è andata a buon fine nel codice in risposta al comando sarà riportato il link al tool. Basterà copiare ed incollare quest’ultimo nel browser di ricerca per poter iniziare a lavorare.

Per poter garanture il funzionamento di DeepGravity, sarà però necessario assicurarsi che la variabile "main_path" e "plots_path" siano state correttamente modificate con il path assoluto che rispettivamente porta ai file main.py di DeepGravity e con il file "plots.ipynb" di DeepGravity.

### Modifica del file "plots.ipynb"
Di tutti i file necessari per l’esecuzione di DeepGravity, il file "plots.ipynb" sarà l’unico che necessiterà di una modifica, questo poichè esso lavora con ulteriori path mediante cui andrà a prelevare i files excel e salvare il file pdf raffigurante il grafo. Sarà, inoltre, necessario modificare il valore della variabile "country" in base alla regione di interesse che si sta analizzando. I path da modificare, se si sta eseguendo il file .ipynb, si troveranno nel secondo blocco di istruzioni e nell’ultimo blocco di istruzioni. È inoltre da considerare che, per come DeepGravity è stato progettato, i file excel, una volta ottenuti, dovranno essere rinominati, aggiungendo, in append, un " 0", " 1", ..., " i" dove i rappresenta l’iesima nonché ultima esecuzione di DeepGravity.


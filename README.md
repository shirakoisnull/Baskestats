# 🏀 Baskestats - Εργασία Μηχανικής Λογισμικού 2023-24
## 📘 Περιγραφή
Το Baskestats είναι μια εφαρμογή που αποσκοπεί στην αποθήκευση και ανάκτηση στατιστικών παιχτών και ομάδων καθώς και στην διεξαγωγή πρωταθλημάτων μπάσκετ. Η εφαρμογή αποτελείται από τρία μέρη: Backend (API, Database) και Frontend.
- Το backend είναι υπεύθυνο για την αποθήκευση και ανάκτηση δεδομένων σε μια βάση δεδομένων και την επικοινωνία με το API. 
- Το frontend είναι υπεύθυνο για την εμφάνιση των δεδομένων στον χρήστη και την επικοινωνία με το API. 
- Το API είναι υπεύθυνο για την επικοινωνία του backend με το frontend. Το API είναι υλοποιημένο σε Python με την χρήση του `Flask` framework. 

## ⚙️ Προαπαιτούμενα
> Για να τρέξετε την εφαρμογή θα πρέπει να έχετε εγκατεστημένα τα παρακάτω:
> - [Python](https://www.python.org/downloads/)
> - [Node.js](https://nodejs.org/en/download/)
> - Επιπλέον, θα πρέπει να έχει ρυθμιστεί μια MySQL βάση σύμφωνα με τις [οδηγίες εδώ.](database/README.md)

## 🚀 Συνοπτικές οδηγίες
Θα πρέπει να εγκαταστήσετε τις απαραίτητες βιβλιοθήκες για το [backend](backend/README.md) και το [frontend](app/README.md). 

Ανοίξτε ένα τερματικό στον φάκελο `backend`, εκτελέστε την εντολή 
```bash
pip install -r requirements.txt
```
κατόπιν, δημιουργήστε ένα `.env` αρχείο που περιλαμβάνει τα στοιχεία σύνδεσης στη βάση σας:
```
DB_HOST = <your DB hostname>
DB_USER = <your DB username>
DB_PASSWORD = <your DB password>
DB_NAME = <your DB name>
JWT_SECRET_KEY = <your jwt authentication secret key>
```
και έπειτα:
```bash
python run_backend.py
```
Στην συνέχεια ανοίξτε ένα τερματικό στον φάκελο `app/client/baskestats` και εκτελέστε την εντολή 
```bash
npm install
```
και έπειτα:
```bash
npm run dev
```
## 📖 Αναλυτικές Οδηγίες
* [Οδηγίες backend](backend/README.md)

* [Οδηγίες frontend](app/README.md)

* [Οδηγίες database](database/README.md)

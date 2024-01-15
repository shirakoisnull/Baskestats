# 🏀 Baskestats - Εργασία Μηχανικής Λογισμικού 2023-24
## 📘 Περιγραφή
Το Baskestats είναι μια εφαρμογή που αποσκοπεί στην αποθήκευση και ανάκτηση στατιστικών παιχτών και ομάδων καθώς και στην διεξαγωγή πρωταθλημάτων μπάσκετ. Η εφαρμογή αποτελείται από τρία μέρη: Backend (API, Database) και Frontend.
- Το backend είναι υπεύθυνο για την αποθήκευση και ανάκτηση δεδομένων σε μια βάση δεδομένων και την επικοινωνία με το API. 
- Το frontend είναι υπεύθυνο για την εμφάνιση των δεδομένων στον χρήστη και την επικοινωνία με το API. 
- Το API είναι υπεύθυνο για την επικοινωνία του backend με το frontend. Το API είναι υλοποιημένο σε Python με την χρήση του `Flask` framework. 

## ⚙️ Προαπαιτούμενα
> Για να τρέξετε την εφαρμογή θα πρέπει να έχετε εγκατεστημένα τα παρακάτω:
> - [Python 3.9](https://www.python.org/downloads/)
> - [Node.js](https://nodejs.org/en/download/)
> - [MySQL Server](https://dev.mysql.com/downloads/mysql/)

## 🚀 Συνοπτικές οδηγίες
Θα πρέπει να εγκαταστήσετε τις απαραίτητες βιβλιοθήκες για το backend και το frontend. Ανοίξτε ένα τερματικό στον φάκελο `backend`, εκτελέστε την εντολή 
```bash
pip install -r requirements.txt
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

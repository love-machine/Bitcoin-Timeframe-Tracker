# BTC TRACKER

![image](https://github.com/user-attachments/assets/64f17efb-809b-4580-b759-ec091606f2df)


Un outil de suivi des données Bitcoin en temps réel qui récupère les informations OHLCV (Open, High, Low, Close, Volume) de Binance à différents intervalles de temps et les enregistre dans des formats facilement exploitables.

![BTC Tracker Banner](https://via.placeholder.com/800x200?text=BTC+TRACKER)

## 📋 Fonctionnalités

- ✅ Collecte des données OHLCV du Bitcoin sur plusieurs timeframes (1m à 1 semaine)
- ✅ Mise à jour automatique à intervalle régulier
- ✅ Exportation des données au format CSV et/ou Excel
- ✅ Génération de graphiques pour chaque timeframe
- ✅ Interface en ligne de commande avec bannière personnalisée
- ✅ Journalisation des événements et erreurs

## 🔧 Installation

### Prérequis

- Python 3.13 ou supérieur
- pip (gestionnaire de paquets Python)

### Dépendances

```bash
pip install asyncio aiohttp pandas openpyxl matplotlib
```

### Configuration

Clonez ce dépôt et naviguez dans le répertoire du projet :

```bash
git clone https:/love-machine/github.com//btc-tracker.git
cd btc-tracker
```

## 🚀 Utilisation

Exécutez le script principal :

```bash
python BitcoinTimeframeTracker.py
```

Vous serez invité à choisir un format de sortie :
1. CSV uniquement
2. Excel uniquement
3. Les deux formats

Le programme commencera alors à collecter des données et à générer des graphiques pour chaque timeframe.

## 📊 Timeframes disponibles

Le tracker surveille les données Bitcoin sur les timeframes suivants :
- 1 minute (1m)
- 3 minutes (3m)
- 5 minutes (5m)
- 15 minutes (15m)
- 30 minutes (30m)
- 1 heure (1h)
- 2 heures (2h)
- 4 heures (4h)
- 6 heures (6h)
- 8 heures (8h)
- 12 heures (12h)
- 1 jour (1d)
- 3 jours (3d)
- 1 semaine (1w)

## 📁 Structure des fichiers de sortie

### Fichier CSV (crypto_data.csv)
Contient les données au format suivant :
```
timeframe,timestamp,open,high,low,close,volume
1m,2023-04-04 15:30:00,27954.32000000,27955.00000000,27950.04000000,27952.60000000,12.55940000
...
```

### Fichier Excel (crypto_data.xlsx et DATA_crypto.xlsx)
Contient les mêmes données que le CSV mais dans un format tabulaire Excel.

### Graphiques (btcusdt_[timeframe].png)
Un graphique en ligne est généré pour chaque timeframe, montrant l'évolution du prix de clôture.

## 🧩 Architecture du code

- **Initialisation** : Configuration des variables globales et paramètres initiaux
- **Récupération des données** : Utilisation d'API asynchrones pour interroger Binance
- **Traitement des données** : Organisation et formatage des données OHLCV
- **Exportation** : Enregistrement au format CSV/Excel et génération de graphiques
- **Interface utilisateur** : Interface en ligne de commande pour les options d'exportation

## 📝 Journal des événements

Le programme crée un fichier `crypto_tracker.log` qui enregistre toutes les actions et erreurs pendant l'exécution.

## ⚠️ Avertissement

Ce programme est fourni à des fins éducatives et informatives uniquement. Les données de marchés financiers comportent des risques et les performances passées ne préjugent pas des performances futures. Utilisez cet outil avec prudence dans le cadre de vos décisions d'investissement.

## 🙏 Remerciements

- [Binance API](https://github.com/binance/binance-spot-api-docs) pour l'accès aux données de marché

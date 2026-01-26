# DEVLOG

## [2026-01-24] Initialisation & Ingestion Binance

### Réalisé
- Mise en place de la structure du projet (directives, app, storage).
- Implémentation du client d'ingestion Binance (`app/ingestion/binance_client.py`).
- Utilisation de `pandas` pour transformer les listes brutes en DataFrame typé et indexé.
- Merge de la feature `ingestion-binance` sur `main`.

### Appris
- **Pandas** : `iloc` pour le slicing, `to_datetime` avec `unit='ms'`, et `set_index`.
- **Git** : Gestion des branches (divergence local/remote réparée avec `pull --no-rebase`).
- **SQLite** : Distinction entre `Connection` (l'autoroute) et `Cursor` (le camion/magasinier).
- **Architecture** : Ne JAMAIS fermer la connexion (`con.close()`) à l'intérieur d'une boucle d'insertion qui réutilise le curseur.

## [2026-01-26] Stockage SQLite

### Réalisé
- Implémentation de `app/storage/db.py`.
- Création de la table `klines` avec `init_db`.
- Fonction `save_klines` avec gestion des doublons (`INSERT OR IGNORE`).


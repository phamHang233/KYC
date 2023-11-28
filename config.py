import os


# class PostgresDBConfig:
    # SCHEMA = os.environ.get("POSTGRES_SCHEMA", "chain_")
    # TRANSFER_EVENT_TABLE = os.environ.get("POSTGRES_TRANSFER_EVENT_TABLE", "token_transfer")
    # CONNECTION_URL = os.environ.get("POSTGRES_CONNECTION_URL", "postgresql://centic_intern:kstn_k65_k66@34.126.75.56:5432/postgres")

class PostgresDBConfig:
    SCHEMA = os.environ.get("POSTGRES_SCHEMA", "chain_0x1")
    TRANSFER_EVENT_TABLE = os.environ.get("POSTGRES_TRANSFER_EVENT_TABLE", "token_transfer")
    CONNECTION_URL = os.environ.get("POSTGRES_CONNECTION_URL", "postgresql://centic_intern:kstn_k65_k66@34.126.75.56:5432/postgres")

class MongoETLConfig:
    HOST = "mongodb://etlReaderAnalysis:etl_reader_analysis__Gr2rEVBXyPWzIrP@34.126.84.83:27017,34.142.204.61:27017,34.142.219.60:27017/"
    USERNAME = "root"
    PASSWORD = "dev123"
    # KLG_DATABASE = "klg_database"
    DATABASE = "blockchain_etl"
    blocks ='blocks'

class MongoDbKLGConfig:
    HOST = "mongodb://klgReaderAnalysis:klgReaderAnalysis_4Lc4kjBs5yykHHbZ@35.198.222.97:27017,34.124.133.164:27017,34.124.205.24:27017/"
    USERNAME = "root"
    PASSWORD = "dev123"
    # KLG_DATABASE = "klg_database"
    KLG_DATABASE = "knowledge_graph"
    KLG = "knowledge_graph"
    WALLETS = "wallets"
    MULTICHAIN_WALLETS = "multichain_wallets"
    DEPOSITS = "deposits"
    BORROWS = "borrows"
    REPAYS = "repays"
    WITHDRAWS = "withdraws"
    LIQUIDATES = "liquidates"
    SMART_CONTRACTS = "smart_contracts"
    CONFIG = 'configs'
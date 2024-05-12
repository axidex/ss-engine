from src.configs.postgres_config import PostgresConfig


class ReadData:
    """"""

    def __init__(self, config: dict, creds: dict):
        """"""

        self.config = config
        self.creds = creds

    def get_postgres_config(self) -> PostgresConfig:
        """Read database secrets"""

        db_host = self.config['host']
        db_port = self.config['port']
        db_database = self.config['database']

        with open(self.creds["username"]) as f:
            db_user = f.readline().strip()

        with open(self.creds["password"]) as f:
            db_password = f.readline().strip()

        return PostgresConfig(db_user, db_password, db_host, db_port, db_database)
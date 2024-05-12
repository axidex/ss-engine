from dataclasses import dataclass

@dataclass
class PostgresConfig:
    """"""

    username: str
    password: str
    host: str
    port: str
    database: str

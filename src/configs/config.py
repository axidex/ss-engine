import yaml

from src.utils.read_data import ReadData
from src.utils.wait import wait_secret

with open('config.yml') as f:
    config: dict = yaml.safe_load(f)

app_port = config["app"]["port"]

logpath = config.get("logpath", "./logs")

tmp_path = config.get("tmp", "./tmp")

gl_path = config["path_to_gl_bin"]
ds_path = config["path_to_ds_bin"]

prefixes_to_remove = config["prefixes_to_remove"]

ds_timeout = config["ds"]["timeout"]
gl_timeout = config["gl"]["timeout"]

ds_args = config["ds"]["args"]
gl_args = config["gl"]["args"]

max_unpacked_size = config["max_unpacked_size"]
max_unpacked_size_ds = config["ds"]["max_unpacked_size"]

postgres_config = config["db"]
postgres_creds: dict[str, str] = config["secrets"]["postgres"]

for path in postgres_creds.values():
    wait_secret(path)

postgres_config = ReadData(config=postgres_config, creds=postgres_creds).get_postgres_config()

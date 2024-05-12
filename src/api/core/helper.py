from src.configs import config

class Helper:

    working = False
    task_id = ""
    max_file_size = config.max_unpacked_size * 1024 * 1024
    max_file_size_ds = config.max_unpacked_size_ds * 1024 * 1024

    @staticmethod
    def engine_start(task_id: str):
        Helper.working = True
        Helper.task_id = task_id

    @staticmethod
    def engine_stop():
        Helper.working = False
        Helper.task_id = "IDLE"
        
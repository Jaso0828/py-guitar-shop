from core.guitars.guitars import Guitar


class GuitarRepo:
    def __init__(self, repo_type: str):
        self.repo_type = repo_type
        self.file_path = ''
        self._db_connection_string = ''


    def _configure(self, repo_type: str):
        if repo_type == 'file':
            self._

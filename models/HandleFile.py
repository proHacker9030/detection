from Web1Project.models import Result


class HandleFile:
    def __init__(self, file, method_id):
        self.file = file
        self.method_id = method_id

    def handle(self):
        # TODO: refactor
        file = "result.jpg"
        return file

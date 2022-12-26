from threading import Thread


class CellsThread(Thread):
    def __init__(self):
        super().__init__(name="thr-cells", daemon=True)

    def open_cell(self):
        pass
import math
from processingTables.processingTableContract import ProcessingTableContract

class AbstractProcessingTable(ProcessingTableContract):
    def __init__(self):
        self._processCallback = []

    def sizeControl(self, size: int) -> int:
        if size <= 0:
            raise ValueError("Only positive number")
        return size

    def processTable(self, size: int, chunkSize: int = 1000) -> str:
        size = self.sizeControl(size)
        maxWidth = len(f"{size} x 10 = {size * 10}")
        columnSpacing = 5

        chunks = math.ceil(size / chunkSize)
        result = ""

        for chunk in range(chunks):
            start = chunk * chunkSize + 1
            end = min((chunk + 1) * chunkSize, size)

            for i in range(start, end + 1):
                line = ""
                for j in range(1, 11):
                    formattedResult = f"{i} x {j} = {i * j}"
                    line += f"{formattedResult:<{maxWidth + columnSpacing}}"
                result += line + "\n"

        self.callbackRun(result)
        return result

    def processCallback(self, callback: callable) -> None:
        self._processCallback.append(callback)

    def callbackRun(self, result) -> None:
        for callback in self._processCallback:
            callback(result)

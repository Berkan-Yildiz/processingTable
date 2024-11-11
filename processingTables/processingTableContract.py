class ProcessingTableContract:
    def sizeControl(self, size: int) -> int:
        pass

    def processTable(self, size: int) ->str:
        pass

    def processCallback(self, callback: callable) -> None:
        pass

    def callbackRun(self, result) -> None:
        pass

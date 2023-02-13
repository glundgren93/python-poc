from abc import ABC, abstractmethod

class IHttpServer(ABC):
    @abstractmethod
    def on (self, method, url, callback):
        pass
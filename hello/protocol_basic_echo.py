from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor


class Echo(Protocol):

    def receivedData(self, data):
        self.transport.write(data)


class QOTD(Protocol):

    def connectionMade(self):
        self.transport.write("An apple a day keep the doctor away\r\n")
        self.transport.loseConnection()


class QOTDFactory(Factory):

    def buildProtocol(self, addr):
        return QOTD()

if __name__ == '__main__':
    # 8007 is the port you want to run under. Choose something > 1024
    endpoint = TCP4ServerEndpoint(reactor, 8007)
    endpoint.listen(QOTDFactory())
    reactor.run()

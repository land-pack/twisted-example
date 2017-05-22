from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor


class QOTD(Protocol):

    def connectionMade(self):
    	"""
    	When the Protocol bind to the Factory
    	There no attribute call `factory` bind to the Protocol ~~
    	so when you access the self.factory.quote you will see quote from factory ~~
    	"""
        # self.factory was set by the factory's default buildProtocol

        self.transport.write(self.factory.qoute + '\r\n')
        print("self.attribue=%s" % dir(self.factory))
        self.transport.loseConnection()
        # self.transport.abortConnection() # twisted version 10.0+


class QOTDFactory(Factory):
    # This will be used by the default buildProtocol to create a new protocols
    protocol = QOTD

    def __init__(self, qoute=None):
    	print("Init factory ....")
        self.qoute = qoute or 'An apple a day keeps the doctor away'


if __name__ == '__main__':


	endpoint = TCP4ServerEndpoint(reactor, 8007)
	endpoint.listen(QOTDFactory("Configurable quote"))
	reactor.run()
	# q = QOTDFactory("Hello world")
	# print(dir(q))

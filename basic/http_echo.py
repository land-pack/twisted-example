from twisted.internet import protocol, reactor, endpoints

class Echo(protocol.Protocol):

	def dataReceived(self, data):
		"""
		Override this method!
		"""
		self.transport.write(data)

class EchoFactory(protocol.Factory):
	def buildProtocol(self, addr):
		"""
		Override this method
		"""
		return Echo()

endpoint = endpoints.serverFromString(reactor, "tcp:1234")
endpoint.listen(EchoFactory())
reactor.run()
import sys
import traceback
from twisted.web.static import File
from twisted.python import log
from twisted.web.server import Site
from twisted.internet import reactor, defer

from autobahn.twisted.websocket import WebSocketServerFactory, \
    WebSocketServerProtocol

from autobahn.twisted.resource import WebSocketResource


class SomeServerProtocol(WebSocketServerProtocol):

    
    def makeConnection(self, request):
        return True

    def onOpen(self):
        print("WebSocket connection open.")

    def onConnect(self, request):
        print("some request connected {}".format(request))

    def onMessage(self, payload, isBinary):
        self.sendMessage("message received")

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {}".format(reason))


if __name__ == "__main__":
    # defer.Deferred.debug = True
    # failure.startDebugMode()
    log.startLogging(sys.stdout)


    # static file server seving index.html as root
    root = File("/")

    factory = WebSocketServerFactory(u"ws://localhost:9009/ws")
    factory.protocol = SomeServerProtocol
    resource = WebSocketResource(factory)
    # websockets resource on "/ws" path
    root.putChild(u"/ws", resource)

    site = Site(root)
    reactor.listenTCP(9009, site)
    reactor.run()
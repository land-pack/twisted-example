from twisted.web import server, resource
from twisted.internet import reactor, endpoints

class Counter(resource.Resource):
	isLeaf = True
	numberRequests = 0
	allowedMethods = ("GET","HEAD")
	def render_GET(self, request):
		self.numberRequests += 1
		request.setHeader(b"content-type", b"text/plain")
		content = "I am request#{}\n".format(self.numberRequests)
		return content.encode("ascii")

resource = Counter()

endpoint = endpoints.serverFromString(reactor, "tcp:8080")
endpoint.listen(server.Site(resource))
reactor.run()
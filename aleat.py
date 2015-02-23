import webapp
import random
import socket

class otroServidor(webapp.webApp):
		def process(self, parsedRequest):
				return("200 OK", "<html>""<body><h1>" + "Pagina aleatoria</h1>" +  "<a href='" + str(random.randrange(999999)) + "'>Dame otra</a>" + "</body></html>")

if __name__ == "__main__":
		serv = otroServidor(socket.gethostname(), 1234)

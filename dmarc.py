import gzip
import logging
import lxml
from StringIO import StringIO

from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
import webapp2


class DmarcHandler(InboundMailHandler):
    """Simple handler for DMARC emails"""
    def receive(self, email):
        logging.info("Received a message from: <%s>, Subject: %s", email.sender, email.subject)

        if len(email.attachments) > 0:
            attachment = email.attachments[0]
            logging.info("attachments: %s", attachment.filename)
            data = attachment.payload.decode()
            unzipped = gzip.GzipFile(fileobj=StringIO(data)).read()
            logging.info("Content: %s", unzipped)
            


app = webapp2.WSGIApplication([DmarcHandler.mapping()], debug=True)
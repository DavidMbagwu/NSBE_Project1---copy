import smtplib
import ssl
from django.core.mail.backends.smtp import EmailBackend as SMTPBackend

class StageEmailBackend(SMTPBackend):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_connection(self, *args, **kwargs):
        connection = super().get_connection(*args, **kwargs)
        # Configure SSL if necessary
        if self.ssl_certfile or self.ssl_keyfile:
            ssl_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)
            ssl_context.load_cert_chain(self.ssl_certfile, self.ssl_keyfile)
            connection.ssl_context = ssl_context
        else:
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            connection.ssl_context = ssl_context
        return connection

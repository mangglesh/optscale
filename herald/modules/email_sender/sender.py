import os
import logging
import smtplib
import ssl

from herald_server.utils import (
    is_valid_port,
    is_email_format
)


LOG = logging.getLogger(__name__)


def send_email(message, config_client=None):
    if config_client is not None:
        smtp_params = config_client.smtp_params()
        LOG.info(smtp_params)
        if smtp_params is not None:
            if _is_valid_smtp_params(smtp_params):
                server, port, email, password,from_email = smtp_params
                _send_email_to_user_smtp(server, port, email, password, message, from_email)
                return
            else:
                LOG.warning("User SMTP parameters are not valid")
    _send_email_from_default_service(message)


def _is_valid_smtp_params(params):
    if params is None:
        return False
    server, port, email, password, from_email = params
    for value in (server, email, password):
        if value is None:
            LOG.error("Server/email/password should not be none")
            return False
    if not isinstance(server, str):
        LOG.error("server %s is not instance " & (server))
        return False
    if not is_email_format(from_email):
        LOG.error("email %s is  not valid " % (from_email))
        return False
    if is_valid_port(port):
        LOG.error("port %s is not valid " % (port))
    return True


def _send_email_to_user_smtp(server, port, email, password, message, from_email):
    context = ssl._create_unverified_context()
    try:
        with smtplib.SMTP_SSL(server, port, context=context) as smtp_server:
            smtp_server.login(email, password)
            smtp_server.sendmail(from_email, message.get("To"), message.as_string())
    except Exception as e:
        LOG.error("Could not send mail using server %s and port %s with email %s. "
                  "Error %s" % (server, port, email, str(e)))


def _send_email_from_default_service(message):
    sendmail_location = "/usr/sbin/sendmail"
    p = os.popen("%s -t -i" % sendmail_location, "w")
    p.write(message.as_string())
    p.close()

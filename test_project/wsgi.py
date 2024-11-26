import logging
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")

logger = logging.getLogger(__name__)

application = get_wsgi_application()

# from _socket import gaierror
#
# logger.debug("initialising remote debug")
# host_debug_port = 45769
# try:
#     import pydevd_pycharm
#
#     pydevd_pycharm.settrace(
#         "host.docker.internal",
#         port=host_debug_port,
#         stdoutToServer=True,
#         stderrToServer=True,
#         suspend=False,
#     )
#     logger.info(
#         "pydevd_pycharm daemon attached to host debug port: %s", host_debug_port
#     )
# except (ConnectionRefusedError, gaierror):
#     logger.warning(
#         "pydevd_pycharm daemon failed to connect to host debug port: %s - ignoring ...",
#         host_debug_port,
#     )

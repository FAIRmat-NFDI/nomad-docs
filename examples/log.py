from nomad.logtransfer import transfer_logs
from nomad.utils import get_logger

get_logger(__name__).info('logger initialized')
transfer_logs()

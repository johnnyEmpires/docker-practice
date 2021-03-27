import time
from basiclog import module_logger

log = module_logger(__name__)

log.info("App running within docker")

for i in reversed(range(1, 6)):
    log.info(f'end of script in...{i}')
    time.sleep(1)

log.info('sample app in docker terminated.')
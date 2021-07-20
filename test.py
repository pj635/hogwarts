import logging
import pytest

logging.basicConfig(level = logging.DEBUG, format = '%(filename)s:%(lineno)d[%(levelname)s] %(message)s')


# logging.basicConfig(level=logging.DEBUG,
#                     format="%(asctime)s %(name)s %(levelname)s %(message)s")

def test():
    logging.debug("msg1")
    logging.info("msg2")
    logging.warning("msg3")
    logging.error("msg4")
    logging.critical("msg5")

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_tag.py'])
    # pytest.main(['-v', '-s', 'test.py', '--log-cli-level=INFO'])

import unittest
import os
import signal
import subprocess
import time
from gradescope_utils.autograder_utils.decorators import weight, visibility, number

class test_uthread(unittest.TestCase):
    @weight(10)
    @number("4.1")
    def test1(self):
        p = subprocess.Popen(['./test1'], stdout=subprocess.PIPE)
        time.sleep(3)
        os.killpg(os.getpgid(p.pid), signal.SIGTERM)
        out, err = p.communicate()

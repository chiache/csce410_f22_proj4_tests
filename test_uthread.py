import unittest
import os
import signal
import subprocess
import time
from gradescope_utils.autograder_utils.decorators import weight, visibility, number

class test_uthread(unittest.TestCase):
    @weight(20)
    @number("4.1")
    def test1(self):
        p = subprocess.Popen(['./test1'], stdout=subprocess.PIPE)
        time.sleep(3)
        p.kill()
        out, _ = p.communicate()

    @weight(15)
    @number("4.2")
    def test1(self):
        p = subprocess.Popen(['./test2'], stdout=subprocess.PIPE)
        time.sleep(3)
        p.kill()
        out, _ = p.communicate()

    @weight(20)
    @number("4.3")
    def test1(self):
        p = subprocess.Popen(['./test3'], stdout=subprocess.PIPE)
        time.sleep(3)
        p.kill()
        out, _ = p.communicate()

    @weight(10)
    @number("4.3")
    def test1(self):
        p = subprocess.Popen(['./test6'], stdout=subprocess.PIPE)
        time.sleep(3)
        p.kill()
        out, _ = p.communicate()


    @weight(10)
    @number("4.4.1")
    def test1(self):
        p = subprocess.Popen(['./test4'], stdout=subprocess.PIPE)
        time.sleep(3)
        p.kill()
        out, _ = p.communicate()

    @weight(10)
    @number("4.4.1")
    def test1(self):
        p = subprocess.Popen(['./test5'], stdout=subprocess.PIPE)
        time.sleep(3)
        p.kill()
        out, _ = p.communicate()

    @weight(15)
    @number("4.5")
    def test1(self):
        p = subprocess.Popen(['./test7'], stdout=subprocess.PIPE)
        time.sleep(3)
        p.kill()
        out, _ = p.communicate()



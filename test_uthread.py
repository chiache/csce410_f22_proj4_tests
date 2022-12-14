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
        p = subprocess.Popen(['./test1'], stderr=subprocess.PIPE)
        time.sleep(6)
        p.kill()
        _, out = p.communicate()
        print "output:"
        print out
        t1_count = 0
        t2_count = 0
        for l in out.splitlines():
            if "thread 1" in l: t1_count += 1
            if "thread 2" in l: t2_count += 1
        print "thread 1 appears", t1_count, "times"
        print "thread 2 appears", t2_count, "times"
        self.assertTrue(t1_count == 10, "The output does not have 10 outputs from thread 1")
        self.assertTrue(t2_count == 10, "The output does not have 10 outputs from thread 2")


    @weight(15)
    @number("4.2.1")
    def test2(self):
        p = subprocess.Popen(['./test2'], stderr=subprocess.PIPE)
        time.sleep(6)
        p.kill()
        _, out = p.communicate()
        print "output:"
        print out
        t1_count = 0
        t2_count = 0
        for l in out.splitlines():
            if "thread 1" in l: t1_count += 1
            if "thread 2" in l: t2_count += 1
        print "thread 1 appears", t1_count, "times"
        print "thread 2 appears", t2_count, "times"
        self.assertTrue(t1_count == 10, "The output does not have 10 outputs from thread 1")
        self.assertTrue(t2_count == 10, "The output does not have 10 outputs from thread 2")


    @weight(20)
    @number("4.2.2")
    def test3(self):
        p = subprocess.Popen(['./test3'], stderr=subprocess.PIPE)
        time.sleep(6)
        p.kill()
        _, out = p.communicate()
        print "output:"
        print out
        t1_count = 0
        t2_count = 0
        for l in out.splitlines():
            if "thread 1" in l: t1_count += 1
            if "thread 2" in l: t2_count += 1
        print "thread 1 appears", t1_count, "times"
        print "thread 2 appears", t2_count, "times"
        self.assertTrue(t1_count == 10, "The output does not have 10 outputs from thread 1")
        self.assertTrue(t2_count == 10, "The output does not have 10 outputs from thread 2")


    @weight(10)
    @number("4.2.3")
    def test6(self):
        p = subprocess.Popen(['./test6'], stderr=subprocess.PIPE)
        time.sleep(6)
        p.kill()
        _, out = p.communicate()
        print "output:"
        print out
        stack_counts = dict()
        for l in out.splitlines():
            if "stack" in l:
                stack_addr = int(l.split()[4], base=16) / 4096 * 4096
                if stack_addr in stack_counts:
                    stack_counts[stack_addr] += 1
                else:
                    stack_counts[stack_addr] = 1
        all_stack_addrs = stack_counts.keys()
        for addr in all_stack_addrs:
            print "stack %08x appears %d times" % (addr, stack_counts[addr])
        self.assertTrue(len(all_stack_addrs) == 2, "Exactly two stacks are used in uthreads")
        if len(all_stack_addrs) == 2:
            self.assertTrue(stack_counts[all_stack_addrs[0]] == 11,
                            "The output does not have 11 outputs from the 1st stack")
            self.assertTrue(stack_counts[all_stack_addrs[1]] == 11,
                            "The output does not have 11 outputs from the 2nd stack")


    @weight(20)
    @number("4.2.4")
    def test5(self):
        p = subprocess.Popen(['./test5'], stderr=subprocess.PIPE)
        time.sleep(6)
        p.kill()
        _, out = p.communicate()
        print "output:"
        print out
        t1_count = 0
        t2_count = 0
        for l in out.splitlines():
            if "thread 1 (count = 9)" in l:
                t1_count += 1
            if "thread 2 (count = 9)" in l:
                t2_count += 1
        self.assertTrue(t1_count == 1, "The output does not have count = 9 from thread 1")
        self.assertTrue(t2_count == 1, "The output does not have count = 9 from thread 2")


    @weight(15)
    @number("4.2.5")
    def test7(self):
        p = subprocess.Popen(['./test7'], stderr=subprocess.PIPE)
        time.sleep(6)
        p.kill()
        _, out = p.communicate()
        print "output:"
        print out
        thread_order = []
        for l in out.splitlines():
            if "thread 1" in l: thread_order.append("1")
            if "thread 2" in l: thread_order.append("2")
            if "thread 3" in l: thread_order.append("3")
        self.assertListEqual(thread_order[0:1], ["1"], "The first thread order should be 1")
        self.assertListEqual(thread_order[-5:], ["3", "3", "3", "3", "3"], "The last 5 thread orders should all be thread 3")

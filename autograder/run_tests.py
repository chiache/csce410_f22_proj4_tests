import unittest
import os
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('/autograder/submission/csce410_f22_proj4_tests', pattern='test_uthread.py')

    with open('/autograder/results/results.json', 'w') as f:
        print "Run with -fPIC..."
        runner = JSONTestRunner(visibility='visible', stream=f)
        runner.run(suite)
        printf "Score with -fPIC:", runner.json_data['score']

    suite_nopic = unittest.defaultTestLoader.discover('/autograder/submission/csce410_f22_proj4_tests', pattern='test_uthread_nopic.py')

    with open('/autograder/results/results-nopic.json', 'w') as f:
        print "Run without -fPIC..."
        runner_nopic = JSONTestRunner(visibility='visible', stream=f)
        runner_nopic.run(suite_nopic)
        printf "Score without -fPIC:", runner_nopic.json_data['score']

    if runner_nopic.json_data['score'] > runner.json_data['score']:
        os.replace('/autograder/results/results-nopic.json', '/autograder/results/result.json')



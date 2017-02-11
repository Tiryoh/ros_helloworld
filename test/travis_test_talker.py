#!/usr/bin/env python
import rospy, unittest, rostest
import rosnode
import time

class TalkerTest(unittest.TestCase):
    def test_node_exist(self):
        nodes = rosnode.get_node_names()
        self.assertIn('/talker', nodes, "node does not exist")

if __name__ == '__main__':
    time.sleep(5)
    rospy.init_node('travis_test_talker')
    rostest.rosrun('ros_helloworld', 'travis_test_talker', TalkerTest)


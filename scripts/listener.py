#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s",data.data)

def listener():
    rospy.init_node('listener', anonymouse=True)
    rospy.subscriber("chatter", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()


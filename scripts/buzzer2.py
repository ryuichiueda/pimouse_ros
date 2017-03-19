#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16

def recv_buzzer(data):
    rospy.loginfo(type(data))
    rospy.loginfo(data.data)

if __name__ == '__main__':
    rospy.init_node('buzzer')
    rospy.Subscriber("buzzer", UInt16, recv_buzzer)
    rospy.spin()

# Copyright 2016 Ryuichi Ueda
# Released under the BSD License.
# To make line numbers be identical with the book, this statement is written here. Don't move it to the header.

#!/usr/bin/env python

import rospy 
from std_msgs.msg import Int16 
from edx_week1.msg import twoints


def sum(msg):  
    global sum_msg
    sum_msg = msg.a+msg.b
    rospy.loginfo(str(msg.a)+ " + " +str(msg.b) + " = " + str(sum_msg))
    pub.publish(sum_msg)

def listener():
    global pub
    rospy.init_node("week1_solution",anonymous=True)
    sub = rospy.Subscriber('/two_ints',twoints,sum)
    pub = rospy.Publisher('sum',Int16,queue_size=1)    
    rospy.spin()

if __name__ == "__main__":
    listener()
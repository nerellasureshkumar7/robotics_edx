#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Int16
from edx_week1.msg import twoints

def talker():
    rospy.init_node('week1_question',anonymous=True)
    pub =rospy.Publisher('two_ints',twoints,queue_size=1)
    rate =rospy.Rate (1)
    random.seed()
    while not rospy.is_shutdown():

        msg= twoints()
        msg.a = random.randint(1,20)
        msg.b = random.randint(1,20)
        rospy.loginfo("a="+ str(msg.a)+ ","+ "b=" +str(msg.b))
        pub.publish(msg)
        rate.sleep()




if __name__ == "__main__":

    try:
        talker()

    except rospy.ROSInterruptException:
        pass        

import rospy
from sensor_msgs.msg import Image
from darknet_ros_msgs.msg import BoundingBoxes, BoundingBox
from std_msgs.msg import Header
from std_msgs.msg import String
from geometry_msgs.msg import Twist


def callback(data):
    
    #print(str(data.bounding_boxes[0].Class))
    for box in data.bounding_boxes:
        #print(str(box.Class))
        #print(str(box.probability))
        if(box.Class=="car" and box.probability>0.7):
            print("car")
        if(box.Class=="truck" and box.probability>0.7):
            print("truck")
            twist.linear.x = 0.0
            twist.angular.z = 200.0
            cmd_vel.publish(twist)
    


  
        
if __name__ == '__main__':
    try :
        rospy.init_node('levha_algilayici_sub')
        rospy.Subscriber('/darknet_ros/bounding_boxes', BoundingBoxes , callback)
        cmd_vel = rospy.Publisher('/Diff_Drive/diff_drive_controller/cmd_vel',Twist,queue_size=1)
        twist = Twist()
        
        
        rospy.spin()
        
        #talker()
    except rospy.ROSInterruptException:
        pass

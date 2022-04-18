import rospy
from sensor_msgs.msg import Image
from darknet_ros_msgs.msg import BoundingBoxes, BoundingBox
from robotaksi_gazebo.msg import Hareket
from std_msgs.msg import Float64
from std_msgs.msg import String



def callback(data):
    
    for box in data.bounding_boxes:
        
        if(box.Class=="truck" and box.probability>0.40):
            print("truck")
            cmd_vel.publish(mesaj_hiz)
            

        if(box.Class=="stop sign" and box.probability>0.90):
            cmd_vel.publish(mesaj_fren)
        
        
if __name__ == '__main__':
    try :
        rospy.init_node('levha_algilayici_sub')
        rospy.Subscriber('/darknet_ros/bounding_boxes', BoundingBoxes , callback)
        cmd_vel = rospy.Publisher('/Path_Planning',Hareket,queue_size=1)
        
        mesaj_hiz = Hareket()
        mesaj_hiz.data = 0.1

        mesaj_donus = Hareket()
        mesaj_donus.data = 5.0

        mesaj_fren = Hareket()
        mesaj_fren.data = 10

        
        
        
        rospy.spin()
        
       
    except rospy.ROSInterruptException:
        pass
import logging
import rospy
from std_msgs.msg import String

logger = logging.getLogger("logger")

def logger_callback(data):
    rospy.loginfo("/log: %s", data.data)
    logger.info(data.data)

def logger_node():
    rospy.init_node("logger_node", anonymous=True)
    rospy.Subscriber("/log", String, logger_callback, queue_size=10)
    rospy.spin()

if __name__ == "__main__":
    logger_node()


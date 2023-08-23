import rospy
from std_msgs.msg import String

from fastapi import FastAPI
from pydantic import BaseModel

import uvicorn
import multiprocessing

app = FastAPI()

class LogItem(BaseModel):
    data: str

@app.post("/info")
async def process(data: LogItem):
    rospy.init_node("listener_node", anonymous=True)
    pub = rospy.Publisher("/info", String, queue_size=10)
    pub.publish(data.data)

def listener_callback(data):
    rospy.loginfo("/info: %s", data.data)
    pub = rospy.Publisher("/log", String, queue_size=10)
    pub.publish(data.data)

def listener_node():
    rospy.init_node("listener_node", anonymous=True)
    rospy.Subscriber("/info", String, listener_callback)
    rospy.spin()

if __name__ == "__main__":
    listener_process = multiprocessing.Process(target=listener_node)
    listener_process.start()
    uvicorn.run(app, host="0.0.0.0", port=8001)
    listener_process.join()



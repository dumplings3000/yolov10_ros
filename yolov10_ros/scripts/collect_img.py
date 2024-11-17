#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import os

class ImageSaver:
    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/image_raw", Image, self.callback)
        self.image_count = 0
        self.save_path = "/path/to/save/images"  # 替換為你要儲存圖片的路徑
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            rospy.logerr("CvBridge Error: {0}".format(e))
            return

        image_name = os.path.join(self.save_path, f"image_{self.image_count:04d}.jpg")
        cv2.imwrite(image_name, cv_image)
        rospy.loginfo(f"Saved image: {image_name}")
        self.image_count += 1

if __name__ == '__main__':
    rospy.init_node('image_saver_node', anonymous=True)
    image_saver = ImageSaver()
    rospy.spin()
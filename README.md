# Yolov8_ros

This package provides a ROS wrapper for [PyTorch-YOLOv10](https://github.com/ultralytics/ultralytics) based on PyTorch-YOLOv10. The package has been tested with Ubuntu 20.04.

# develop environment：
- Ubuntu 20.04
- ROS Noetic
- Python>=3.7.0 environment, including PyTorch>=1.7

# Prerequisites:
```
pip install ultralytics
```

## Installation

```
cd /your/catkin_ws/src
git clone https://github.com/dumplings3000/yolov10_ros.git
cd ..
catkin_make

```

## Basic Usage

1. First, make sure to put your weights in the [weights](https://github.com/qq44642754a/Yolov8_ros/tree/master/yolov8_ros/weights) folder. 
2.  The default settings (using `yolov8s.pt`) in the `launch/yolo_v8.launch` file should work, all you should have to do is change the image topic you would like to subscribe to:

```
roslaunch yolov10_ros yolo_v8.launch
```


### Node parameters

* **`sub_topic`** 

    Subscribed camera topic.

* **`weights_path`** 

    Path to weights file.

* **`pub_topic`** 

    Published topic with the detected bounding boxes.
    
* **`confidence`** 

    Confidence threshold for detected objects.
    



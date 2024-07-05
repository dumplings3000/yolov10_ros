# Yolov10_ros

This package provides a ROS wrapper for [ultralytics](https://github.com/ultralytics/ultralytics) based on PyTorch-YOLOv10. The package has been tested with Ubuntu 20.04.

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
cd yolov10_ros
git submodule update --init --recursive
cd ..
catkin_make

```

## Basic Usage
```
roslaunch yolov10_ros yolo_v10.launch
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
    



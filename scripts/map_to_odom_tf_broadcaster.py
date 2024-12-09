#!/usr/bin/env python3
import rospy
import tf2_ros
import geometry_msgs.msg
from nav_msgs.msg import Odometry

def odom_callback(msg):
    br = tf2_ros.TransformBroadcaster()
    transform = geometry_msgs.msg.TransformStamped()

    transform.header.stamp = rospy.Time.now()
    transform.header.frame_id = "map"
    transform.child_frame_id = "odom"
    transform.transform.translation.x = msg.pose.pose.position.x
    transform.transform.translation.y = msg.pose.pose.position.y
    transform.transform.translation.z = msg.pose.pose.position.z
    transform.transform.rotation = msg.pose.pose.orientation

    br.sendTransform(transform)

def publish_tf():
    rospy.init_node('static_tf_pub')
    br = tf2_ros.StaticTransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()
    
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "map"
    t.child_frame_id = "base_link"
    t.transform.translation.x = 0.0
    t.transform.translation.y = 0.5  # 调整y方向的差异
    t.transform.translation.z = 0.0
    t.transform.rotation.x = 0.0
    t.transform.rotation.y = 0.0
    t.transform.rotation.z = 0.0
    t.transform.rotation.w = 1.0
    
    br.sendTransform(t)
    rospy.spin()

def listener():
    rospy.init_node('map_to_odom_broadcaster')
    rospy.Subscriber('/aft_mapped_to_init', Odometry, odom_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
    publish_tf()
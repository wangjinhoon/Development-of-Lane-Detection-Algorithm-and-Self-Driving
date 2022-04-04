;; Auto-generated. Do not edit!


(when (boundp 'xycar_motor::xycar_motor)
  (if (not (find-package "XYCAR_MOTOR"))
    (make-package "XYCAR_MOTOR"))
  (shadow 'xycar_motor (find-package "XYCAR_MOTOR")))
(unless (find-package "XYCAR_MOTOR::XYCAR_MOTOR")
  (make-package "XYCAR_MOTOR::XYCAR_MOTOR"))

(in-package "ROS")
;;//! \htmlinclude xycar_motor.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass xycar_motor::xycar_motor
  :super ros::object
  :slots (_header _angle _speed ))

(defmethod xycar_motor::xycar_motor
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:angle __angle) 0)
    ((:speed __speed) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _angle (round __angle))
   (setq _speed (round __speed))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:angle
   (&optional __angle)
   (if __angle (setq _angle __angle)) _angle)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int32 _angle
    4
    ;; int32 _speed
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int32 _angle
       (write-long _angle s)
     ;; int32 _speed
       (write-long _speed s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int32 _angle
     (setq _angle (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _speed
     (setq _speed (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get xycar_motor::xycar_motor :md5sum-) "776d1e41053a9ee231920fdd113d2d0a")
(setf (get xycar_motor::xycar_motor :datatype-) "xycar_motor/xycar_motor")
(setf (get xycar_motor::xycar_motor :definition-)
      "Header header
int32 angle
int32 speed


================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

")



(provide :xycar_motor/xycar_motor "776d1e41053a9ee231920fdd113d2d0a")



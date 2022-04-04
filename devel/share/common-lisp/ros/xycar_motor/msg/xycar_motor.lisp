; Auto-generated. Do not edit!


(cl:in-package xycar_motor-msg)


;//! \htmlinclude xycar_motor.msg.html

(cl:defclass <xycar_motor> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (angle
    :reader angle
    :initarg :angle
    :type cl:integer
    :initform 0)
   (speed
    :reader speed
    :initarg :speed
    :type cl:integer
    :initform 0))
)

(cl:defclass xycar_motor (<xycar_motor>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <xycar_motor>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'xycar_motor)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name xycar_motor-msg:<xycar_motor> is deprecated: use xycar_motor-msg:xycar_motor instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <xycar_motor>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xycar_motor-msg:header-val is deprecated.  Use xycar_motor-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <xycar_motor>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xycar_motor-msg:angle-val is deprecated.  Use xycar_motor-msg:angle instead.")
  (angle m))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <xycar_motor>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xycar_motor-msg:speed-val is deprecated.  Use xycar_motor-msg:speed instead.")
  (speed m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <xycar_motor>) ostream)
  "Serializes a message object of type '<xycar_motor>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'angle)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'speed)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <xycar_motor>) istream)
  "Deserializes a message object of type '<xycar_motor>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'angle) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'speed) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<xycar_motor>)))
  "Returns string type for a message object of type '<xycar_motor>"
  "xycar_motor/xycar_motor")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'xycar_motor)))
  "Returns string type for a message object of type 'xycar_motor"
  "xycar_motor/xycar_motor")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<xycar_motor>)))
  "Returns md5sum for a message object of type '<xycar_motor>"
  "776d1e41053a9ee231920fdd113d2d0a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'xycar_motor)))
  "Returns md5sum for a message object of type 'xycar_motor"
  "776d1e41053a9ee231920fdd113d2d0a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<xycar_motor>)))
  "Returns full string definition for message of type '<xycar_motor>"
  (cl:format cl:nil "Header header~%int32 angle~%int32 speed~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'xycar_motor)))
  "Returns full string definition for message of type 'xycar_motor"
  (cl:format cl:nil "Header header~%int32 angle~%int32 speed~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <xycar_motor>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <xycar_motor>))
  "Converts a ROS message object to a list"
  (cl:list 'xycar_motor
    (cl:cons ':header (header msg))
    (cl:cons ':angle (angle msg))
    (cl:cons ':speed (speed msg))
))


(cl:in-package :asdf)

(defsystem "xycar_motor-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "xycar_motor" :depends-on ("_package_xycar_motor"))
    (:file "_package_xycar_motor" :depends-on ("_package"))
  ))
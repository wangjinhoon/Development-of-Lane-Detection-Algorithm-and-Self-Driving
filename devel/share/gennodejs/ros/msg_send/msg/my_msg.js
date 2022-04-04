// Auto-generated. Do not edit!

// (in-package msg_send.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class my_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.first_name = null;
      this.last_name = null;
      this.age = null;
      this.score = null;
      this.phone_number = null;
      this.id_number = null;
      this.angle = null;
      this.speed = null;
    }
    else {
      if (initObj.hasOwnProperty('first_name')) {
        this.first_name = initObj.first_name
      }
      else {
        this.first_name = '';
      }
      if (initObj.hasOwnProperty('last_name')) {
        this.last_name = initObj.last_name
      }
      else {
        this.last_name = '';
      }
      if (initObj.hasOwnProperty('age')) {
        this.age = initObj.age
      }
      else {
        this.age = 0;
      }
      if (initObj.hasOwnProperty('score')) {
        this.score = initObj.score
      }
      else {
        this.score = 0;
      }
      if (initObj.hasOwnProperty('phone_number')) {
        this.phone_number = initObj.phone_number
      }
      else {
        this.phone_number = '';
      }
      if (initObj.hasOwnProperty('id_number')) {
        this.id_number = initObj.id_number
      }
      else {
        this.id_number = 0;
      }
      if (initObj.hasOwnProperty('angle')) {
        this.angle = initObj.angle
      }
      else {
        this.angle = 0;
      }
      if (initObj.hasOwnProperty('speed')) {
        this.speed = initObj.speed
      }
      else {
        this.speed = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type my_msg
    // Serialize message field [first_name]
    bufferOffset = _serializer.string(obj.first_name, buffer, bufferOffset);
    // Serialize message field [last_name]
    bufferOffset = _serializer.string(obj.last_name, buffer, bufferOffset);
    // Serialize message field [age]
    bufferOffset = _serializer.int32(obj.age, buffer, bufferOffset);
    // Serialize message field [score]
    bufferOffset = _serializer.int32(obj.score, buffer, bufferOffset);
    // Serialize message field [phone_number]
    bufferOffset = _serializer.string(obj.phone_number, buffer, bufferOffset);
    // Serialize message field [id_number]
    bufferOffset = _serializer.int32(obj.id_number, buffer, bufferOffset);
    // Serialize message field [angle]
    bufferOffset = _serializer.int32(obj.angle, buffer, bufferOffset);
    // Serialize message field [speed]
    bufferOffset = _serializer.int32(obj.speed, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type my_msg
    let len;
    let data = new my_msg(null);
    // Deserialize message field [first_name]
    data.first_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [last_name]
    data.last_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [age]
    data.age = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [score]
    data.score = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [phone_number]
    data.phone_number = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [id_number]
    data.id_number = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [angle]
    data.angle = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [speed]
    data.speed = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.first_name.length;
    length += object.last_name.length;
    length += object.phone_number.length;
    return length + 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'msg_send/my_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '009b3e6baca845acfcb349a1568f69dc';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string first_name
    string last_name
    int32 age
    int32 score
    string phone_number
    int32 id_number
    int32 angle
    int32 speed
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new my_msg(null);
    if (msg.first_name !== undefined) {
      resolved.first_name = msg.first_name;
    }
    else {
      resolved.first_name = ''
    }

    if (msg.last_name !== undefined) {
      resolved.last_name = msg.last_name;
    }
    else {
      resolved.last_name = ''
    }

    if (msg.age !== undefined) {
      resolved.age = msg.age;
    }
    else {
      resolved.age = 0
    }

    if (msg.score !== undefined) {
      resolved.score = msg.score;
    }
    else {
      resolved.score = 0
    }

    if (msg.phone_number !== undefined) {
      resolved.phone_number = msg.phone_number;
    }
    else {
      resolved.phone_number = ''
    }

    if (msg.id_number !== undefined) {
      resolved.id_number = msg.id_number;
    }
    else {
      resolved.id_number = 0
    }

    if (msg.angle !== undefined) {
      resolved.angle = msg.angle;
    }
    else {
      resolved.angle = 0
    }

    if (msg.speed !== undefined) {
      resolved.speed = msg.speed;
    }
    else {
      resolved.speed = 0
    }

    return resolved;
    }
};

module.exports = my_msg;

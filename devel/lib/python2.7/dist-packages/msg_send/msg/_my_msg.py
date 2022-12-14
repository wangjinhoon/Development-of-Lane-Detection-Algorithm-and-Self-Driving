# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from msg_send/my_msg.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class my_msg(genpy.Message):
  _md5sum = "009b3e6baca845acfcb349a1568f69dc"
  _type = "msg_send/my_msg"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """string first_name
string last_name
int32 age
int32 score
string phone_number
int32 id_number
int32 angle
int32 speed
"""
  __slots__ = ['first_name','last_name','age','score','phone_number','id_number','angle','speed']
  _slot_types = ['string','string','int32','int32','string','int32','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       first_name,last_name,age,score,phone_number,id_number,angle,speed

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(my_msg, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.first_name is None:
        self.first_name = ''
      if self.last_name is None:
        self.last_name = ''
      if self.age is None:
        self.age = 0
      if self.score is None:
        self.score = 0
      if self.phone_number is None:
        self.phone_number = ''
      if self.id_number is None:
        self.id_number = 0
      if self.angle is None:
        self.angle = 0
      if self.speed is None:
        self.speed = 0
    else:
      self.first_name = ''
      self.last_name = ''
      self.age = 0
      self.score = 0
      self.phone_number = ''
      self.id_number = 0
      self.angle = 0
      self.speed = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.first_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.last_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2i().pack(_x.age, _x.score))
      _x = self.phone_number
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3i().pack(_x.id_number, _x.angle, _x.speed))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.first_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.first_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.last_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.last_name = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.age, _x.score,) = _get_struct_2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.phone_number = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.phone_number = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.id_number, _x.angle, _x.speed,) = _get_struct_3i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.first_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.last_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2i().pack(_x.age, _x.score))
      _x = self.phone_number
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3i().pack(_x.id_number, _x.angle, _x.speed))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.first_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.first_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.last_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.last_name = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.age, _x.score,) = _get_struct_2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.phone_number = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.phone_number = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.id_number, _x.angle, _x.speed,) = _get_struct_3i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2i = None
def _get_struct_2i():
    global _struct_2i
    if _struct_2i is None:
        _struct_2i = struct.Struct("<2i")
    return _struct_2i
_struct_3i = None
def _get_struct_3i():
    global _struct_3i
    if _struct_3i is None:
        _struct_3i = struct.Struct("<3i")
    return _struct_3i

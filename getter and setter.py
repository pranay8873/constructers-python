class GetterSetter:
    def __init__(self, value):
        self._mlvalue = 10 * value  # Use private attribute
        self._mllvalue = value      # Initialize the private attribute for mllvalue
    
    @property
    def mlvalue(self):
        return self._mlvalue
    
    @mlvalue.setter
    def mlvalue(self, value):
        self._mlvalue = value
    
    @property
    def mllvalue(self):
        return self._mllvalue  # Return the private attribute, not self.mllvalue
    
    @mllvalue.setter
    def mllvalue(self, value):
        self._mllvalue = value  # Set the private attribute

# Demo the getter and setter functionality
pk = GetterSetter(20)
print(pk.mlvalue)  # Should print 200
pk.mllvalue = 20
print(pk.mllvalue)  # Should print 20
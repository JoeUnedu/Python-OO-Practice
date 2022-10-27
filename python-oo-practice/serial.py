"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    # let us initialize start in a  function
    def __init__(self, start):
      

        # start must be an integer 
        # start must be greater than zero
        # initialize start now to a value
        # ininstance returns true if start is an intiger
        if (isinstance(start, int)):
            if (start > 0):
                self.start = start
                # self.next_serial_num is set to None
                # self.next_num is used to call reset function to a default value 
            
                self.next_serial_num = None
                self.reset()
                # if serial is not greater than zero
                # it will raise an error
                # raise () is used to raise an exception error
                #  ValueError () needed here
                # used when there is a wrong value in a specified data type
            else:
                raise ValueError(
                    f" This serial number must be greater than zero.")
        else:
            raise ValueError(f"serial '{start}' not real integer.")
        # now let return function for serial generators
      # this () returns serial generator and for the  next serial numbers
    def __repr__(self):
        return f"<SerialGenerator ={self.start} and  next is ={self.next_serial_num + 1}>"
   # This function returns the next serial number
    def generate_self(self):
        self.next_serial_num = self.next_serial_num + 1
        return self.next_serial_num
     # reset the  serial numbers
    def reset(self):
        self.next_serial_num = self.start - 1


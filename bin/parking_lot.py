class car():
  # Intiate Car Instance
  def __init__(self, reg_no, color):
    self.color = color
    self.reg_no = reg_no

class parking_allocation():
  # Intiate parking lot size.
  current_size = 0
  available_slot = 0
  park_list = list()
  def __init__(self, max_size):
    self.max_size = max_size
  
  def is_slot_number_valid(self, slot_no):
    # Is parking slot number provided valid.
    if slot_no > self.max_size or slot_no <= 0:
      return False
    return True

  def park(self, reg_no, color):
    # Check if the max size is reached.
    assert self.current_size <= self.max_size, "Sorry, parking lot is full"
    # Check if the Max size is zero.
    assert self.max_size <= 0, "Sorry, Parking Slot is not having minimum required space"
    self.allocate(reg_no, color)
  
  def allocate(self, reg_no, color):
    # Allocate a parking slot to car.
    car_obj = car(reg_no=reg_no, color=color)
    self.park_list[self.available_slot] = car_obj
  
  def remove_car(self, slot_no):
    # Remove car from parking lot.
    if self.is_slot_number_valid(slot_no) :
      print("No Car found for this slot number.")
    self.park_list.remove(slot_no)
    print("Slot number %s is free" % slot_no)
  
  def get_car(self, slot_no):
    # Get car by slot number.
    if self.is_slot_number_valid(slot_no):
      return self.park_list[slot_no]
    raise Exception("Invalid Slot Number")

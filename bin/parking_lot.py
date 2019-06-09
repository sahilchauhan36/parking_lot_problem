from library.notification_enums import NotificationMessage as message
import sys
import array


class Car:
    """
    This Class Represents Car as a Granular Real World Entity.
    """
    # Initiate Car Instance
    def __init__(self, reg_no, color):
        self.color = color
        self.reg_no = reg_no


class ParkingAllocation:
    """
    The Class Represents Parking Allocation System
    """
    # Intiate Current Size of the Parking Slot, Available Slot
    current_size = 0
    available_slot = 1
    park_list = dict()

    def __init__(self, max_size):
        # Intiate parking lot size
        self.max_size = max_size
        print ("Created a parking lot with %d slots" % max_size)

    def is_slot_number_valid(self, slot_no):
        # Is parking slot number provided valid.
        if int(slot_no) > self.max_size or int(slot_no) <= 0:
            return False
        return True

    def is_parking_lot_valid(self):
        # Is parking slot number provided valid.
        if self.max_size <= 0:
            return False
        return True

    def set_available_slot(self):
        for i in range(1,self.max_size+1):
            if self.park_list.get(i) is None:
                self.available_slot = i
                return
        self.available_slot = None

    def park(self, reg_no, color):

        # Check if Parking Lot is full
        if self.current_size >= self.max_size:
            print(message.FULL_PARKING)
            return

        # Check if the Max size is zero.
        if not self.is_parking_lot_valid():
            print(message.INVALID_PARKING_LOT)
            return

        self.allocate(reg_no, color)

    def allocate(self, reg_no, color):
        """
        Allocate a parking slot to car.

        :param reg_no: Registration Number of the Car
        :type reg_no: str
        :param color: Color of the Car
        :type color: str
        """
        car_obj = Car(reg_no=reg_no, color=color)
        self.park_list.update([(self.available_slot,car_obj)])
        print('Allocated slot number: %d' % self.available_slot)
        self.set_available_slot()
        self.current_size = self.current_size + 1

    def leave(self, slot_no):
        """
        Leave Car from Parking Lot.

        :param slot_no: Slot Number allocated to car
        :type slot_no: int
        """

        # Check if Parking Slot Number is Valid
        if not self.is_slot_number_valid(slot_no):
            print(message.INVALID_SLOT_NUMBER)
            return

        # Check if Car is available on Slot Number specified
        if self.park_list.get(slot_no) is None:
            print(message.NO_CAR_FOUND)
            return

        # Remove Car from Parking List
        self.park_list.pop(slot_no)

        # Update Current Size of Cars Parked in Parking Lot
        if self.current_size > 0:
            self.current_size = self.current_size - 1
        print("Slot number %s is free" % slot_no)

        # Update Next Available Slot
        if self.available_slot is None or slot_no < self.available_slot:
            self.available_slot = slot_no

    def get_car(self, slot_no):
        """
        Get Car by Slot number.

        :param slot_no: Slot Number allocated to car
        :type slot_no: int
        """
        # Get car by slot number.
        if self.is_slot_number_valid(slot_no):
            return self.park_list[slot_no]
        print(message.INVALID_SLOT_NUMBER)

    def status(self):
        """
        Print Status of Parking Lot
        """
        # Check if there are any cars in the Parking Lot
        if len(self.park_list) <= 0:
            print(message.EMPTY_PARKING_LOT)
            return

        print('Slot No.\tRegistration No\t\tColour')
        for slot_no, car in self.park_list.items():
            print('%d\t\t%s\t\t%s' %(slot_no,car.reg_no, car.color))

    def get_slot_by_color(self, color):
        """
        Get Slots with specified color
        :param color: Name of the color
        :type color: str
        """
        car_slots = list()
        for slot_no, car in self.park_list.items():
            if car.color == color:
                car_slots.append(slot_no)

        # Check if the number of cars are zero.
        if len(car_slots) <= 0:
            print(message.NOT_FOUND)
            return

        print(car_slots)

    def get_slot_number_from_reg_no(self, reg_no):
        """
        Get Car Slot Number from Car Registration Number.

        :param reg_no: Car registration number
        :type reg_no: str
        """
        for slot_no, car in self.park_list.items():
            if car.reg_no == reg_no:
                print(slot_no)
                return
        print(message.NOT_FOUND)

    def get_reg_no_from_color(self, color):
        """
        Get Registration number from Car Color.

        :param color: Color of the Car
        :type color: str
        """
        colored_cars = list()
        for car in self.park_list.values():
            if car.color == color:
                colored_cars.append(car.reg_no)

        # Check if the number of cars are zero.
        if len(colored_cars) <= 0:
            print(message.NOT_FOUND)
            return
        print(','.join(colored_cars))

    def exit(self):
        """
        To Exit from Parking Lot
        """
        sys.exit()

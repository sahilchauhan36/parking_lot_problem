from library.notification_enums import notification_message as message
import logging as log

class car():
    # Initiate Car Instance
    def __init__(self, reg_no, color):
        self.color = color
        self.reg_no = reg_no


class parking_allocation():
    # Intiate parking lot size.
    current_size = 0
    available_slot = 1
    park_list = list()

    def __init__(self, max_size):
        self.max_size = max_size

    def is_slot_number_valid(self, slot_no):
        # Is parking slot number provided valid.
        if slot_no > self.max_size or slot_no <= 0:
            return False
        return True

    def is_parking_lot_valid(self):
        # Is parking slot number provided valid.
        if self.max_size <= 0:
            return False
        return True

    def set_available_slot(self):
        for i in range(1,self.max_size):
            if i not in self.park_list:
                self.available_slot = i
                return
        self.available_slot = 0

    def park(self, reg_no, color):
        # Check if Parking Lot is full
        if self.current_size >= self.max_size:
            log.debug(message.FULL_PARKING)

        # Check if the Max size is zero.
        assert self.is_parking_lot_valid(), \
            log.debug(message.INVALID_PARKING_LOT)

        self.allocate(reg_no, color)

    def allocate(self, reg_no, color):
        """
        Allocate a parking slot to car.

        :param reg_no: Registration Number of the Car
        :type reg_no: str
        :param color: Color of the Car
        :type color: str
        """
        car_obj = car(reg_no=reg_no, color=color)
        self.park_list[self.available_slot] = car_obj
        log.info('Allocated slot number: %d' % self.available_slot)
        self.set_available_slot()
        self.current_size = self.current_size + 1

    def leave(self, slot_no):
        """
        Leave Car from Parking Lot.

        :param slot_no: Slot Number allocated to car
        :type slot_no: int
        """

        # Check if Parking Slot Number is Valid
        if self.is_slot_number_valid(slot_no):
            log.info(message.INVALID_SLOT_NUMBER)
            return
        # Check if Car is available on Slot Number specified
        if slot_no not in self.park_list:
            log.info(message.NO_CAR_FOUND)
            return
        # Remove Car from Parking List
        self.park_list.remove(slot_no)
        # Update Current Size of Cars Parked in Parking Lot
        if self.current_size > 0:
            self.current_size = self.current_size - 1
        log.info("Slot number %s is free" % slot_no)
        # Set Next Available Slot
        if slot_no < self.available_slot:
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
        log.debug(message.INVALID_SLOT_NUMBER)

    def status(self):
        """
        Print Status of Parking Lot
        """
        if len(self.park_list) <= 0:
            log.info(message.EMPTY_PARKING_LOT)

        log.info('Slot No.\t\tRegistration No\t\tColour')
        for car in self.park_list:
            log.info('%s\t\t%s\t\t%s' %(self.park_list.index(car),
                                        car.reg_no, car.color))

    def get_slot_by_color(self, color):
        """
        Get Slots with specified color
        :param color: Name of the color
        :type color: str
        """
        colored_cars = list()
        for car in self.park_list:
            if car.color == color:
                colored_cars.append(self.park_list.index(car))
        # Check if the number of cars are zero.
        if len(colored_cars) <= 0:
            log.info(message.NOT_FOUND)
            return
        log.info(','.join(colored_cars))

    def get_slot_number_from_reg_no(self, reg_no):
        """
        Get Car Slot Number from Car Registration Number.

        :param reg_no: Car registration number
        :type reg_no: str
        """
        for car in self.park_list:
            if car.reg_no == reg_no:
                log.info(self.park_list.index(car))
                return
        log.info(message.NOT_FOUND)

    def get_reg_no_from_color(self, color):
        """
        Get Registration number from Car Color.

        :param color: Color of the Car
        :type color: str
        """
        colored_cars = list()
        for car in self.park_list:
            if car.color == color:
                colored_cars.append(car.reg_no)
        # Check if the number of cars are zero.
        if len(colored_cars) <= 0:
            log.info(message.NOT_FOUND)
            return
        log.info(','.join(colored_cars))

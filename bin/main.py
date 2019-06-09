from bin.parking_lot import ParkingAllocation
from library.command_enums import CommandEnums as com
import os
import sys


class program():

    def execute(self):
        input_file = 'PycharmProjects/parking_lot/input/input.txt'
        #print('Welcome to Parking Allocation System Designed by SAHIL CHAUHAN.')
        #print('Taking Input from file %s' % input_file)

        if not os.path.isfile(input_file):
            print("File Path [%s] doesn't exist" % input_file)
            sys.exit()

        # Read File
        try:
            fp = open(input_file, 'r')
            with open(input_file) as fp:
                for line in fp:
                    words = line.strip().split(' ')
                    if words[0] == com.CREATE_PARKING:
                        self.parking_lot = ParkingAllocation(max_size=int(words[1]))
                    if words[0] == com.PARK:
                        self.parking_lot.park(reg_no=words[1],color=words[2])
                    if words[0] == com.EXIT:
                        self.parking_lot.exit()
                    if words[0] == com.GET_REGN_NO_FROM_COLOR:
                        self.parking_lot.get_reg_no_from_color(color=words[1])
                    if words[0] == com.GET_SLOT_FROM_COLOR:
                        self.parking_lot.get_slot_by_color(color=words[1])
                    if words[0] == com.GET_SLOT_FROM_REG_NO:
                        self.parking_lot.get_slot_number_from_reg_no(reg_no=words[1])
                    if words[0] == com.LEAVE:
                        self.parking_lot.leave(slot_no=int(words[1]))
                    if words[0] == com.STATUS:
                        self.parking_lot.status()
            fp.close()
        except Exception as e:
            print('Error')
            print(e)

def main_func():
    prog = program()
    prog.execute()


if __name__ == '__main__':
    main_func()

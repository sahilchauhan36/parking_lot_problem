
class LeaveTests:
    def test_verify_leave_invalid_slot(self):
        """
        Test to verify Leave on Invalid Slot.

        Test Steps:
        1. Create a Parking Lot.
        2. Park One Car.
        3. Leave a Car from Slot which is outside the Parking Slot range.
        """

    def test_verify_leave_vacant_slot(self):
        """
        Test to verify leave operation on an already vacant Slot.

        Test Steps:
        1. Create a Parking lot
        2. Park One Car.
        3. Leave Car from Slot.
        4. Again try to Leave Car from Slot.
        """

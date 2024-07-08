import unittest
from employee import Employee

print("Employee uchun test....")


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUp")
        cls.emp_1 = Employee("Avazbek", "Hazratov", 50000)
        cls.emp_2 = Employee("Asadbek", "Hazratov", 150000)

    @classmethod
    def tearDownClass(cls):
        print("tearDown\n")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, "AvazbekHazratov@email.com")
        self.assertEqual(self.emp_2.email, "AsadbekHazratov@email.com")

        self.emp_1.first = "Leo"
        self.emp_2.first = "Santiago"

        self.assertEqual(self.emp_1.email, "LeoHazratov@email.com")
        self.assertEqual(self.emp_2.email, "SantiagoHazratov@email.com")

    print("good")

    def full_name(self):
        print("full_name")
        self.assertEqual(self.emp_1.fullname, "Avazbek Hazratov")
        self.assertEqual(self.emp_2.fullname, "Asadbek Hazratov")

    print("good")

    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 50000)
        self.assertEqual(self.emp_2.pay, 150000)

    print("3 ta test ham ishladi")


if __name__ == "__main__":
    unittest.main()

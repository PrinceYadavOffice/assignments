#Q1
#
# def convert_cel_to_far(c):
#      """
#      convert celcius to farenheit
#      >>> convert_cel_to_far(37)
#      '37 degrees C = 98.60 degrees F'
#      """
#      f = c * 9 / 5 + 32
#      return f"{c} degrees C = {f:.2f} degrees F"
#
# def convert_far_to_cel(f):
#      """
#      convert celcius to farenheit
#      >>> convert_far_to_cel(72)
#      '72 degrees F = 22.22 degrees C'
#      """
#      c = (f - 32) * 5 / 9
#      return f"{f} degrees F = {c:.2f} degrees C"

def summ(num):
     sum=0
     for i in num:
          sum+=i
     return sum

import unittest
from oop2 import Car,Bus,Employee,Point

class Test(unittest.TestCase):
     def test_sum(self):
          l=(1,2,3)
          self.assertEqual(summ(l),6)

     def test_car_fare(self):
          """Testing Car Fare"""
          c= Car('maruti',18,5)
          fare = (c.mileage * c.capacity) + 15 / 100
          self.assertEqual(c.get_fare(),fare)
     def test_bus_fare(self):
          """Testing Bus Fare"""
          b=Bus('volvo',12,80)
          fare = (b.mileage * b.capacity) + 25 / 100
          self.assertEqual(b.get_fare(),fare)

     def test_add_email(self):
          """Testing Email of Employee"""
          e1 =Employee('prince','yadav',100000)
          email = "prince.yadav@tothenew.com"
          self.assertEqual(e1.addEmail(),email)

     def test_point_add(self):
          """Testing Point object addition"""
          p1=Point(2,3)
          p2=Point(4,5)
          p3 =p1+p2
          self.assertEqual(p3.__repr__(),'(6,8)')


if __name__=="__main__":
     unittest.main()

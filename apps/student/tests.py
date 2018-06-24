from django.test import TestCase
import unittest
from faker import Faker
from .models import Student
from apps.teacher.models import Teacher
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class StudentModelTestClass(TestCase):
    """
    Test model Student
    """

    @classmethod
    def setUpTestData(cls):
        """ Create Student """
        fake = Faker()

        teacher_user = User.objects.create(
            username=fake.simple_profile(sex=None)['username'],
            password=fake.ean8(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
        )

        teacher = Teacher.objects.create(
            user=teacher_user,
            ci=fake.ean8(),
        )

        user = User.objects.create(
            username=fake.simple_profile(sex=None)['username'],
            password=fake.ean8(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
        )

        Student.objects.create(
            user=user,
            teacherMentor=teacher,
            ci=fake.ean8(),
        )

    def setUp(self):
        """ Initial Test """
        self.fake = Faker()

    def test_save_model(self):
        """ Count the number of Currencies """
        saved_models = Student.objects.count()
        self.assertEqual(saved_models, 1)

    def test_update_model(self):
        ci = self.fake.ean8()

        student = Student.objects.all()

        student.update(ci=ci)

        student = Student.objects.all().first()

        self.assertEqual(student.ci, ci)

    def test_delete_model(self):
        student = Student.objects.all().first()
        student.delete()

        saved_models = Student.objects.count()
        self.assertEqual(saved_models, 0)


"""
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/Lizandro Zerpa/Documents/ACADEMIA ULA/INGENIERIA DE SOFTWARE/PROYECTO/chromedriver.exe')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

"""


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.fake = Faker()
        self.driver = webdriver.Chrome('C:/Python27/chromedriver.exe')

    def test_search_in_python_org(self):
        # all_options = element.find_elements_by_tag_name("option")
        driver = self.driver
        driver.get("http://localhost:8000")
        self.assertIn("STI", driver.title)
        # username field
        username = driver.find_element_by_name("username")
        username.send_keys(self.fake.simple_profile(sex=None)['username'])
        username.send_keys(Keys.RETURN)
        # ci field
        ci = driver.find_element_by_name("ci")
        ci.send_keys(self.fake.ean8())
        ci.send_keys(Keys.RETURN)
        # first_name field
        first_name = driver.find_element_by_name("first_name")
        first_name.send_keys(self.fake.first_name())
        first_name.send_keys(Keys.RETURN)
        # last_name field
        last_name = driver.find_element_by_name("last_name")
        last_name.send_keys(self.fake.last_name())
        last_name.send_keys(Keys.RETURN)
        # email field
        email = driver.find_element_by_name("email")
        email.send_keys(self.fake.email())
        email.send_keys(Keys.RETURN)
        # password1
        password = self.fake.ean8()
        password1 = driver.find_element_by_name("password1")
        password1.send_keys(password)
        password1.send_keys(Keys.RETURN)
        # password2
        password2 = driver.find_element_by_name("password2")
        password2.send_keys(password)
        password2.send_keys(Keys.RETURN)
        # teacherMentor field
        teacherMentor = driver.find_element_by_name("teacherMentor")
        teacherMentor.send_keys(1)
        teacherMentor.send_keys(Keys.RETURN)

        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

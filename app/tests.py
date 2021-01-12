from django.test import TestCase
from .models import Location

# Create your tests here.

class LocationTestClass(TestCase):
    '''
    Test case for the Location class .
    '''

    # Set up method
    def setUp(self):
        '''
        Method that will run before any test case under this class
        '''
        self.new_location = Location(location_name = "Nairobi")

    def tearDown(self):
        Location.objects.all().delete()    


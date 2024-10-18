import numpy as np
import unittest
class Test(unittest.TestCase):
    def setUp(self):
        print('Loaded the data file')
    def test_training_cnn(self):
        dat= np.loadtxt("data.csv")
        if len(np.polyfit(dat[:,0], dat[:,1],1))==2:
            print("Polyfit is linear")
        else:
            print("Change polyfit")


from functools import wraps
import unittest
import robot_detection

class RobotDetectTestCase(unittest.TestCase):

    def _known_robot(user_agent):
        def testFunc(self):
            self.assertTrue(robot_detection.is_robot(user_agent))
        testFunc.__doc__ = "Should detect {0} as a robot".format(user_agent)
        return testFunc

    def _known_human(user_agent):
        def testFunc(self):
            self.assertFalse(robot_detection.is_robot(user_agent))
        testFunc.__doc__ = "Should not detect {0} as a robot".format(user_agent)
        return testFunc

    testGoogle1 = _known_robot("googlebot")
    testGoogle2 = _known_robot("Foo bargooglebot")
    testGoogle3 = _known_robot("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
    testGoogle4 = _known_robot('\xef\xbb\xbfMozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
    testYeti = _known_robot('Yeti/1.0 (NHN Corp.; http://help.naver.com/robots/)')
    testHuman1 = _known_human("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.83 Safari/535.11")

        

if __name__ == '__main__':
    unittest.main()

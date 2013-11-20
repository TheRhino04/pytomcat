import os,sys,random
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

from tomcat.retry import retry

@retry(Exception, tries=4)
def test_fail():
    raise Exception("Fail")

@retry(Exception)
def test_success():
    print "Success"

@retry(Exception, tries=8)
def test_random():
    x = random.random()
    if x < 0.5:
        raise Exception("Fail")
    else:
        print "Success"


def test_failures():
    try:
        test_fail()
    except:
        return True
    else:
        return False

def test_success():
    try:
        test_success()
    except:
        return False
    else:
        return True

def test_random_success():
    try:
        test_random()
    except:
        return False
    else:
        return True

if test_failures() and test_success() and test_random_success():
    print "Selftest OK"
else:
    print "Selftest Failure"

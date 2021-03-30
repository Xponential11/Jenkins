###########################Name:Sarth Vadgama ############################################
import pytest
import tasks 
from tasks import Task



#################Task----2########################


@pytest.fixture(autouse=True,scope='module')
def test_yield():
    print('\nBefore Yield')
    yield
    print('\nAfter Yield')

@pytest.fixture()
def tuple_data():
    return ('test',True,False,34,{'size':1024})

@pytest.fixture()
def list_data():
    return [4,'soft','hard',True,False,None]

@pytest.fixture()
def dict_data():
    return {'apple':'a','orange':'o','banana':'b','kiwi':'k','berry':'be'}


@pytest.fixture(scope='module')
def test_double():
    return [3,4,5,'string',True]




###################################################

##########Task----3################################

def test_tuple(tuple_data):
    assert tuple_data[4]['size'] == 1024 #Pass

def test_list(list_data):
    assert list_data[1] == 'soft' #Fail

def test_dict(dict_data):
    assert dict_data['apple'] == 'a' #pass

####################################################

###########Task-4###################################

def test_double_1(test_double):
    assert isinstance(test_double[0],int)

def test_double_2(test_double):
    assert isinstance(test_double[3],str)

####################################################


#########################Task-8,9###################
def test_yield_fun():
    print ('\nIn function')
    assert True
    


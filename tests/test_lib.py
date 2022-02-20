from mlprojectTeacher.lib import try_me

def test_length_of_try_me():
    assert len(try_me()) != 0
    
def test_try_me():
    assert(try_me() == "You're trespassing! Abandon all hope ye who enter here !!")
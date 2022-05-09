class TestClass(object):
    v = 0
    def test_one(self):
        TestClass.v = 1
        assert TestClass.v  == 1

    def test_two(self):
        assert TestClass.v  == 1


        
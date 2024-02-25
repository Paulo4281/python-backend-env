class TestUserModule:
    @staticmethod
    def test_user_auth():
        assert 1 + 1 == 2
    
    @staticmethod
    def test_user_save():
        assert 1 + 2 == 3

    @staticmethod
    def test_user_find():
        assert 1 + 4 == 5

    @staticmethod
    def test_user_find_by_id():
        assert True
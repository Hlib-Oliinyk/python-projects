from lab8_task9 import User, Privileges, Admin


class TestUser:
    def test_valid_user_initialization(self):
        user = User("Іван", "Петров", "ivan@example.com", "ivan123", True)
        assert user.valid is True
        assert user.first_name == "Іван"
        assert user.last_name == "Петров"
        assert user.email == "ivan@example.com"
        assert user.nickname == "ivan123"
        assert user.newsletter_consent is True
        assert user.login_attempts == 0

    def test_invalid_first_name(self):
        user = User("", "Петров", "ivan@example.com", "ivan123", True)
        assert user.valid is False
        assert user.first_name is None

    def test_invalid_email_format(self):
        user = User("Іван", "Петров", "invalid-email", "ivan123", True)
        assert user.valid is False
        assert user.email is None

    def test_valid_email_format(self):
        user = User("Іван", "Петров", "test@example.com", "test", True)
        assert user.valid is True
        assert user.email == "test@example.com"

    def test_invalid_newsletter_consent(self):
        user = User("Іван", "Петров", "ivan@example.com", "ivan123", "not_bool")
        assert user.valid is False
        assert user.newsletter_consent is False

    def test_describe_user(self):
        user = User("Іван", "Петров", "ivan@example.com", "ivan123", True)
        desc = user.describe_user()
        assert desc == "Користувач: Іван Петров"

        invalid_user = User("", "Петров", "ivan@example.com", "ivan123", True)
        assert invalid_user.describe_user() is None

    def test_greeting_user(self):
        user = User("Іван", "Петров", "ivan@example.com", "ivan123", True)
        greeting = user.greeting_user()
        assert greeting == "Вітаємо, ivan123!"

        invalid_user = User("Іван", "", "ivan@example.com", "ivan123", True)
        assert invalid_user.greeting_user() is None

    def test_login_attempts(self):
        user = User("Іван", "Петров", "ivan@example.com", "ivan123", True)
        assert user.increment_login_attempts() is True
        assert user.login_attempts == 1
        assert user.increment_login_attempts() is True
        assert user.login_attempts == 2

        assert user.reset_login_attempts() is True
        assert user.login_attempts == 0

        invalid_user = User("", "Петров", "invalid", "ivan123", True)
        assert invalid_user.increment_login_attempts() is False
        assert invalid_user.reset_login_attempts() is False


class TestPrivileges:
    def test_valid_privileges(self):
        priv = Privileges(["can_delete", "can_add_users"])
        assert priv.privileges == ["can_delete", "can_add_users"]

    def test_empty_privileges(self):
        priv = Privileges()
        assert priv.privileges == []

    def test_invalid_privileges(self):
        priv = Privileges(["can_delete", 123])
        assert priv.privileges == []

    def test_show_privileges(self):
        priv = Privileges(["can_delete", "can_add_users"])
        result = priv.show_privileges()
        expected = "Привілеї адміністратора:\n- can_delete\n- can_add_users"
        assert result == expected

        empty_priv = Privileges()
        assert empty_priv.show_privileges() == "Немає привілеїв"


class TestAdmin:
    def test_valid_admin(self):
        admin = Admin("Адмін", "Системний", "admin@example.com", "admin", True,
                      ["can_delete", "can_ban"])
        assert admin.valid is True
        assert admin.first_name == "Адмін"
        assert admin.privileges.privileges == ["can_delete", "can_ban"]

    def test_invalid_admin_from_user(self):
        admin = Admin("", "Системний", "admin@example.com", "admin", True)
        assert admin.valid is False
        assert admin.first_name is None

    def test_admin_privileges(self):
        admin = Admin("Адмін", "Системний", "admin@example.com", "admin", True)
        assert admin.privileges.show_privileges() == "Немає привілеїв"

        admin_with_priv = Admin("Адмін", "Системний", "admin@example.com", "admin", True,
                                ["manage_users"])
        result = admin_with_priv.privileges.show_privileges()
        assert result == "Привілеї адміністратора:\n- manage_users"

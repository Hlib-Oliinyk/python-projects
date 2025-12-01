import re

class User:
    def __init__(self, first_name, last_name, email, nickname, newsletter_consent):
        self.valid = True
        self.login_attempts = 0

        if not isinstance(first_name, str) or not first_name.strip():
            self.valid = False
            self.first_name = None
        else:
            self.first_name = first_name.strip()

        if not isinstance(last_name, str) or not last_name.strip():
            self.valid = False
            self.last_name = None
        else:
            self.last_name = last_name.strip()

        if not isinstance(email, str) or not email.strip():
            self.valid = False
            self.email = None
        elif not self.is_valid_email(email):
            self.valid = False
            self.email = None
        else:
            self.email = email.strip()

        if not isinstance(nickname, str) or not nickname.strip():
            self.valid = False
            self.nickname = None
        else:
            self.nickname = nickname.strip()

        if not isinstance(newsletter_consent, bool):
            self.valid = False
            self.newsletter_consent = False
        else:
            self.newsletter_consent = newsletter_consent

    def is_valid_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(pattern, email.strip()))

    def describe_user(self):
        if not self.valid:
            return None
        return f"Користувач: {self.first_name} {self.last_name}"

    def greeting_user(self):
        if not self.valid:
            return None
        return f"Вітаємо, {self.nickname}!"

    def increment_login_attempts(self):
        if not self.valid:
            return False
        self.login_attempts += 1
        return True

    def reset_login_attempts(self):
        if not self.valid:
            return False
        self.login_attempts = 0
        return True


class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = []
        elif isinstance(privileges, list) and all(isinstance(p, str) for p in privileges):
            self.privileges = privileges
        else:
            self.privileges = []

    def show_privileges(self):
        if not self.privileges:
            return "Немає привілеїв"
        result = ["Привілеї адміністратора:"]
        result += [f"- {p}" for p in self.privileges]
        return "\n".join(result)


class Admin(User):
    def __init__(self, first_name, last_name, email, nickname, newsletter_consent, privileges=None):
        super().__init__(first_name, last_name, email, nickname, newsletter_consent)
        self.privileges = Privileges(privileges)

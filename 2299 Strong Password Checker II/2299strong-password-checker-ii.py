class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        n = len(password)

        if n < 8:
            return False
        lower = any(c.islower() for c in password)
        upper = any(c.isupper() for c in password)
        digit = any(c.isdigit() for c in password)
        special = any(c in "!@#$%^&*()-+" for c in password)
        adjacent = any(password[i] == password[i + 1] for i in range(n - 1))

        return lower and upper and digit and special and not adjacent


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        missing_types = 3
        if any(c.islower() for c in password):
            missing_types -= 1
        if any(c.isupper() for c in password):
            missing_types -= 1
        if any(c.isdigit() for c in password):
            missing_types -= 1

        replace = 0
        one_removes = 0
        two_removes = 0
        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            length = j - i
            if length >= 3:
                replace += length // 3
                if length % 3 == 0:
                    one_removes += 1
                elif length % 3 == 1:
                    two_removes += 1
            i = j

        if n < 6:
            return max(missing_types, 6 - n)
        elif n <= 20:
            return max(missing_types, replace)
        else:
            delete = n - 20
            replace -= min(delete, one_removes)
            replace -= min(max(delete - one_removes, 0), two_removes * 2) // 2
            replace -= max(delete - one_removes - two_removes * 2, 0) // 3
            return delete + max(missing_types, replace)
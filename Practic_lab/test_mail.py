import unittest
import check_mail

class Test_test_mail(unittest.TestCase):
    def test_mail_T(self):
        list_mail_cor = ["dhdf@mail.ru", "fkjh@gmail.com", "dsjkfsdk@yandex.ru"]
        for email in list_mail_cor:
            self.assertTrue(check_mail.mail_check(email))

    def test_mail_F(self):
        list_mail_uncor = ["sdf@mailru", "gsaf.ru", "sadf@", "1",""]
        for email in list_mail_uncor:
            self.assertFalse(check_mail.mail_check(email))


if __name__ == '__main__':
    unittest.main()

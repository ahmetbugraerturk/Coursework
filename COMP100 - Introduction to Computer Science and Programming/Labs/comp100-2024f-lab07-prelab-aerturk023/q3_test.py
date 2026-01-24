import unittest
from q3 import generate_monthly_report

class TestGenerateMonthlyReport(unittest.TestCase):

    def test_generate_monthly_report(self):
        transactions = [  # Reset transactions to its original values
            {'id': 1, 'type': 'credit', 'amount': 500, 'timestamp': '2024-01-05'},
            {'id': 2, 'type': 'debit', 'amount': 300, 'timestamp': '2024-01-10'},
            {'id': 3, 'type': 'credit', 'amount': 700, 'timestamp': '2024-01-15'},
            {'id': 4, 'type': 'debit', 'amount': 200, 'timestamp': '2024-01-20'},
            {'id': 5, 'type': 'credit', 'amount': 100, 'timestamp': '2024-01-25'},
            {'id': 6, 'type': 'credit', 'amount': 900, 'timestamp': '2024-02-01'},
            {'id': 7, 'type': 'debit', 'amount': 400, 'timestamp': '2024-02-05'},
            {'id': 8, 'type': 'credit', 'amount': 600, 'timestamp': '2024-02-12'},
            {'id': 9, 'type': 'debit', 'amount': 300, 'timestamp': '2024-02-18'},
            {'id': 10, 'type': 'credit', 'amount': 800, 'timestamp': '2024-02-28'},
            {'id': 11, 'type': 'credit', 'amount': 1200, 'timestamp': '2024-03-03'},
            {'id': 12, 'type': 'debit', 'amount': 700, 'timestamp': '2024-03-08'},
            {'id': 13, 'type': 'credit', 'amount': 300, 'timestamp': '2024-03-12'},
            {'id': 14, 'type': 'credit', 'amount': 400, 'timestamp': '2024-03-16'},
            {'id': 15, 'type': 'debit', 'amount': 500, 'timestamp': '2024-03-22'},
            {'id': 16, 'type': 'credit', 'amount': 700, 'timestamp': '2024-04-01'},
            {'id': 17, 'type': 'debit', 'amount': 200, 'timestamp': '2024-04-05'},
            {'id': 18, 'type': 'credit', 'amount': 500, 'timestamp': '2024-04-10'},
            {'id': 19, 'type': 'debit', 'amount': 100, 'timestamp': '2024-04-15'},
            {'id': 20, 'type': 'credit', 'amount': 900, 'timestamp': '2024-04-20'},
            {'id': 21, 'type': 'credit', 'amount': 800, 'timestamp': '2024-05-03'},
            {'id': 22, 'type': 'debit', 'amount': 400, 'timestamp': '2024-05-08'},
            {'id': 23, 'type': 'credit', 'amount': 600, 'timestamp': '2024-05-12'},
            {'id': 24, 'type': 'debit', 'amount': 300, 'timestamp': '2024-05-16'},
            {'id': 25, 'type': 'credit', 'amount': 1000, 'timestamp': '2024-05-28'},
            {'id': 26, 'type': 'credit', 'amount': 500, 'timestamp': '2024-06-02'},
            {'id': 27, 'type': 'debit', 'amount': 300, 'timestamp': '2024-06-06'},
            {'id': 28, 'type': 'credit', 'amount': 400, 'timestamp': '2024-06-10'},
            {'id': 29, 'type': 'credit', 'amount': 800, 'timestamp': '2024-06-15'},
            {'id': 30, 'type': 'debit', 'amount': 200, 'timestamp': '2024-06-20'},
        ]
        expected_result = {
            '2024-01': {'total_credit': 1300, 'total_debit': 500, 'net_balance': 800},
            '2024-02': {'total_credit': 2300, 'total_debit': 700, 'net_balance': 1600},
            '2024-03': {'total_credit': 1900, 'total_debit': 1200, 'net_balance': 700},
            '2024-04': {'total_credit': 2100, 'total_debit': 300, 'net_balance': 1800},
            '2024-05': {'total_credit': 2400, 'total_debit': 700, 'net_balance': 1700},
            '2024-06': {'total_credit': 1700, 'total_debit': 500, 'net_balance': 1200}
        }
        result = generate_monthly_report(transactions)
        self.assertEqual(result, expected_result)

    def test_empty_transactions(self):
        empty_transactions = []
        result = generate_monthly_report(empty_transactions)
        self.assertEqual(result, {})

    def test_single_transaction(self):
        single_transaction = [{'id': 1, 'type': 'credit', 'amount': 100, 'timestamp': '2024-01-01'}]
        result = generate_monthly_report(single_transaction)
        expected_result = {
            '2024-01': {'total_credit': 100, 'total_debit': 0, 'net_balance': 100}
        }
        self.assertEqual(result, expected_result)

    def test_credit_only(self):
        credit_only_transactions = [
            {'id': 1, 'type': 'credit', 'amount': 500, 'timestamp': '2024-01-05'},
            {'id': 2, 'type': 'credit', 'amount': 300, 'timestamp': '2024-01-10'},
            {'id': 3, 'type': 'credit', 'amount': 200, 'timestamp': '2024-02-05'},
        ]
        result = generate_monthly_report(credit_only_transactions)
        expected_result = {
            '2024-01': {'total_credit': 800, 'total_debit': 0, 'net_balance': 800},
            '2024-02': {'total_credit': 200, 'total_debit': 0, 'net_balance': 200},
        }
        self.assertEqual(result, expected_result)

    def test_debit_only(self):
        debit_only_transactions = [
            {'id': 1, 'type': 'debit', 'amount': 200, 'timestamp': '2024-01-05'},
            {'id': 2, 'type': 'debit', 'amount': 100, 'timestamp': '2024-01-10'},
            {'id': 3, 'type': 'debit', 'amount': 300, 'timestamp': '2024-02-05'},
        ]
        result = generate_monthly_report(debit_only_transactions)
        expected_result = {
            '2024-01': {'total_credit': 0, 'total_debit': 300, 'net_balance': -300},
            '2024-02': {'total_credit': 0, 'total_debit': 300, 'net_balance': -300},
        }
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGenerateMonthlyReport)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")


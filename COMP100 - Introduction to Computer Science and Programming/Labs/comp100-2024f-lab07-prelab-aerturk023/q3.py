from datetime import datetime

transactions = [
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
] # Do not modify this list

def generate_monthly_report(transactions):
    """Groups a list of transactions by month, calculates the total credits and debits for each month, and computes the net balance for each month. Returns a dictionary with the monthly report."""
    
    tot_dic = {}
    
    for trans in transactions:
        
        date = trans['timestamp'][:7]

        
        if date not in tot_dic.keys():
            tot_dic[date] = {'total_credit': 0, 'total_debit': 0, 'net_balance': 0}
        tot_dic[date][f"total_{trans['type']}"] += trans['amount']
        tot_dic[date]['net_balance'] = tot_dic[date]['total_credit']-tot_dic[date]['total_debit']
    
    return tot_dic

        

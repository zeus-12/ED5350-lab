#f part
def sortBankAccounts(bank_accounts):
    bank_accounts = sorted(bank_accounts, key=lambda x: x[0])
    return bank_accounts

#b part
def createAccount(bank_details, bank_accounts):
    bank_accounts.append(bank_details)
    bank_accounts = sortBankAccounts(bank_accounts)
    return bank_accounts

# c part
def deleteAccount(name,bank_accounts):
    for account_details in bank_accounts:
        if name in account_details:
            bank_accounts.remove(account_details)
    return bank_accounts

# d part
def appendStart(bank_details, bank_accounts):
    bank_accounts.insert(0, bank_details)
    return bank_accounts

# e part
def removeDuplicates(bank_accounts):
    new_bank_accounts = []
    for account in bank_accounts:
        if account in new_bank_accounts:
            continue
        else:
            new_bank_accounts.append(account)
    return new_bank_accounts


#a part
# list of lists
bank_accounts = [["vishnu","13-12-2002","kerala",4000],["pranav","01-05-2001","kerala",12000],["pranoy","06-08-2001","kerala",8000],["thazeel","13-02-2001","kerala",2000],["albin","23-12-2003","kerala",6000],]



new_account_details_1 = ["sarath","20-04-2000","chennai",2500]
bank_accounts = createAccount(new_account_details_1, bank_accounts)

bank_accounts = deleteAccount("vishnu", bank_accounts)

new_account_details_2 = ["nihad","20-04-2000","chennai",2500]
bank_accounts = appendStart(new_account_details_2, bank_accounts)

bank_accounts = createAccount(new_account_details_1, bank_accounts)
bank_accounts = removeDuplicates(bank_accounts)
bank_accounts = sortBankAccounts(bank_accounts)

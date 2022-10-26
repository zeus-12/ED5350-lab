#b part
def createAccount(name, bank_accounts):
    bank_accounts.append(name)
    bank_accounts.sort()
    return bank_accounts

# c part
def deleteAccount(name,bank_accounts):
    if name in bank_accounts:
        bank_accounts.remove(name)
    return bank_accounts

# d part
def appendStart(name, bank_accounts):
    bank_accounts.insert(0, name)
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

# f part
def sortAccounts(bank_accounts):
    bank_accounts.sort()
    return bank_accounts

#a part
bank_accounts = ['c','d','e','z','b','d','e','kaj']
bank_accounts.sort()

bank_accounts = createAccount("aaa", bank_accounts)
bank_accounts = appendStart("kaj", bank_accounts)
bank_accounts = removeDuplicates(bank_accounts)
bank_accounts = sortAccounts(bank_accounts)

print(bank_accounts)
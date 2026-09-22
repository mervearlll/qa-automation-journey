
test_results = [True, True, True, False, False, True, False]
test= len(test_results)
print(test)


passed_test = 0
for result in test_results: 
    if result == True:
     passed_test = passed_test +1 
print("passed:", passed_test )

failed_test = 0
for result in test_results:
    if result == False:
       failed_test = failed_test +1
print("failed:", failed_test)

def calculate_pass_rate(passed_test, failed_test, test):
    pass_rate = (passed_test / test)*100 
    fail_rate = (failed_test/ test)*100
    return pass_rate, fail_rate

print(calculate_pass_rate(passed_test, failed_test, test))
#pass_rate = (passed_test/len(test_results))*100
#fail_rate = (failed_test/test)*100

#print(pass_rate, fail_rate)

ttest_results = [True, False, True, True, False, True,True, False]
ttest = len(ttest_results)
print(ttest)

passed_test1 = 0
for result in ttest_results:
   if result == True:
    passed_test1 = passed_test1 +1 
print("passed1", passed_test1)

failed1_test = 0
for result in ttest_results:
   if result == False:
      failed1_test = failed1_test +1
print("failed1", failed1_test)

def calculate_pass_rate1 (ttest, failed1_test, passed_test1):
   passed_rate1 = (passed_test1/ttest)*100
   return passed_rate1
print("passedRate1", calculate_pass_rate1(ttest, failed1_test, passed_test1))

def calculate_failed_rate1 (ttest, failed1_test, passed_test1):
   failed1_rate1 = (failed1_test/ttest)*100
   return failed1_rate1
print("failed_rate1", calculate_failed_rate1(ttest, failed1_test, passed_test1))

test_results = [
    True,
    True,
    False,
    True,
    False,
    False,
    True,
    True,
    True,
    False
]

test = len(test_results)
print(test)

passed_test = 0
for result in test_results:
    if result == True:
        passed_test = passed_test + 1
print ("passed", passed_test)

failed_test = 0
for result in test_results: 
   if result == False:
       failed_test = failed_test +1
print("failed", failed_test)

def calculate_rates(test, passed_test, failed_test):
    passed_rate = (passed_test/ test)*100
    failed_rate = (failed_test/test)*100
    return passed_rate, failed_rate
print("passed_rate", "failed_rate", calculate_rates(test, passed_test, failed_test))

test_results = [
    True,
    False,
    True,
    True,
    True,
    True,
    False,
    True
]
  
test = len(test_results)
print(test)

passed_test = 0
for result in test_results:
    if result == True:
        passed_test = passed_test +1
print("passed", passed_test)

failed_test = 0
for result in test_results:
    if result == False:
        failed_test = failed_test +1
print("failed", failed_test)

def calculate_rates(test, failed_test, passed_test):
    passed_rate = (passed_test/test)*100
    failed_rate = (failed_test/test)*100
    return passed_rate , failed_rate
passed_rate , failed_rate = calculate_rates(test, failed_test, passed_test)
print(f"Pass rate: {passed_rate:.2f}%")
print(f"Fail rate: {failed_rate:.2f}%")

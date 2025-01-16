###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = 20
tasks_ok = total_tasks/2
test_passed = False
your_mark=input("enteer yout mark from yest:")
if your_mark >= tasks_ok:
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')
import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)


folder_in = '/home/alexey/tst'
folder_out = '/home/alexey/out'


def test_step1():
    assert checkout(f'cd {folder_in}; 7z a {folder_out}/arh1', 'Everything is Ok'), 'test1 FAIL'


def test_step2():
    assert checkout(f'cd {folder_in}; 7z u {folder_out}/arh1', 'Everything is Ok'), 'test2 FAIL'


def test_step3():
    assert checkout(f'cd {folder_in}; 7z d {folder_out}/arh1', 'Everything is Ok'), 'test3 FAIL'


def test_step4():
    assert checkout(f'cd {folder_in}; 7z l {folder_out}/arh1', 'Everything is Ok'), 'test4 FAIL'


def test_step5():
    assert checkout(f'cd {folder_in}; 7z x {folder_out}/arh1', 'Everything is OK'), 'test5 FAIL'


def test_step6():
    assert checkout(f'cd {folder_in}; 7z h {folder_out}/arh1', 'Everything is Ok'), 'test6 FAIL'

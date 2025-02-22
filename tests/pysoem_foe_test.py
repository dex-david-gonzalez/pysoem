
import pytest
import pysoem


def test_foe_good(pysoem_env):
    pysoem_env.config_init()
    test_slave = pysoem_env.get_slave_for_foe_testing()

    for file_path in ['./foe_testdata/random_data_01.bin', './foe_testdata/random_data_02.bin']:
        with open(file_path, 'rb') as file:
            random_data = file.read()

        # write
        test_slave.foe_write('test.bin', 0, random_data)
        # read back
        reread_data = test_slave.foe_read('test.bin', 0, 8192)
        # and check if the reread data is the same as the written data
        assert reread_data[:len(random_data)] == random_data


def test_foe_fails(pysoem_env):
    pysoem_env.config_init()
    test_slave = pysoem_env.get_slave_without_foe_support()

    # expect foe READ to fail
    with pytest.raises(pysoem.MailboxError) as excinfo:
        test_slave.foe_read('test.bin', 0, 8192)

    assert excinfo.value.error_code == 2
    assert excinfo.value.desc == 'The mailbox protocol is not supported'

    # expect foe WRITE to fail
    with pytest.raises(pysoem.MailboxError) as excinfo:
        test_slave.foe_write('test.bin', 0, bytes(32))

    assert excinfo.value.error_code == 2
    assert excinfo.value.desc == 'The mailbox protocol is not supported'


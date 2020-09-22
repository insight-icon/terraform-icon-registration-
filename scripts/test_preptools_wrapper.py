import preptools_wrapper as pc
import os
import pytest


def test_working():
    """Test working."""

    network_name = "testnet"
    keystore_path = os.path.abspath(os.path.join("..", "test", "fixtures", "keystore", "testnet"))
    register_json = os.path.abspath(os.path.join("..", "registerPRep.json"))
    keystore_password = "testing1."
    p = pc.PRepChecker(network_name, keystore_path, register_json, keystore_password)
    p.prep_reg()
    print(p.operator_wallet_password)
    print(p.output)
    print(p.err)
    print(p.command)


def test_empty():
    """Test working."""

    network_name = "testnet"
    keystore_path = os.path.abspath(os.path.join("..", "test", "fixtures", "keystore", "empty"))
    register_json = os.path.abspath(os.path.join("..", "registerPRep.json"))
    keystore_password = "testing1."
    p = pc.PRepChecker(network_name, keystore_path, register_json, keystore_password)
    with pytest.raises(ValueError) as e:
        p.prep_reg()

    assert e


# Lab 9 Ethan Newton

import re


def is_valid_license_plate(license_plate):
    """
    Validation of license_plate based on requirements from lab document
    :param license_plate: The license plate that is to be validated
    :return: True or False
    """
    if re.match("[A-Z0-9]{6}|[A-Z]{2}[0-9] [0-9]{2}[A-Z]|[A-Z]{2}[0-9]-[0-9]{2}[A-Z]", license_plate):
        return True
    else:
        return False


def is_valid_python_name(python_name):
    """
    Validates python_name based on requirements from lab document
    :param python_name: The python name to be validated
    :return: True or False
    """
    if re.match("[a-z](_?[a-z]){1,32}", python_name):
        return True
    else:
        return False


def is_valid_email_address(email_address):
    """
    Validates email_address based on requirements from lab document
    :param email_address: The email address to be validated
    :return: True or False
    """
    if re.match("[a-z][?_a-z]{1,255}@[a-z]{1,32}.[a-z]{2,5}", email_address, re.I):
        print("Large Peen")
        return True
    else:
        return False

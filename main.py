# Lab 9 Ethan Newton partners are Erik and William

import re


def is_valid_license_plate(license_plate):
    """
    Validation of license_plate based on requirements from lab document
    :param license_plate: The license plate that is to be validated
    :return: True
    """
    if re.match("[A-Z0-9]{6}|[A-Z]{2}[0-9] [0-9]{2}[A-Z]|[A-Z]{2}[0-9]-[0-9]{2}[A-Z]", license_plate):
        return True


def is_valid_python_name(python_name):
    """
    Validates python_name based on requirements from lab document
    :param python_name: The python name to be validated
    :return: True
    """
    if re.match("[a-z](_?[a-z]){0,31}", python_name):
        return True


def is_valid_email_address(email_address):
    """
    Validates email_address based on requirements from lab document
    :param email_address: The email address to be validated
    :return: True
    """
    if re.match("[a-z][_?a-z]{1,255}@[a-z]{1,32}.[a-z]{2,5}", email_address, re.I):
        return True


def is_valid_human_height(height):
    """
    Validates human_height based on requirements from lab document
    :param height: The height to be validated
    :return: True
    """
    if re.match("[2-8]'((0?[1-9](\"|in))|(1[0-2](\"|in)))", height):
        return True


def main():
    is_valid_license_plate("ABC123")
    is_valid_python_name("this_is_a_good_name")
    is_valid_email_address("solid_email___right_here@gmail.com")
    is_valid_human_height("5\'09\"")


if __name__ == '__main__':
    main()

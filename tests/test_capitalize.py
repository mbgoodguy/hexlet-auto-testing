#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from package_name.capitalize import capitalize
if capitalize('hello') != 'Hello':
    raise Exception('Функция работает неверно!')

if capitalize('') != '':
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')
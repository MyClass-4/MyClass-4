# -*- coding:utf-8 -*-
from MyClass.wsgi import *
from User.models import *
import csv
import os
import codecs

def main():
    file = codecs.open('/home/boyce/myclass.csv')
    reader = csv.reader(file)
    reader.next()
    record = reader.next()
    while True:
        user, not_exist= User.objects.get_or_create(name = record[0], number = record[1])
        if not_exist:
            user.save()
        try:
            record = reader.next()
        except:
            break

if __name__ == '__main__':
    main()
    print 'Done'

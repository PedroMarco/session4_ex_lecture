__author__ = 'acpb859'

sentinel_value = -5
while sentinel_value !=0:
    print('loop still running because setinel_value is %s' % sentinel_value)
    sentinel_value = eval(input('Enter a value, and stop loop with 0'))

### %s' % sentinel_value would work as an str as well
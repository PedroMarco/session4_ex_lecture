__author__ = 'acpb859'
# pdb allows to read debug per error line.
# n step fwd until error, c is 'Continue'
def nPrintln(message, n):
    for i in range(0, n):
        print(message)

nPrintln('Naranjas', 4)
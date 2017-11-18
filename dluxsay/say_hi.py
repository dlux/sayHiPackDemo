'''
Simple say hi class
The intention is to grow from here


@author: luzC
'''
import random
import sys


class SayHiClass(object):
    '''
    Say hi class documentation
    '''

    def __init__(self):
        '''
        Class constructor

        '''
        pass

    def hi(self, name='Stranger'):
        """ Print a random greeting for a given name """
        hi = ("Bonjour","Hello", "Hi", "Hola", "Ni hao")
        
        print('{0} {1}'.format(random.choice(hi), name))

    def sum(self, values):
        """
        Addition operation on a given list of int values
        Raises a ValueError Exeption if non-numeric values are passed.
        Raises a TypeError if no parameters are given.

        e.g. dlux_say sum 20 20 10
        """
        result = 0
        try:
            values = map(int, values)

            for num_ in values:
                result = result + num_

        except ValueError:
            print ("Skiping due to invalid entry {0}".format(values))
            raise

        print ("Sum is = {0}".format(result))
        return result


def main():
    args = sys.argv[1:]
    dlux = SayHiClass()

    if not args:
        dlux.hi() 
    elif args[0] == "sum":
        dlux.sum(args[1:])
    else:
        dlux.hi(''.join(args)) 


if __name__ == '__main__':
    main()
    #dlux = sayHiClass()
    #dlux.hi()
    #dlux.sum([1,2,3,4])

def collatz(n):
    '''
    Purpose:
        Perform a Collatz conjecture. This means to take in number and if it is even, divide it by 2, if it is odd multiply it by 3 and add 1.
        Once it reaches 1, find the sum of all the integers, including the starting integer.
    Parameter(s):
        n: Any positive integer.
    Return Value:
        The sum of all the numbers found in the Collatz conjecture including the starting number. 
    '''
    if n == 1:
        return 1
    if n % 2 != 0:
        return n + collatz(n * 3 + 1)
    if n % 2 == 0:
        return n + collatz(n // 2)

def two_es(lines):
    '''
    Purpose:
        Determine of the given list has any strings containing exactly two lowercase 'e''s.
    Parameter(s):
        lines: A list containing strings 
    Return Value:
        Returns True if there is a string that containes exactly two 'e''s, returns False if there are no strings containing exactly two 'e''s.
            Uppercase E's do not count.
    '''
    if lines == []:
        return False
    if lines[0].count('e') == 2:
        return True
    else:
        return two_es(lines[1:])

import os
def get_targets(path):
    '''
    Purpose:
        Use a helper function containing a list to return a list of evil organizations. 
    Parameter(s): 
        path: The given file that the code will look through.
    Return Value:
        A helper function added that contains a list, so that eachtext file found that passes the rules is concatanated to.
    '''
    return help_get_targets(path,[])

def help_get_targets(path,target):
    '''
    Purpose:
        Find the target of evil organizations within a document
    Parameter(s):
        path: The given file that the code will look through
        target: An empty list
    Return Value:
        A list containing all of the targets that fit the parameters ( Any txt file that contains a line with exactly two lowercase 'e''s).
    '''
    for file in os.listdir(path): 
        if os.path.isfile(path+'/'+file):
            if file.endswith('.txt'):
                fp = open(path+'/'+file)
                for line in fp:
                    y = line.strip()
                    if two_es([y]) == True:
                        target.append(path+'/'+file)
                fp.close
        else:
            help_get_targets(path+'/'+file,target)
    return target
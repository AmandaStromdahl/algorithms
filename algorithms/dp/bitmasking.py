MAX_NB_PEOPLE = 10

"""
Check that the given caps sets is valid 

:param capsSets: The caps sets to check
:returns: nothing but raises errors if invalid caps sets
"""
def checkArgument(capsSets: list, nbCaps: int):
    if len(capsSets) > MAX_NB_PEOPLE:
        raise ValueError(f'The maximum number of people is {MAX_NB_PEOPLE}, but you gave {len(capsSets)} people !')
    for capsSet in capsSets:
        if not isinstance(capsSet, list):
            raise ValueError(f'The given caps set {capsSet} is not valid !')
        for cap in capsSet:
            if not isinstance(cap, int):
                raise ValueError(f'The given cap "{cap}" in caps set {capsSet} is not valid !')
            if cap > nbCaps:
                raise ValueError(f'The maximum cap id is {nbCaps}, but you gave a cap id "{cap}" in caps set {capsSet} !')

def initialization(capsSets: list, nbCaps: int):

    checkArgument(capsSets, nbCaps)

    nbPeople = len(capsSets)
    nbMasks = 2 ** nbPeople

    # TODO initialize the caps dict
    # TODO initialize the DP matrix

    # TODO return the values

"""
Determines the nr of ways to assign unique caps to every person using bitmasking and dynamic programming (dp).

:param capSets: A nested list containing the caps of every person. 
:returns: The nr of ways to select unique caps for every person.
"""
def assignUniqueCaps(capsSets: list, nbCaps: int) -> int:

    # TODO assign values from initialization

    # TODO call the algorithm
    
    return 0

# For debugging purposes
def main():
    caps=[[1,2,3], [4], [1,2]]
    nbCaps = 4
    print(assignUniqueCaps(caps, nbCaps))
    
if __name__ == '__main__':
    main()
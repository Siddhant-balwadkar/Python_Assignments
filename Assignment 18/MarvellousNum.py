##############################################################
#  Function Name :           ChkPrime
#  Description   :           Checks whether the given number is prime
#  Author :                 Siddhant Vikas Balwadkar
#  Date :                   14/07/2026
##############################################################

def ChkPrime(No):
    if No <= 1:
        return False

    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False

    return True
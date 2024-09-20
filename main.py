"""
Code de la fonction palindrome
"""
#### Fonction secondaire


INTAB="AÀàBCçDEéèeëêÉFGHIïîJKLMNOôöPQRSTUùVWXYZ"
OUTAB="aaabccdeeeeeeefghiiijklmnooopqrstuuvwxyz"
SUP="' ,.?;:/!-"
Transtab=str.maketrans(INTAB,OUTAB)
Transtab1=str.maketrans("","",SUP)


def ispalindrome(x):
    """
    Cherche si une fonction est un palindrome
    Args:
        x = chaîne de caractère
    Returns:
        Bool = True si x palindrome, False sinon
    """
    s=x.translate(Transtab1).translate(Transtab)
    for i in range(len(s)):
        if s[i]!=s[len(s)-1-i]:
            return False
    return True

#### Fonction principale

def main():
    """
    Test la fonction palindrome pour plusieurs exemple
    """

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()

import re
from random import randrange


def check_for_login_data(USERNAME: str, PASSWORD: str) -> None:
    """Make sure user entered their login data."""
    if not USERNAME or not PASSWORD:
        print("\n")
        if not USERNAME:
            print("> Missing Username! <".center(40, "-"))
        else:
            print("> Missing Password! <".center(40, "-"))
        print("\n")
        raise ValueError("Missing Login Info!")


def url_check(lst):
    """Make URL's conform to standard pattern or omit from list."""
    out = []
    for url in lst:
        url.strip()
        if re.match(r"https://www.linkedin.com/in/", url):
            out.append(url)
        else:
            if re.match(r"http://www.linkedin.com/in/", url):
                end = url.split("//")[1]
                out.append(f"https://{end}")
            elif re.match(r"www.linkedin.com/in/", url):
                out.append(f"https://{url}")
            elif re.match(r"linkedin.com/in/", url):
                out.append(f"https://www.{url}")
    return out


def rand_sleep():
    """Function to return random value between 5 and 15"""
    return randrange(5, 16)


def rand_sleep2():
    """Function to return random value between 3 and 8"""
    return randrange(2, 8)


MESSAGE = "Hello {name}, fellow {school} student! I'm hoping to \
connect with other students to grow my network. Please connect \
with me if you are still trying to grow yours as well. Thanks! \
(sent by Python)"


ASCII_ART = r"""
                                                                                                      
                                                 JJ                                                   
        000j            QLL                    CJJJ             XUU       \YY                         
        000j            QQL                    CCJJ             UUU       YYY                         
        000j                                   CCCC             UUUU     'YYY:                        
        000j          QQQQQ    LLL .LLLL/      CCCC    JJJJ    -UUUU     YYYYY        YYXXX~          
        000r          QQQQQ    LLLLLLLLLLL[    CCCC   CCJJ     JJUUUU    UUUUY      YYYYYYXXXX        
        000j            QQQ    QLLL    LLLL    CCCC rCCC`      JJJUUU   UUUUYY     YYYY    XXXX       
        OO0r            QQQ    QQQ      LLLL   CCCCCCCC        JJJ>JUU  UUUUUUY   YYY?      XXX`      
        OOOr            00Q    QQQ      LLLL   CCCCCCCC       JJJJ JUU UUU  UUU   YYYYYYYYYYYYXX      
        OOOr            000    QQQ      LLLL   CCCCCCCCC      JJJ   UUUUUU  UUU   YYYYYYYYYYYYY.      
        OOOr            000    QQQ      LLLL   LLCC  CCCC     CCJ   JJUUU   UUUU  UUY                 
        OOOr            000    QQQ      LLLL   LLLL   CCCC   CCCC    JJJU    UUU  UUYU      Y         
        OOOOOOOOOOOO    000    0QQ      LLLL   LLLL    CCCC  CCC"    JJJ     UUU   UUUUUYYYYYY        
        OOOOOOOOOOOO    000    00Q      QLLL   LLLL     CCCC CCC      JJ     UUUu    UUUUYYYY         
                                                                                                
"""

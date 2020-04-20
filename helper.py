import re
from random import randrange


def check_for_login_data(USERNAME: str, PASSWORD: str, driver: str) -> None:
    """Make sure user entered their login data."""
    if not USERNAME or not PASSWORD or not driver:
        print("\n")
        if not USERNAME:
            print("> Missing Username! <".center(40, "-"))
            print("\n")
        if not USERNAME:
            print("> Missing Password! <".center(40, "-"))
            print("\n")
        if not driver:
            print("> Missing Chrome Driver! <".center(40, "-"))
            print("\n")
        raise ValueError("Missing Login Info or missing Chrome Driver info!")


def print_no_students_txt():
    """Print warning when no students.txt file is found."""
    print(f"""

        You must save a file of LinkedIn profile URL's as 
        students.txt in linkme directory.

        """)


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


def rand_sleep(switch):
    """Function to return random value between 2-7 when
    switch is true otherwise random value between 5-15."""
    if switch:
        return randrange(2, 6)
    return randrange(4, 9)


MESSAGE = "Hello {name}, fellow {school} student! I'm hoping to \
connect with other students to grow my network. Please connect \
with me if you are still trying to grow yours as well. Thanks! \
(sent by Python)"


ASCII_ART = r"""


                                        "                                         
      000          LLL                JJJ           UU      YY                    
      000           Ql                CCC          UUU     YYY                    
      000                     U~      CCC          UUUU    UUY        ?c          
      000         QQQQ   LLLLLLLLL    CCC  CJJ     JUUU   UUUYY    YYYYXXXXf      
      OO0          QQQ   LLL    LLL   CCC CCC     1JJUUU  UUUYU   YYY     XX>     
      OOO          00Q   QQQ    LLL   CCCCCC      JJJ JJ UUU UU   YYY11111YYX     
      OOO          00Q   QQQ    LLL   CLCCCCC     JJY JJJUU  UUU  UYYYYYYYYYX     
      OOO          000   QQQ    LLL   LLL  CCC   ?CC   JJUU  UUU  UUY             
      OOOOOOOO00   000   QQQ    QLL   LLL   CCC  CCC   JJJ    UU  IUUUY+XYY       
      OOOOOOOOOO   000   000    QLL   LLL    CCC CCJ    JJ    UUU   UUUUYYY       
                                                                                  
                                                                                                                                                                                                                                                                
"""

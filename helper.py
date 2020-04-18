def check_for_login_data(USERNAME: str, PASSWORD: str) -> None:
    """Make sure user entered their login data."""
    if not USERNAME or not PASSWORD:
        print('\n')
        if not USERNAME:       
            print('> Missing Username! <'.center(40, '-'))   
        else:
            print('> Missing Password! <'.center(40, '-'))
        print('\n')
        raise ValueError("Missing Login Info!")


MESSAGE = "Hi, I'm a fellow Springboard student hoping to\
connect with other students to grow my network. Please connect\
with me if you are still trying to grow yours as well. Thanks! 🐍👩‍🎓👩‍💻👨‍💻👨‍🎓💫"


ASCII_ART ="""
                                                                                                      
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
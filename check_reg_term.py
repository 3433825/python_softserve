def check_example(example_site):
    from try_whois import expect_whois

    ERR_MESS_TWO_POINTS = "Wrong site name"
    ERR_MESS_UNFINISHED_NAME = "Unfinished name"
    ERR_MESS_CHECK_SITE_NAME = "Check site name"

    if example_site.rfind("..") != -1:
        return ERR_MESS_TWO_POINTS
    elif example_site.endswith("."):
        return ERR_MESS_UNFINISHED_NAME
    elif example_site.rfind(".") == -1:
        return ERR_MESS_CHECK_SITE_NAME
    else:
        return expect_whois(example_site)
import logging
logging.basicConfig(filename="hay.log",level=logging.DEBUG)
def prime(n):
    if n==0:
        logging.debug("file created")
        return n
    else:
        return "wrong"
print(prime(0))




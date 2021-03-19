import ftplib

host = "myhost"
user = "root"
passw = "pass"
filename = "my.png"
con = ftplib.FTP(host, user, passw)
fp = open(filename, "rb")
band = con.storbinary("ST" + filename, fp)
con.close()

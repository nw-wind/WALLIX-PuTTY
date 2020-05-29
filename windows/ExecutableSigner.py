import os.path
import subprocess

target_file_name           = 'VS2015-WAB\putty\Release\putty.exe'
sign_cert_file_name        = 'SignCertFile.p12'
sign_cert_passwd_file_name = 'SignCertPasswdFile.txt'

if not os.path.isfile(target_file_name):
	print('not target_file_name');
else:
	print('target_file_name');
	
if not os.path.isfile(target_file_name):
   print('taget is wrong')
   exit(1)
                                     
if not os.path.isfile(sign_cert_file_name):
   print('cert is wrong')
   exit(2)                                  

if not os.path.isfile(sign_cert_passwd_file_name):
   print('password is wrong')
   exit(3)

print('ExecutableSigner');
with open(sign_cert_passwd_file_name, 'r') as sign_cert_passwd_file:
    sign_cert_passwd = sign_cert_passwd_file.read().replace('\n', '')
    subprocess.call(                                                    \
        ['C:\\Program Files (x86)\\Windows Kits\\8.1\\bin\\x86\\signtool.exe', 'sign', '/t',                                  \
         'http://timestamp.digicert.com', '/f', sign_cert_file_name,    \
         '/fd', 'sha256', '/p', sign_cert_passwd, target_file_name])

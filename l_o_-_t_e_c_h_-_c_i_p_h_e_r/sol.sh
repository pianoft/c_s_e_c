rm -rfv ./p1.png ./secret.png ./flag.png;

convert c1.png c2.png -gravity center -composite p1.png        

cp secret.zip ./secret.png;


convert ./secret.png p1.png -gravity center -composite flg.png

#p1.png は overlayed image .
#./secret.pngも白黒砂砂漠画像 .
#Visual cryptography .

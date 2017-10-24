function callTw(){
    /usr/bin/php7.0 -f '/home/nginx-chroot/home/4v1anc4C0mandc/prod/callTw.php'
}

function getConfigVals(){
    /usr/bin/php7.0 -f '/home/nginx-chroot/home/4v1anc4C0mandc/prod/callMongo.php'
}


# func1 parameters: a b
resultI=$(callTw)
result=$(getConfigVals)


INDEX=0
OIFS=$IFS
IFS='°'
mails2=$result

for y in $mails2

do
    #echo ${INDEX}
    let INDEX=${INDEX}+1
    #./BOT.py "$x"
done

INDEX1=0
for x in $mails2

do
    let INDEX1=${INDEX1}+1
    #let INDEX=${INDEX}+1
    if [ "$INDEX" -le "$INDEX1" ];then
    #echo $INDEX1
    #echo "Para";
        #./BOT.py "$x" "S"
        /usr/bin/python3.5 /home/nginx-chroot/home/4v1anc4C0mandc/prod/BOT.py "$x"
    else :
        #echo $INDEX1
        #echo $INDEX
        #echo "Sigue";
        #./BOT.py "$x" "N"
        /usr/bin/python3.5 /home/nginx-chroot/home/4v1anc4C0mandc/prod/BOT.py "$x"
    fi
done

IFS=$OIFS

exit 0


#!/bin/bash
network1=""
network2=""
tries=0
while [ -z "$network2" ]
do
	((tries++));
	network2=$(echo `sudo nmap -sn 192.168.1.0/24 | grep -B2 -i 74:da:38:42:3b:22 | grep -v -i 74:da:38:42:3b:22 | grep -v "Host"` | awk '{print $NF}');#
	echo "network 2 $network2";
	echo "try number $tries";
	
	if [ $tries -eq 3 ]; then
		echo "in if block";
		network2=`echo BAD2`;
		echo $network2;
	fi
done
tries=0
while [ -z "$network1" ]
do
	((tries++));
	network1=$(ifconfig | grep -oP '^\s*inet\s+(addr:)?\K\d+\.\d+\.\d+\.\d+' | grep -v '127.0.0.1');	
	echo "network 1 $network1";
	echo "try number $tries";
	
	if [ $tries -eq 3 ]; then
		echo "in if block";
		network1=`echo BAD1`;
		echo $network1;
	fi
done

echo $network1 $network2 >| network_info.py

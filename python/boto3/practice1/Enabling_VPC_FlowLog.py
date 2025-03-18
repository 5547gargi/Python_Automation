'''
 VPC flowlog captures all the traffic which is going in or out of your VPC.
 Traffic comming out your elastic network interface(eni).
 eg:- Accepted and rejected traffic
      In this example, SSH traffic (destination port 22, TCP protocol) from IP address 172.31.16.139 
      to network interface with private IP address is 172.31.16.21 and ID eni-1235b8ca123456789 in 
      account 123456789010 was allowed.
      2 123456789010 eni-1235b8ca123456789 172.31.16.139 172.31.16.21 20641 22 6 20 4249 1418530010 1418530070 ACCEPT OK  
      count_no        eni_id                 srcIP           destIP   srpt  dp  
      In this example, RDP traffic (destination port 3389, TCP protocol) to network interface eni-1235b8ca123456789 in account 123456789010 was rejected.
      2 123456789010 eni-1235b8ca123456789 172.31.9.69 172.31.9.12 49761 3389 6 20 4249 1418530010 1418530070 REJECT OK
'''
import boto3

ec2=boto3.client('ec2')
respons
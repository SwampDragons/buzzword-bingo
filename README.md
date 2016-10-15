# buzzword-bingo

# Testing

```
pip install -r requirements.txt
py.test
```

Or, to be really fancy with continouos output:

```
pip install pytest-watch
ptw -- -s
```

# SErving from EC2

Followed the directions here: http://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/
Instance is buzzword-bingo in us-west-2 datacenter
sauce users was run, so your creds should work
If you are remote, must be on VPN. IPs restricted to Sauce HQ.
Public DNS: ec2-52-53-167-110.us-west-1.compute.amazonaws.com

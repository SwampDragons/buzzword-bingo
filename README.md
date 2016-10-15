# buzzword-bingo

## Hosted

Hosted live at http://ec2-52-53-167-110.us-west-1.compute.amazonaws.com/

Any pushes to this repo will update there automatically.

## Testing

Tests run on pushes to master. You can also run them locally.

```
mkvirtualenv buzz
workon buzz
pip install -r requirements.txt
py.test
```

Or to be really fancy with continouos output:
```
pip install pytest-watch
ptw -- -s
```

## EC2 Setup

I followed the directions here:
http://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/

The instance is "buzzword-bingo" in the us-west-2 datacenter

sauce_users.yml was run, so your creds should work. Be sure to use the right port.

If you are remote, must be on VPN. IPs are restricted to Sauce HQ.

Public DNS:
  ec2-52-53-167-110.us-west-1.compute.amazonaws.com

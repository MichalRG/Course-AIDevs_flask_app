# Details

This is ownapi task which requires own api to run so I decided to move it to separate repo. This is simple main.py which run flask server on localhost. To make available server as VPS out of local network I used ngrok, I downloaded .exe file and I run in grok terminal:

```bash
ngrok http http://localhost:5000
```

it will create for u on pointed link your temp VPS to test. If I think correctly such testing is free doesn't reuqire additional fees.

Useful link how to use ngrok:
https://ngrok.com/docs/getting-started/?os=windows
https://dashboard.ngrok.com/get-started/setup/windows

Second endpoint /google allow to solve goole task it requres to set APIKEY_SERPAPI key to get access to serapi.

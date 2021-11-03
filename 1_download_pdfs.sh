# source of this script: https://stackoverflow.com/questions/21919156/how-do-i-copy-cookies-from-chrome?answertab=active#tab-top
# sharepoint folder of papers: https://liebertpub-my.sharepoint.com/personal/abrunson_liebertpub_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fabrunson%5Fliebertpub%5Fcom%2FDocuments%2F%2EJournal%20of%20Palliative%20Med%2Ftop%20100%20cited&originalPath=aHR0cHM6Ly9saWViZXJ0cHViLW15LnNoYXJlcG9pbnQuY29tLzpmOi9wL2FicnVuc29uL0VwWm9GUXJ4YkxCTXFGb1lqWHh2UmRnQktYbnVfNGZYeENqWFlLQW9tbmRtVUE%5FcnRpbWU9Qkgwa2JtcGQyVWc
curl 'https://eastus1-mediap.svc.ms/transform/zip?cs=fFNQTw' \
  -H 'authority: eastus1-mediap.svc.ms' \
  -H 'cache-control: max-age=0' \
  -H 'sec-ch-ua: "Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'origin: https://liebertpub-my.sharepoint.com' \
  -H 'content-type: application/x-www-form-urlencoded' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'sec-fetch-site: cross-site' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-dest: iframe' \
  -H 'accept-language: de-DE,de;q=0.9' \
  --data-raw 'zipFileName=top+100+cited.zip&guid=39b40e64-9b59-45ce-8917-cfc0eb8446b4&provider=spo&files=%7B%22items%22%3A%5B%7B%22name%22%3A%22top+100+cited%22%2C%22size%22%3A0%2C%22docId%22%3A%22https%3A%2F%2Fliebertpub-my.sharepoint.com%3A443%2F_api%2Fv2.0%2Fdrives%2Fb%21pbZ_HjLKBUyLBst7lZIlpskzotDjuQxOtJfvg_pKwtSxhSMFLmcBSb82HAkhe9cE%2Fitems%2F014NIIRCEWNAKQV4LMWBGKQWQYRV6G6ROY%3Fversion%3DPublished%26access_token%3DeyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvbGllYmVydHB1Yi1teS5zaGFyZXBvaW50LmNvbUAzMzlhNzEzZC1kNzcxLTQ0YjMtYmFkNC1iMjIxNzdjNmRkYWYiLCJpc3MiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAiLCJuYmYiOiIxNjM1ODk3NjAwIiwiZXhwIjoiMTYzNTkxOTIwMCIsImVuZHBvaW50dXJsIjoiK2x6ZDFvSXBJK1c1MGlXUVd5S05KK01kZzRhOFFPcG5aYTVteWRRV2R4RT0iLCJlbmRwb2ludHVybExlbmd0aCI6IjEyMCIsImlzbG9vcGJhY2siOiJUcnVlIiwidmVyIjoiaGFzaGVkcHJvb2Z0b2tlbiIsInNpdGVpZCI6Ik1XVTNabUkyWVRVdFkyRXpNaTAwWXpBMUxUaGlNRFl0WTJJM1lqazFPVEl5TldFMiIsIm5hbWVpZCI6IjAjLmZ8bWVtYmVyc2hpcHx1cm4lM2FzcG8lM2Fhbm9uI2RjOGJiZDI0M2UzZDk5YzlkMjJjNTMxMjQ1MmQ0YTZmYjUzNjMyOTM3YTkzOWMyNmFiYTlkMGU5NzUxODQzNWQiLCJuaWkiOiJtaWNyb3NvZnQuc2hhcmVwb2ludCIsImlzdXNlciI6InRydWUiLCJjYWNoZWtleSI6IjBoLmZ8bWVtYmVyc2hpcHx1cm4lM2FzcG8lM2Fhbm9uI2RjOGJiZDI0M2UzZDk5YzlkMjJjNTMxMjQ1MmQ0YTZmYjUzNjMyOTM3YTkzOWMyNmFiYTlkMGU5NzUxODQzNWQiLCJzaGFyaW5naWQiOiJRVjJ0V1hoSmhVQ3B6WVY4T3A4S3BnIiwidHQiOiIwIiwidXNlUGVyc2lzdGVudENvb2tpZSI6IjIiLCJpcGFkZHIiOiIxOTIuMTI0LjI2LjU2In0.YnAxYm41VGUwM1RqLzRlRWppUjdVVGorbFEyR0pUSDQwRk5EV2Myd200Yz0%22%2C%22isFolder%22%3Atrue%7D%5D%7D&oAuthToken=' \
  --compressed --output papers_jpm.zip
unzip papers_jpm.zip
mv 'top 100 cited' papers_jpm

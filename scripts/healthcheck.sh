if [ -z "$1" ]; then
  echo "Morate uneti argument koji predstavlja URL aplikacije koja se testira!"
  echo "Exit code: 0"
  exit 0
else
  for i in 1 2 3 4 5; do
    response=$(curl -s "$1/health")
    status=$(echo "$response" | jq -r '.status')
    http_code=$(curl -s -o /dev/null -w "%{http_code}" "$1/health")
    echo "[$(date + "%d-%m-%Y %H:%M:%S")] Pokusaj $i/5 - HTTP $http_code"
    sleep 3
  done
  if [ "$status" != "ok" ]; then
    echo "Exit code: 1"
    exit 1
  fi
fi
echo "Exit code: 0"
exit 0
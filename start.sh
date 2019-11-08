#! /bin/bash
# if (test lsof -i tcp:8080 | wc -l $gte 0);
#   then
#     echo "hey"
# fi
lsof -i tcp:8080 | wc -l | (read wc; 
  if (test $wc -eq 0); then
    python server3.py &
    sleep 5
    python client3.py
  elif (test $wc -ge 0); then
    python client3.py
  fi
)
# python client3.py
#!/bin/bash
# Today we are going to use a case statment instead of a conditional
# Have the program ask how your day is and echo out a response for good or bad
# Case statment format is a little different so please look up how this would be formated

echo "How is your day? Please select good and bad"
read response

case "$response" in
    "good")
    echo "that is great to hear, keep it up!"
    ;;
    "bad")
    echo "that is not great to hear, have a better day!"
    ;;
    *)
    echo "sorry, I did not understand your response"
    ;;
esac
#! /bin/bash

# Run on input file in Vim:
# :0 put =line('$')

read num;

sum_invalid=0;
sum=0;
for (( i=0; i<num; i++ ))
do
    read buf;
    game_num=`echo $buf | awk -F: '{print $1}' | awk '{print $2}'`
    game=`echo $buf | awk -F: '{print $2}'`
    num_rounds=`echo $game | awk -F';' '{print NF}'`;

    echo -n $game_num;
    sum=$((sum+game_num));
   
    for (( g=1; g<=num_rounds; g++ ))
    do
        c="echo '$game' | awk -F';' '{print \$${g}}'"
        round=`eval $c`;
        red=0;
        blue=0;
        green=0;

        if [[ $round =~ "red" ]];
        then
            red=`echo $round | awk -F'red' '{print $1}' | awk '{print $NF}'`;
        fi
        
        if [[ $round =~ "blue" ]];
        then
            blue=`echo $round | awk -F'blue' '{print $1}' | awk '{print $NF}'`;
        fi

        if [[ $round =~ "green" ]];
        then
            green=`echo $round | awk -F'green' '{print $1}' | awk '{print $NF}'`;
        fi

        if [ $red -gt 12 ] || [ $green -gt 13 ] || [ $blue -gt 14 ];
        then
            sum_invalid=$((sum_invalid+game_num));
            echo -n " Invalid $sum_invalid";
            break;
        fi;
    done;
    
    echo;
done;

let sum_valid=$sum-$sum_invalid;

echo "Sum of valid games -" $sum_valid;

#! /bin/bash

# Run on input file in Vim:
# :0 put =line('$')

read num;

sum=0;
for (( i=0; i<num; i++ ))
do
    read buf;
    game_num=`echo $buf | awk -F: '{print $1}' | awk '{print $2}'`
    game=`echo $buf | awk -F: '{print $2}'`
    num_rounds=`echo $game | awk -F';' '{print NF}'`;

    min_red=0;
    min_blue=0;
    min_green=0;
   
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
        
        if [[ $min_red -lt $red ]]; then
            min_red=$red;
        fi

        if [[ $min_blue -lt $blue ]]; then
            min_blue=$blue;
        fi

        if [[ $min_green -lt $green ]]; then
            min_green=$green;
        fi
    done;

    power=$((min_green * min_red * min_blue));
    echo "${game_num} ${power}";
    sum=$((power+sum));
done;

echo "Sum of powers -" $sum;

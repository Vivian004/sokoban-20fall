#!/bin/bash

PYTHON=`which python`
for i in {0..99}
do
	PYTHON game.py -l $i -i 3000 -a AStar >> ./output/AStar/$i.txt
	PYTHON game.py -l $i -i 3000 -a HillClimber >> ./output/HillClimber/$i.txt
done


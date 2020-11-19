PYTHON=`which python`

echo " " >> result.txt

for i in {1..99}
do
    PYTHON game.py -l $i -a MCTS | tail -1 >> result.txt
done
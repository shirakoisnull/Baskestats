#!/bin/bash

tmux new-session -d -s my_session
tmux set -g mouse
python_files=("login.py" "team.py" "player.py" "championship.py" "match.py")

for file in "${python_files[@]}"; do
    tmux split-window -h "python $file"
    tmux select-layout tiled
    tmux select-pane -R
done

tmux attach-session -t my_session

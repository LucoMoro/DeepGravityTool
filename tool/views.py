from django.shortcuts import render
from .models import cmdCommands
import os
import subprocess

#main html page
def tool(request):
    return render(request, 'tool/tool.html')

#html page to execute DeepGravity
def results(request):
    mode="train"
    batch_size="1"
    test_batch_size="1"
    epochs="1"
    lr="5e-6"
    momentum="0.9"
    seed="1234"
    log_interval="1"
    device="cpu"
    dataset="new_york"

    commands = cmdCommands.objects.all()
    for command in commands:
        if(command.name == "main_path"):
            main_path = command.command
        if(command.name == "mode"):
            mode = command.command
        if(command.name == "batch_size"):
            batch_size = command.command
        if(command.name == "test_batch_size"):
            test_batch_size = command.command
        if(command.name == "epochs"):
            epochs = command.command
        if(command.name == "lr"):
            lr = command.command
        if(command.name == "momentum"):
            momentum = command.command
        if(command.name == "seed"):
            seed = command.command
        if(command.name == "log_interval"):
            log_interval = command.command
        if(command.name == "device"):
            device = command.command
        if(command.name == "dataset"):
            dataset = command.command        

    cmd_command="python main.py --dataset "+dataset+" --oa-id-column GEOID --flow-origin-column geoid_o --flow-destination-column geoid_d --flow-flows-column pop_flows --epochs "+epochs+" --batch_size "+batch_size+" --test-batch-size "+test_batch_size+" --lr "+lr+" --momentum "+momentum+" --seed "+seed+" --log-interval "+log_interval+" --device "+device+" --mode "+mode
    os.chdir(main_path)
    subprocess.run(cmd_command, shell=True, check=True)
    data='Tutto deep_gravity andato a buon fine'
    return render(request, 'tool/results.html', {'data': data})


#html page to render the plots.ipynb file
def jupyter(request):
    commands = cmdCommands.objects.all()
    for command in commands:
        if(command.name == "plots_path"):
            jupyter_path = command.command
    os.chdir(jupyter_path)
    subprocess.run("jupyter notebook plots.ipynb", shell=True, check=True)
    data='Tutto jupyter andato a buon fine'
    return render(request, 'tool/jupyter.html', {'data': data})


def navtest(request):
    return render(request, 'tool/navtest.html')
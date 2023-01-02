from django.shortcuts import render
from .models import cmdCommands
import os
import subprocess


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
tessellation_area="new_york"
tessellation_size="25000"
tile_id_column="tile_ID"
tile_geometry="geometry"
oa_id_column="GEOID"
oa_geometry="geometry"
flow_origin_column="geoid_o"
flow_destination_column="geoid_d"
flow_flows_column="pop_flows"

#FIX MULTIPLE COMMAND LINES

#main html page
def tool(request):
    return render(request, 'tool/tool.html')

#html page to execute DeepGravity
def dg_results(request):
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
        if(command.name == "tessellation_area"):
            tessellation_area = command.command 
        if(command.name == "tessellation_size"):
            tessellation_size = command.command 
        if(command.name == "tile_id_column"):
            tile_id_column = command.command 
        if(command.name == "tile_geometry"):
            tile_geometry = command.command 
        if(command.name == "oa_id_column"):
            oa_id_column = command.command 
        if(command.name == "oa_geometry"):
            oa_geometry = command.command 
        if(command.name == "flow_origin_column"):
            flow_origin_column = command.command 
        if(command.name == "flow_destination_column"):
            flow_destination_column = command.command 
        if(command.name == "flow_flows_column"):
            flow_flows_column = command.command 
    cmd_command="python DG_main.py --dataset "+dataset+" --oa-id-column "+oa_id_column+" --flow-origin-column "+flow_origin_column+" --flow-destination-column "+flow_destination_column+" --flow-flows-column "+flow_flows_column+" --epochs "+epochs+" --batch_size "+batch_size+" --test-batch-size "+test_batch_size+" --lr "+lr+" --momentum "+momentum+" --seed "+seed+" --log-interval "+log_interval+" --device "+device+" --tessellation-area "+tessellation_area+" --tessellation-size "+tessellation_size+" --tile-id-column "+tile_id_column+" --tile-geometry "+tile_geometry+" --oa-geometry "+oa_geometry+" --mode "+mode
    print(epochs)
    os.chdir(main_path)
    subprocess.run(cmd_command, shell=True, check=True)
    data='DG eseguito con successo'
    return render(request, 'tool/dg_results.html', {'data': data})

def g_results(request):
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
        if(command.name == "tessellation_area"):
            tessellation_area = command.command 
        if(command.name == "tessellation_size"):
            tessellation_size = command.command 
        if(command.name == "tile_id_column"):
            tile_id_column = command.command 
        if(command.name == "tile_geometry"):
            tile_geometry = command.command 
        if(command.name == "oa_id_column"):
            oa_id_column = command.command 
        if(command.name == "oa_geometry"):
            oa_geometry = command.command 
        if(command.name == "flow_origin_column"):
            flow_origin_column = command.command 
        if(command.name == "flow_destination_column"):
            flow_destination_column = command.command 
        if(command.name == "flow_flows_column"):
            flow_flows_column = command.command 
    cmd_command="python G_main.py --dataset "+dataset+" --oa-id-column "+oa_id_column+" --flow-origin-column "+flow_origin_column+" --flow-destination-column "+flow_destination_column+" --flow-flows-column "+flow_flows_column+" --epochs "+epochs+" --batch_size "+batch_size+" --test-batch-size "+test_batch_size+" --lr "+lr+" --momentum "+momentum+" --seed "+seed+" --log-interval "+log_interval+" --device "+device+" --tessellation-area "+tessellation_area+" --tessellation-size "+tessellation_size+" --tile-id-column "+tile_id_column+" --tile-geometry "+tile_geometry+" --oa-geometry "+oa_geometry+" --mode "+mode
    
    os.chdir(main_path)
    subprocess.run(cmd_command, shell=True, check=True)
    data='G eseguito con successo'
    return render(request, 'tool/g_results.html', {'data': data})

def ng_results(request):
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
        if(command.name == "tessellation_area"):
            tessellation_area = command.command 
        if(command.name == "tessellation_size"):
            tessellation_size = command.command 
        if(command.name == "tile_id_column"):
            tile_id_column = command.command 
        if(command.name == "tile_geometry"):
            tile_geometry = command.command 
        if(command.name == "oa_id_column"):
            oa_id_column = command.command 
        if(command.name == "oa_geometry"):
            oa_geometry = command.command 
        if(command.name == "flow_origin_column"):
            flow_origin_column = command.command 
        if(command.name == "flow_destination_column"):
            flow_destination_column = command.command 
        if(command.name == "flow_flows_column"):
            flow_flows_column = command.command 
    cmd_command="python NG_main.py --dataset "+dataset+" --oa-id-column "+oa_id_column+" --flow-origin-column "+flow_origin_column+" --flow-destination-column "+flow_destination_column+" --flow-flows-column "+flow_flows_column+" --epochs "+epochs+" --batch_size "+batch_size+" --test-batch-size "+test_batch_size+" --lr "+lr+" --momentum "+momentum+" --seed "+seed+" --log-interval "+log_interval+" --device "+device+" --tessellation-area "+tessellation_area+" --tessellation-size "+tessellation_size+" --tile-id-column "+tile_id_column+" --tile-geometry "+tile_geometry+" --oa-geometry "+oa_geometry+" --mode "+mode
    
    os.chdir(main_path)
    subprocess.run(cmd_command, shell=True, check=True)
    data='NG eseguito con successo'
    return render(request, 'tool/ng_results.html', {'data': data})

def mfg_results(request):
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
        if(command.name == "tessellation_area"):
            tessellation_area = command.command 
        if(command.name == "tessellation_size"):
            tessellation_size = command.command 
        if(command.name == "tile_id_column"):
            tile_id_column = command.command 
        if(command.name == "tile_geometry"):
            tile_geometry = command.command 
        if(command.name == "oa_id_column"):
            oa_id_column = command.command 
        if(command.name == "oa_geometry"):
            oa_geometry = command.command 
        if(command.name == "flow_origin_column"):
            flow_origin_column = command.command 
        if(command.name == "flow_destination_column"):
            flow_destination_column = command.command 
        if(command.name == "flow_flows_column"):
            flow_flows_column = command.command 
    cmd_command="python MFG_main.py --dataset "+dataset+" --oa-id-column "+oa_id_column+" --flow-origin-column "+flow_origin_column+" --flow-destination-column "+flow_destination_column+" --flow-flows-column "+flow_flows_column+" --epochs "+epochs+" --batch_size "+batch_size+" --test-batch-size "+test_batch_size+" --lr "+lr+" --momentum "+momentum+" --seed "+seed+" --log-interval "+log_interval+" --device "+device+" --tessellation-area "+tessellation_area+" --tessellation-size "+tessellation_size+" --tile-id-column "+tile_id_column+" --tile-geometry "+tile_geometry+" --oa-geometry "+oa_geometry+" --mode "+mode
    
    os.chdir(main_path)
    subprocess.run(cmd_command, shell=True, check=True)
    data='MFG eseguito con successo'
    return render(request, 'tool/mfg_results.html', {'data': data})


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

def all_results(request):
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
        if(command.name == "tessellation_area"):
            tessellation_area = command.command 
        if(command.name == "tessellation_size"):
            tessellation_size = command.command 
        if(command.name == "tile_id_column"):
            tile_id_column = command.command 
        if(command.name == "tile_geometry"):
            tile_geometry = command.command 
        if(command.name == "oa_id_column"):
            oa_id_column = command.command 
        if(command.name == "oa_geometry"):
            oa_geometry = command.command 
        if(command.name == "flow_origin_column"):
            flow_origin_column = command.command 
        if(command.name == "flow_destination_column"):
            flow_destination_column = command.command 
        if(command.name == "flow_flows_column"):
            flow_flows_column = command.command 
    print(momentum)
    print(epochs)
    os.chdir(main_path)
    cmd_command="python DG_main.py --dataset "+dataset+" --oa-id-column "+oa_id_column+" --flow-origin-column "+flow_origin_column+" --flow-destination-column "+flow_destination_column+" --flow-flows-column "+flow_flows_column+" --epochs "+epochs+" --batch_size "+batch_size+" --test-batch-size "+test_batch_size+" --lr "+lr+" --momentum "+momentum+" --seed "+seed+" --log-interval "+log_interval+" --device "+device+" --tessellation-area "+tessellation_area+" --tessellation-size "+tessellation_size+" --tile-id-column "+tile_id_column+" --tile-geometry "+tile_geometry+" --oa-geometry "+oa_geometry+" --mode "+mode
    subprocess.run(cmd_command, shell=True, check=True)
    os.chdir(main_path)
    cmd_command="python G_main.py --dataset "+dataset+" --oa-id-column "+oa_id_column+" --flow-origin-column "+flow_origin_column+" --flow-destination-column "+flow_destination_column+" --flow-flows-column "+flow_flows_column+" --epochs "+epochs+" --batch_size "+batch_size+" --test-batch-size "+test_batch_size+" --lr "+lr+" --momentum "+momentum+" --seed "+seed+" --log-interval "+log_interval+" --device "+device+" --tessellation-area "+tessellation_area+" --tessellation-size "+tessellation_size+" --tile-id-column "+tile_id_column+" --tile-geometry "+tile_geometry+" --oa-geometry "+oa_geometry+" --mode "+mode
    subprocess.run(cmd_command, shell=True, check=True)
    os.chdir(main_path)
    cmd_command="python NG_main.py --dataset "+dataset+" --oa-id-column "+oa_id_column+" --flow-origin-column "+flow_origin_column+" --flow-destination-column "+flow_destination_column+" --flow-flows-column "+flow_flows_column+" --epochs "+epochs+" --batch_size "+batch_size+" --test-batch-size "+test_batch_size+" --lr "+lr+" --momentum "+momentum+" --seed "+seed+" --log-interval "+log_interval+" --device "+device+" --tessellation-area "+tessellation_area+" --tessellation-size "+tessellation_size+" --tile-id-column "+tile_id_column+" --tile-geometry "+tile_geometry+" --oa-geometry "+oa_geometry+" --mode "+mode
    subprocess.run(cmd_command, shell=True, check=True)
    os.chdir(main_path)
    cmd_command="python MFG_main.py --dataset "+dataset+" --oa-id-column "+oa_id_column+" --flow-origin-column "+flow_origin_column+" --flow-destination-column "+flow_destination_column+" --flow-flows-column "+flow_flows_column+" --epochs "+epochs+" --batch_size "+batch_size+" --test-batch-size "+test_batch_size+" --lr "+lr+" --momentum "+momentum+" --seed "+seed+" --log-interval "+log_interval+" --device "+device+" --tessellation-area "+tessellation_area+" --tessellation-size "+tessellation_size+" --tile-id-column "+tile_id_column+" --tile-geometry "+tile_geometry+" --oa-geometry "+oa_geometry+" --mode "+mode
    subprocess.run(cmd_command, shell=True, check=True)
    return render(request, 'tool/all_results.html')

def about_me(request):
    return render(request, 'tool/about_me.html')

def how_to_use(request):
    return render(request, 'tool/how_to_use.html')

def plot_results(request):
    return render(request, 'tool/plot_results.html')

def experiments(request):
    return render(request, 'tool/experiments.html')

def inputs(request):
    return render(request, 'tool/inputs.html')
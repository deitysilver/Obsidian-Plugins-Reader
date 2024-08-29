import os
import json

def read_plugin_folders(plugin_dir):
    folders = []
    try:
        for entry in os.listdir(plugin_dir):
            path = os.path.join(plugin_dir, entry)
            if os.path.isdir(path):
                folders.append(entry)
    except FileNotFoundError:
        print(f"Directory not found: {plugin_dir}")
    return folders

def read_active_plugins(active_plugins_file):
    try:
        with open(active_plugins_file, 'r') as file:
            active_plugins = json.load(file)
    except FileNotFoundError:
        print(f"File not found: {active_plugins_file}")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {active_plugins_file}")
        return []
    return active_plugins

def write_plugins_json(plugin_list, output_file, active_plugins):
    plugins_data = []
    for plugin in plugin_list:
        status = "active" if plugin in active_plugins else "inactive"
        plugins_data.append({plugin: status})

    try:
        with open(output_file, 'w') as file:
            json.dump(plugins_data, file, indent=2)
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")

plugin_dir = './plugins'
community_plugins_file = './community-plugins.json'
output_file = './plugins.json'

plugin_list = read_plugin_folders(plugin_dir)

active_plugins = read_active_plugins(community_plugins_file)

write_plugins_json(plugin_list, output_file, active_plugins)

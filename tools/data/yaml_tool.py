
import yaml

def get_yaml(yaml_path):
    with open(yaml_path,'r',encoding='utf-8') as f:
        content =yaml.load(f.read(),Loader=yaml.FullLoader)
    return content